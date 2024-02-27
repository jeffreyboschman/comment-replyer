import textwrap

from openai import OpenAI

from core.background_info import _DEFAULT_SYSTEM_PROMPT
from core.chat_helpers import create_messages

_SYSTEM_PROMPT_SUFFIX = textwrap.dedent(
    """
    We are trying to respond to a comment on our YouTube video.
    {additional_info_str}
    Here is the comment we are replying to: 
    `{comment}`

    Respond only with a reasonable comment reply. Do not add any explanations or pleasantries.
    """
)

_ADDITIONAL_INFO = textwrap.dedent(
    """
    Here is some additional information that you can use to formulate your comment response:
    `{additional_info}`
    """
)


def create_comment_replyer_system_prompt(comment: str, additional_info: str):
    additional_info_str = (
        _ADDITIONAL_INFO.format(additional_info=additional_info)
        if additional_info
        else ""
    )
    system_prompt_suffix = _SYSTEM_PROMPT_SUFFIX.format(
        comment=comment, additional_info_str=additional_info_str
    )
    return _DEFAULT_SYSTEM_PROMPT + system_prompt_suffix


def generate_comment_response(
    user_input: str,
    chat_history: list[tuple[str, str]],
    comment: str,
    additional_info: str,
):
    client = OpenAI()

    system_prompt = create_comment_replyer_system_prompt(comment, additional_info)
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
