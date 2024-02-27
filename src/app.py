import asyncio
import textwrap

import gradio as gr
from dotenv import load_dotenv

from agents.comment_replyer import generate_comment_response
from agents.general_helper import get_general_help
from agents.title_generator import generate_titles
from core.background_info import (_DEFAULT_SYSTEM_PROMPT,
                                  _DEFAULT_SYSTEM_PROMPT_SUFFIX)


def main():

    with gr.Blocks() as demo:
        gr.Markdown(
            """
        # itsjeffandmel specialist
        Type something in the input box and then press the Go! button to see the output
        """
        )
        with gr.Tab(label="General Help"):
            with gr.Row():
                with gr.Column(scale=2):
                    default_prompt = gr.Textbox(
                        label="System Prompt",
                        value=_DEFAULT_SYSTEM_PROMPT,
                        interactive=True,
                        elem_id="system-prompt",
                    )
                    default_prompt_suffix = gr.Textbox(
                        label="System Prompt Suffix",
                        value=_DEFAULT_SYSTEM_PROMPT_SUFFIX,
                        interactive=True,
                        elem_id="system-prompt-suffix",
                    )

                with gr.Column(scale=3):
                    chatbot = gr.Chatbot(show_copy_button=True)
                    input = gr.Textbox(
                        placeholder="Prompt the LLM.",
                        value="Please write a haiku about kichijoji",
                    )
                    get_response_btn = gr.Button(value="Get Response")

            get_response_btn.click(
                get_general_help,
                [input, chatbot, default_prompt, default_prompt_suffix],
                [input, chatbot],
            )
        with gr.Tab(label="Comment Replyer"):
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
                    chatbot = gr.Chatbot(show_copy_button=True)
                    input = gr.Textbox(
                        placeholder="Prompt the LLM.",
                        value="Please write a reply to the comment.",
                    )
                    get_response_btn = gr.Button(value="Get Response")

            get_response_btn.click(
                generate_comment_response,
                [input, chatbot, comment, additional_info],
                [input, chatbot],
            )
        with gr.Tab(label="Title Generator"):
            with gr.Row():
                with gr.Column(scale=2):
                    example_video_desc = textwrap.dedent(
                        """
                    - spring is starting
                    - cooking classes, including sushi making experience in Ginza, and panda charabento making class
                    - trying seasonal drinks from konbinis and cafes
                    - getting kotatsu mat finally
                    - going to Ginza, going to famous bar, staying in nice hotel
                    - cooking simple evening dinner
                    """
                    )
                    video_description = gr.Textbox(
                        placeholder="Please describe current video here.",
                        label="Video Description",
                        value=example_video_desc,
                        lines=20,
                    )

                with gr.Column(scale=3):
                    chatbot = gr.Chatbot(show_copy_button=True)
                    input = gr.Textbox(
                        placeholder="Prompt the LLM.",
                        value="Please write 10 potential video titles",
                    )
                    get_response_btn = gr.Button(value="Get Response")

            get_response_btn.click(
                generate_titles,
                [input, chatbot, video_description],
                [input, chatbot],
            )

    demo.launch()


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
