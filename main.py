import gradio as gr

def predict(text):
    return "Reviewed Code: " + text

demo = gr.Interface(
    fn=predict,
    inputs="text",
    outputs="text"
)

demo.launch()
