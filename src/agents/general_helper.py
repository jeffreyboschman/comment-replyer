from openai import OpenAI

from core.chat_helpers import create_messages


def create_general_system_prompt(
    default_system_prompt: str, default_system_prompt_suffix: str
):
    return default_system_prompt + default_system_prompt_suffix


def get_general_help(
    user_input: str,
    chat_history: list[tuple[str, str]],
    default_system_prompt: str,
    default_system_prompt_suffix: str,
):
    client = OpenAI()
    system_prompt = create_general_system_prompt(
        default_system_prompt, default_system_prompt_suffix
    )
    print(system_prompt)
    messages = create_messages(user_input, chat_history, system_prompt)

    stream = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=messages,
        stream=False,
    )
    llm_response = stream.choices[0].message.content
    chat_history.append((user_input, llm_response))

    return "", chat_history
