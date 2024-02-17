import asyncio

import gradio as gr

from agents.basic import greet, ask_with_context


def main():

    with gr.Blocks() as demo:
        gr.Markdown(
            """
        # itsjeffandmel specialist
        Type something in the input box and then press the Go! button to see the output
        """
        )
        with gr.Row():
            with gr.Column(scale=2):
                inp = gr.Textbox(placeholder="Type in your question.")
                input_button = gr.Button(value="Get Response")
            with gr.Column(scale=3):
                out = gr.Textbox()

        input_button.click(ask_with_context, inp, out)

    demo.launch()


if __name__ == "__main__":
    asyncio.run(main())
