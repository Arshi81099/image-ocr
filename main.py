import pytesseract
from PIL import Image
import gradio as gr

# Set the path to Tesseract (this is not needed on Colab, as Tesseract is installed globally)
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Function to extract text from the image (supports Hindi and English)
def extract_text(image):
    # Specify both Hindi (hin) and English (eng) for OCR
    extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
    return extracted_text

# Function to search for a keyword in the extracted text
def search_text(extracted_text, keyword):
    if keyword.lower() in extracted_text.lower():
        # Highlight the keyword
        highlighted_text = extracted_text.replace(keyword, f"**{keyword}**")
        return highlighted_text
    else:
        return "No match found for the given keyword."

# Gradio interface
def process_image_and_search(image, keyword):
    text = extract_text(image)
    result = search_text(text, keyword)
    return text, result

with gr.Blocks() as demo:
    gr.Markdown("## OCR and Keyword Search Web Application (Supports Hindi and English)")

    image_input = gr.Image(type="pil", label="Upload an Image for OCR")
    extracted_text_output = gr.Textbox(label="Extracted Text", interactive=False)
    keyword_input = gr.Textbox(label="Enter a Keyword to Search in Extracted Text")
    search_output = gr.Markdown(label="Search Results")

    submit_button = gr.Button("Submit")
    submit_button.click(fn=process_image_and_search, inputs=[image_input, keyword_input], outputs=[extracted_text_output, search_output])

# Launch the app
demo.launch()
