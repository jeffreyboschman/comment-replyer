from openai import OpenAI


def ask_with_context(text, system_prompt):
    client = OpenAI()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text},
    ]
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        stream=False,
    )
    return stream.choices[0].message.content
