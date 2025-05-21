import cv2
import streamlit as st
import numpy as np
import dark_channel_prior as dcp
import inference as inf


def remove_noise(image):
    
    processed_image, alpha_map = dcp.haze_removal(image, w_size=15, a_omega=0.95, gf_w_size=200, eps=1e-6)
    return processed_image



def detect_objects(image):
    
    output_image, class_names = inf.detect(image)
    return output_image, class_names



def app():
    st.markdown(
        """
        <style>
            .stApp {
                
                background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 50%, rgba(0,212,255,1) 100%);
                background-size: cover;
            }
           .stText, .stTitle, .stHeader, .stSubheader, .stMarkdown {
                color: #ffff;
                }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<h1 style='color: white;'>Underwater Waste Detection Model</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white;'>Upload an image to detect objects</h3>", unsafe_allow_html=True)
   
        
    
    file = st.file_uploader("Choose file", type=["jpg", "jpeg", "png"])
    
    if file is not None:
        input_image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
        input_image = cv2.resize(input_image, (416, 416))
        st.markdown("<h3 style='color: white;'>Input Image:</h3>", unsafe_allow_html=True)
        st.image(input_image)

        
        st.markdown("<h3 style='color: white;'>Removing noise from input...</h3>", unsafe_allow_html=True)
        
        processed_image = remove_noise(input_image)
        st.image(processed_image, clamp=True)


       
        st.markdown("<h3 style='color: white;'>Running the model...</h3>", unsafe_allow_html=True)
        output_image, class_names = detect_objects(processed_image)

        
        st.markdown("<h3 style='color: white;'>Output Image:</h3>", unsafe_allow_html=True)
        
        st.image(output_image)
        if len(class_names)==0:
            st.success("The water is clear!!!")
        else:
            st.error(f"Waste Detected!!!\nThe image has {class_names}")