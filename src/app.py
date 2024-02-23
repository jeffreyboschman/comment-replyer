import asyncio

import gradio as gr
from dotenv import load_dotenv

from agents.basic import ask_with_context

_SYSTEM_PROMPT = """
    Please act as an expert in social media, marketing, and psychology 
    who is hired to be our social media content assistant.

    We are a Canadian couple on YouTube and Instagram who 
    mainly make posts about our life in Tokyo, Japan. 

    Our vibe is cozy, charming, polite, casual, light, bright,
    clean, relatable, humble, genuine, and Ghibli-esque.

    Please help us develop content by following the user instructions or answering questions.
    """


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
                get_response_btn = gr.Button(value="Get Response")

                default_prompt = gr.Textbox(
                    label="System Prompt",
                    value=_SYSTEM_PROMPT,
                    interactive=True,
                    elem_id="system-prompt",
                )
            with gr.Column(scale=3):
                out = gr.Textbox()

        get_response_btn.click(ask_with_context, [inp, default_prompt], out)

    demo.launch()


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
