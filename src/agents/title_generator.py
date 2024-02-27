import textwrap

from openai import OpenAI

from core.background_info import _DEFAULT_SYSTEM_PROMPT
from core.chat_helpers import create_messages

_SYSTEM_PROMPT_SUFFIX = textwrap.dedent(
    """
    We are trying to generate potential titles for our YouTube videos.

    Here are some examples of previous YouTube video titles we made that performed well:
    - "we took a little break from Tokyo | our weekend trip to Kusatsu Onsen & Karuizawa | life in Japan"
    - "a cozy week in our life in Tokyo | groceries & cooking, shopping & cafés | living in Japan vlog"
    - "what our first Tokyo Christmas was like | new apartment additions, local tradition, Japan life vlog"
    Please take note of the general vibe, the persona, and even the lack of capital letters in these example titles.

    Here is what the current YouTube video is about: 
    `{video_description}`

    Respond only with suggested titles. Do not add any explanations or pleasantries.
    """
)


def create_title_generator_system_prompt(video_description: str):
    system_prompt_suffix = _SYSTEM_PROMPT_SUFFIX.format(
        video_description=video_description
    )
    return _DEFAULT_SYSTEM_PROMPT + system_prompt_suffix


def generate_titles(
    user_input: str,
    chat_history: list[tuple[str, str]],
    video_description: str,
):
    client = OpenAI()

    system_prompt = create_title_generator_system_prompt(video_description)
    print(system_prompt)

    messages = create_messages(user_input, chat_history, system_prompt)

    stream = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        stream=False,
    )
    llm_response = stream.choices[0].message.content
    chat_history.append((user_input, llm_response))

    return "Try again.", chat_history
