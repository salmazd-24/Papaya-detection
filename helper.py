from ultralytics import YOLO
import streamlit as st
import cv2
from .settings import WEBCAM_PATH

def display_tracker_options():
    display_tracker = st.radio("Display Tracker", ('Yes', 'No'))
    is_display_tracker = True if display_tracker == 'Yes' else False
    if is_display_tracker:
        tracker_type = st.radio("Tracker", ("bytetrack.yaml", "botsort.yaml"))
        return is_display_tracker, tracker_type
    return is_display_tracker, None

def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    image = cv2.resize(image, (720, int(720*(9/16))))

    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        res = model.predict(image, conf=conf)

    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )

def play_webcam(conf, model):
    is_display_tracker, tracker = display_tracker_options()

    if st.sidebar.button('Buka Kamera'):
        try:
            vid_cap = cv2.VideoCapture(WEBCAM_PATH)
            st_frame = st.empty()

            if not vid_cap.isOpened():
                raise RuntimeError('Could not open webcam.')

            while True:
                success, image = vid_cap.read()
                if not success:
                    break

                _display_detected_frames(conf, model, st_frame, image, is_display_tracker, tracker)

                # Delay to match the webcam frame rate
                st.time.sleep(0.1)

            vid_cap.release()
        except RuntimeError as e:
            st.sidebar.error(f"Error loading webcam: {e}")
        except Exception as e:
            st.sidebar.error(f"Unexpected error: {e}")