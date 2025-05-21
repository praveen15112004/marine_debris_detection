import streamlit as st
import app  
import seaborn as sns
import matplotlib.pyplot as plt
from inference import garbage 
import base64
from PIL import Image

labels = ['Mask', 'can', 'cellphone', 'electronics', 'gbottle', 'glove', 
          'metal', 'misc', 'net', 'pbag', 'pbottle', 'plastic', 
          'rod', 'sunglasses', 'tire']

def get_video_base64(video_path):
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
        base64_video = base64.b64encode(video_bytes).decode("utf-8")
    return f"data:video/mp4;base64,{base64_video}"

def main():
    st.set_page_config(layout="wide")
    
  
    menu = ["Home", "Detection", "Generate Report"]
    selected_page = st.sidebar.radio("", menu)
    
    if selected_page == "Home":
        
        video_path = "01.mp4"  
        video_url = get_video_base64(video_path)
        st.markdown(
            f"""
            <style>
            
                .video-container {{
                    position: relative;
                    width: 100vw;
                    height: 100vh;
                    overflow: hidden;
                }}
                .video-container video {{
                    width: 100vw;
                    height: 100vh;
                    object-fit: cover;
                }}
                .overlay-text {{
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    font-size: 3em;
                    font-weight: bold;
                    color: white;
                    text-align: center;
                    background: rgba(0, 0, 0, 0.5);
                    padding: 20px;
                    border-radius: 10px;
                }}
                
            </style>
            <div class='video-container'>
                <video autoplay loop muted>
                    <source src='{video_url}' type='video/mp4'>
                </video>
                 <div class='overlay-text'>Welcome to Marine Debris Detection</div>
            </div>
           
            """,
            unsafe_allow_html=True
        )
        
        
        st.markdown("""
    <div style='width: 100vw; padding: 50px; background-color: #d9f3ff; text-align: center;'>
        <h2>How Marine Debris Causes Problems</h2>
        <p>Marine debris harms marine life, disrupts ecosystems, and pollutes our oceans.</p>
    </div>
""", unsafe_allow_html=True)


        image_height = 300  
        image_width=500
        def load_and_resize(image_path, width, height):
            img = Image.open(image_path)
            img = img.resize((width, height))  
            return img
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image(load_and_resize("image1.jpg", image_width, image_height))
            st.markdown("<h4 style='text-align: center';>Harm to Marine Life</h4>", unsafe_allow_html=True)
            st.write("Marine animals mistake debris for food, leading to ingestion and entanglement.")

        with col2:
            st.image(load_and_resize("image2.jpg", image_width, image_height))
            st.markdown("<h4 style='text-align: center;'>Disruption of Ecosystems</h4>", unsafe_allow_html=True)
            st.write("Plastic waste alters natural habitats, affecting marine biodiversity.")

        with col3:
            st.image(load_and_resize("image3.jpg", image_width, image_height))
            st.markdown("<h4 style='text-align: center;'>Impact on Humans</h4>", unsafe_allow_html=True)
            st.write("Polluted oceans affect fisheries, tourism, and human health due to toxins.")

        
        st.markdown("""
            <style>
                .about-container {
                    width: 100vw;
                    padding: 40px;
                    background-color: #c2e0f7;
                    text-align: center;
                }
                .about-container h2 {
                    color: #003366;
                    font-size: 28px;
                    margin-bottom: 15px;
                }
                .about-container p {
                    color: #000;
                    font-size: 16px;
                    max-width: 700px;
                    margin: 0 auto;
                    line-height: 1.5;
                }
                .highlight {
                    color: #0077b6;
                    font-weight: bold;
                }
            </style>

            <div class="about-container">
                <h2>🌊 About Us</h2>
                <p>The health of our oceans is under threat due to increasing marine pollution. 
                    <span class="highlight">Neural Ocean</span> is dedicated to tackling this global challenge 
                    using cutting-edge <span class="highlight">AI and deep learning</span>. Our advanced object detection 
                    models, such as <span class="highlight">YOLOv8</span>, enable accurate identification of marine debris, 
                    supporting environmental conservation efforts worldwide.
                      By leveraging technology, we empower researchers, conservationists, and policymakers with 
                    real-time data to take proactive steps toward cleaner oceans. Join us in our mission to protect marine 
                    ecosystems and promote a sustainable future. 🌍
                </p>
                    
                  
                
            </div>
        """, unsafe_allow_html=True)
    
    elif selected_page == "Detection":
        app.app()  
    
    elif selected_page == "Generate Report":
        st.title("Generated Report")
        
       
        occurrences = [garbage.count(label) for label in labels]
        
        
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(y=labels, x=occurrences, ax=ax, palette="coolwarm")
        ax.set_xlabel("Occurrences", fontsize=12)
        ax.set_ylabel("Labels", fontsize=12)
        ax.set_title("Histogram of Waste Occurrences", fontsize=14)
        st.pyplot(fig)
        
       
        most_frequent_label = labels[occurrences.index(max(occurrences))]
        st.markdown(f"""
            <div style='width: 100%; padding: 20px; background-color: #d9f3ff; text-align: center;'>
                <h3>Conclusion</h3>
                <p>The most frequently detected waste type is <b>{most_frequent_label}</b>, appearing <b>{max(occurrences)}</b> times in recent observations.</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()