import streamlit as st
from keras.preprocessing.image import load_img, img_to_array
import pickle

st.set_page_config(
    page_title="LUNG CANCER PREDICTION APP",
    page_icon="🫁",
)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.mobiuspace.com/image/aigc/ba9208c4e85a806fee08815688a3b2d3_3276_2048.webp");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
# Load the saved model
with open('best_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Set the target image size
target_size = (224, 224)  # Replace with the actual target size used during training

# Function to preprocess the user input image
def preprocess_image(uploaded_file, target_size):
    # Use BytesIO to read file content
    image = load_img(uploaded_file, target_size=target_size)
    img_array = img_to_array(image)
    flattened_img_array = img_array.reshape(1, -1)
    return flattened_img_array

# Define class folder names
class_folder_names = [
    'adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib',
    'large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa',
    'normal',
    'squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa'
]
# Streamlit app

new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">LUNG CANCER DETECTION APP</p>'
st.markdown(new_title, unsafe_allow_html=True)
#File uploader for user input image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    # Preprocess the user input image
    st.image(uploaded_file)
    Genrate_pred = st.button("Generate Prediction")
    if Genrate_pred:
        user_input_img = preprocess_image(uploaded_file, target_size)

    # Make predictions on the user input image
        predictions = loaded_model.predict(user_input_img)

    # Get the predicted class
        predicted_class = class_folder_names[predictions[0]]

        st.markdown(f'<p style="font-family:sans-serif; color:white; font-size: 25px;">The predicted image is of type:</p>',unsafe_allow_html=True)

    # Customize the output label with color and font
        output_label = f'<p style="font-family:sans-serif; color:white; font-size: 25px;">{predicted_class}</p>'
    
    # Display the customized output label
        st.markdown(output_label, unsafe_allow_html=True)

    # Display the user input image with the predicted class
        st.image(uploaded_file, caption="User input image")
