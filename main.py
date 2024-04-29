import gradio as gr

def image_text_block(image: gr.Image, text: str):
    return image, text

inputs = [
    gr.Image(label="Input Image"),
    gr.Textbox(lines=5, label="Input Text")
]

outputs = gr.Image(label="Output Image", type="filepath")

gr.Interface(fn=image_text_block, inputs=inputs, outputs=outputs).launch()
