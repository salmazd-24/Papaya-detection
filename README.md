# <span style="color:deepskyblue"> Real-time Papaya Ripeness Detection with YOLOv8 & Streamlit </span>

This repository is an extensive open-source project showcasing the seamless integration of **object detection** using **YOLOv8** (object detection algorithm), along with **Streamlit** (a popular Python web application framework for creating interactive web apps). The project offers a user-friendly and customizable interface designed to detect and track objects in real-time video streams from sources such as webcam, static videos and images.


## <span style="color:deepskyblue">WebApp Demo on Streamlit Server</span>

This app is up and running on Streamlit cloud server!!! You can check the demo of this web application on this link 
[Papaya-detection](https://papaya-detection.streamlit.app/)

Username: admin    
Password: password12345

## Installation

- Clone the repository: git clone <https://github.com/salmazd-24/Papaya-detection.git>
- Change to the repository directory: `cd Papaya-detection`
- Create `weights`, `videos`, and `images` directories inside the project.

## Usage

- Run the app with the following command: `streamlit run main.py`
- The app should open in a new browser window.

### ML Model Config

- Select model confidence
- Use the slider to adjust the confidence threshold (25-100) for the model.

One the model config is done, select a source.

### Detection on images

- The default image with its objects-detected image is displayed on the main page.
- Select a source. (radio button selection `Image`).
- Upload an image by clicking on the "Browse files" button.
- Click the "Detect Objects" button to run the object detection algorithm on the uploaded image with the selected confidence threshold.
- The resulting image with objects detected will be displayed on the page. Click the "Download Image" button to download the image.("If save image to download" is selected)

## Acknowledgements

This app uses [YOLOv8](<https://github.com/ultralytics/ultralytics>) for object detection algorithm and [Streamlit](<https://github.com/streamlit/streamlit>) library for the user interface.
