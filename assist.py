import streamlit as st
from PIL import Image
import pytesseract
import pyttsx3
import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI

print(pytesseract)
# Initialize Google Generative AI with API Key
GEMINI_API_KEY = ""  # Replace with your valid API key
os.environ["AIzaSyDCf6aYDvHk0aViC_uP-N_OgaJdC2sUfAI"] = GEMINI_API_KEY

llm = GoogleGenerativeAI(model="gemini-1.5-pro", api_key=GEMINI_API_KEY)

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Set up Streamlit page
st.set_page_config(page_title="SightAssist", layout="wide")
st.title("🤖 AI ASSIST - Visually Impaired individuals")
st.sidebar.title("Features of AI Assist")
st.sidebar.markdown("""
**OCR (Optical Character Recognition)**:\n
**Functionality:**\n
Extracts text from an uploaded image using pytesseract.\n
**How it Works:**\n
The extract_text_from_image() function processes the image to extract readable text content.\n
**Use Case:** Helps in reading text from documents, signage, or images with embedded text.\n
**Interaction:** Triggered via the "📝 Text Mining" button.\n
**Text-to-Speech Conversion:**\n
**Functionality:**\n
Converts extracted text into speech using pyttsx3.\n
**How it Works:**\n
The text_to_speech() function takes the extracted text and generates audio output.\n
**Use Case:** Enables visually impaired users to "listen" to the text present in an image.\n
**Interaction:** Triggered via the "📝 Text-to-🔊 Audio" button.\n
**Scene Description Using Google Generative AI**\n
**Functionality:**\n
Generates detailed scene descriptions using Google Generative AI (Gemini Model).\n
**Provides:**\n
List of items detected in the image.\n
Overall description of the image.\n
Suggestions or precautions for visually impaired individuals.\n
**How it Works:**\n
The generate_scene_description() function uses Google Generative AI to process the input prompt and image data, generating descriptive responses.\n
**Use Case:** Assists visually impaired users in understanding the context and objects present in a scene.\n
**Interaction:** Triggered via the "🔍 Describe Scene" button.\n
**Streamlit-Powered UI**\n
**Streamlit Framework:**\n
Provides an interactive and user-friendly interface.\n
**UI Components:**\n
**Image Uploader:** Upload images in .jpg, .jpeg, or .png formats.\n
**Buttons:** For triggering text extraction, text-to-speech, and scene description.\n
**Sidebar Features:** Highlights the app’s capabilities.\n
** Accessibility-Centric Design:**\n
**Designed specifically for visually impaired users with clear functionalities:**\n
Extracting and reading text.\n
Generating audible descriptions of visual content.\n
AI-based suggestions for enhanced accessibility.\n
**Error Handling:**\n
**File Upload Check:**\n
Verifies if a file is uploaded before processing.\n
**Text Availability Check:**\n
Ensures that text exists before initiating text-to-speech conversion.\n
** Google Generative AI Integration:**\n
**Model Used:**\n
Google Gemini 1.5 Pro.\n
**Customization:**\n
Allows scene description tailored to visually impaired needs using the input prompt.\n
**Modular and Reusable Functions:**\n
Functions like extract_text_from_image(), text_to_speech(), and generate_scene_description() are modular and can be reused in other applications.

""")

def extract_text_from_image(image):
    """Extracts text from the given image using OCR."""
    text = pytesseract.image_to_string(image)
    return text

def text_to_speech(text):
    """Converts the given text to speech."""
    engine.say(text)
    engine.runAndWait()

def generate_scene_description(input_prompt, image_data):
    """Generates a scene description using Google Generative AI."""
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input_prompt, image_data[0]])
    return response.text

def input_image_setup(uploaded_file):
    """Prepares the uploaded image for processing."""
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError(" 📁 No file uploaded.")

# Main app functionality
uploaded_file = st.file_uploader("📸 Upload an image...", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Uploaded Image", use_container_width=True)

# Buttons for functionalities
col1, col2, col3 = st.columns(3)
ocr_button = col1.button("📝 Text Mining")
tts_button = col2.button("📝 Text-to-🔊Audio")

scene_button = col3.button("🔍 Describe Scene")

# Input Prompt for AI Scene Understanding
input_prompt = """
You are an AI assistant helping visually impaired individuals by describing the scene in the image. Provide:
1. List of items detected in the image with their purpose.
2. Overall description of the image.
3. Suggestions for actions or precautions for the visually impaired.
"""

# Process based on user interaction
if uploaded_file:
    image_data = input_image_setup(uploaded_file)

    if scene_button:
        with st.spinner("Generating scene description..."):
            response = generate_scene_description(input_prompt, image_data)
            st.subheader("Scene Description")
            st.write(response)

    if ocr_button:
        with st.spinner(" 📝 Extracting text from image..."):
            text = extract_text_from_image(image)
            st.subheader("Extracted Text")
            st.write(text)

    if tts_button:
        with st.spinner(" 🗣 Converting text to speech..."):
            text = extract_text_from_image(image)
            if text.strip():
                text_to_speech(text)
                st.success("Text-to-Speech Conversion Completed!")
            else:
                st.warning("No text found in the image.")
