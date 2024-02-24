import asyncio

import gradio as gr
from dotenv import load_dotenv

from agents.basic import ask_with_context


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
                comment = gr.Textbox(
                    placeholder="Please paste comment here.",
                    label="Comment",
                    value="wow you are so cool!",
                )
                additional_info = gr.Textbox(
                    placeholder="Please paste any additional info here.",
                    label="Additional Info",
                )

            with gr.Column(scale=3):
                chatbot = gr.Chatbot()
                input = gr.Textbox(
                    placeholder="Prompt the LLM.",
                    value="Please write a reply to the comment.",
                )
                get_response_btn = gr.Button(value="Get Response")

        get_response_btn.click(
            ask_with_context,
            [input, chatbot, comment, additional_info],
            [input, chatbot],
        )

    demo.launch()


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
