**Building-AI-Powered-Solution-For-Assisting -Visually-Impaired-Individuals**
**Features of AI Assist
OCR (Optical Character Recognition):**

**Functionality:**

Extracts text from an uploaded image using pytesseract.

**How it Works:**

The extract_text_from_image() function processes the image to extract readable text content.

Use Case: Helps in reading text from documents, signage, or images with embedded text.

Interaction: Triggered via the "📝 Text Mining" button.

**Text-to-Speech Conversion:**

**Functionality:**

Converts extracted text into speech using pyttsx3.

**How it Works:**

The text_to_speech() function takes the extracted text and generates audio output.

Use Case: Enables visually impaired users to "listen" to the text present in an image.

Interaction: Triggered via the "📝 Text-to-🔊 Audio" button.

**Scene Description Using Google Generative AI**

**Functionality:**

Generates detailed scene descriptions using Google Generative AI (Gemini Model).

Provides:

List of items detected in the image.

Overall description of the image.

Suggestions or precautions for visually impaired individuals.

How it Works:

The generate_scene_description() function uses Google Generative AI to process the input prompt and image data, generating descriptive responses.

Use Case: Assists visually impaired users in understanding the context and objects present in a scene.

Interaction: Triggered via the "🔍 Describe Scene" button.

Streamlit-Powered UI

Streamlit Framework:

Provides an interactive and user-friendly interface.

UI Components:

Image Uploader: Upload images in .jpg, .jpeg, or .png formats.

Buttons: For triggering text extraction, text-to-speech, and scene description.

Sidebar Features: Highlights the app’s capabilities.

**Accessibility-Centric Design:**

Designed specifically for visually impaired users with clear functionalities:

Extracting and reading text.

Generating audible descriptions of visual content.

AI-based suggestions for enhanced accessibility.

Error Handling:

File Upload Check:

Verifies if a file is uploaded before processing.

Text Availability Check:

Ensures that text exists before initiating text-to-speech conversion.

**Google Generative AI Integration:**

Model Used:

Google Gemini 1.5 Pro.

Customization:

Allows scene description tailored to visually impaired needs using the input prompt.

Modular and Reusable Functions:

Functions like extract_text_from_image(), text_to_speech(), and generate_scene_description() are modular and can be reused in other applications.
