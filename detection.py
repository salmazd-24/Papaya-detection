import streamlit as st
from pathlib import Path
import PIL
import settings
import helper
import io

# Main page heading
st.title("Deteksi Kematangan Pepaya Menggunakan YOLOv8")

# Sidebar
st.sidebar.header("Konfigurasi Model ML")

# Model Options
confidence = float(st.sidebar.slider(
    "Pilih Model Confidence (%)", 25, 100, 40)) / 100

model_path = Path(settings.DETECTION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Tidak dapat memuat model. Periksa path yang ditentukan: {model_path}")
    st.error(ex)

st.sidebar.header("Konfigurasi Gambar")
source_radio = st.sidebar.radio(
    "Pilih Sumber", settings.SOURCES_LIST)

source_img = None
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Pilih gambar...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                default_image_path = str(settings.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Gambar Default",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Gambar yang Diunggah",
                         use_column_width=True)
        except Exception as ex:
            st.error("Terjadi kesalahan saat membuka gambar.")
            st.error(ex)

    with col2:
        if source_img is None:
            default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Gambar Terdeteksi',
                     use_column_width=True)
        else:
            if st.sidebar.button('Deteksi Objek'):
                res = model.predict(uploaded_image,
                                    conf=confidence
                                    )
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Gambar Terdeteksi',
                         use_column_width=True)
                try:
                    with st.expander("Hasil Deteksi"):
                        for box in boxes:
                            st.write(box.data)
                except Exception as ex:
                    st.write("Belum ada gambar yang diunggah!")

                # Save to history
                if 'history' not in st.session_state:
                    st.session_state.history = []
                st.session_state.history.append({
                    "image": source_img,
                    "result": res_plotted,
                    "boxes": boxes
                })

elif source_radio == settings.WEBCAM:
    helper.play_webcam(confidence, model)

else:
    st.error("Pilih jenis sumber yang valid!")