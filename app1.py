import os
import streamlit as st
from cnnClassifier.pipeline.predict import PredictionPipeline
import io
from PIL import Image

# Client App for saving the filepath
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


# For running the complete pipeline
def main():

    # giving a title to the streamlit website
    st.title("Check for the Chicken Coccidiosis Disease")
    # st.markdown("*Streamlit* is **really** ***cool***.")

    # Getting the input image file from the user
    uploaded_image = st.file_uploader("Select the Image (JPG Format): ", type= "jpg",accept_multiple_files=False)

    if uploaded_image:
        # Converting the image to bytes
        bytes_data_image = uploaded_image.getvalue()

        # Converting the bytes back to image
        image_conv = Image.open(io.BytesIO(bytes_data_image))

        # Saving the image to the filepath specified in clApp.filename
        image_conv.save(clApp.filename)

        # Creating a button for prediction
        if st.button("Disease Test Result"):
            result = clApp.classifier.predict()
            
            # Analysing the result and then giving the statement
            if (result[0]['image'] == "Healthy"):
                st.success("The chicken is healthy")
            
            else:
                st.success("The chicken is infected with Coccidiosis")
        if st.button("Train"):
            os.system("dvc repro")
            st.success("Training Successful!")



if __name__ == "__main__":
    clApp = ClientApp()
    main()
    

