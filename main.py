import gradio as gr

def image_comment_block(image_url: str, comment: str):
    return image_url, comment

inputs = [
    gr.Textbox(lines=5, label="Comment")
]

outputs = gr.Image(label="Image",)

gr.Interface(fn=image_comment_block, inputs=inputs, outputs=outputs, examples=[
    ["https://images.pexels.com/videos/852286/free-video-852286.jpg", "This is a nice image!"]
]).launch()
