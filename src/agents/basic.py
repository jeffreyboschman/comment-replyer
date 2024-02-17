from openai import OpenAI


def ask_with_context(text):
    client = OpenAI()
    _SYSTEM_PROMPT = """
    Please act as an expert in social media, marketing, and psychology 
    who is hired to be our social media content assistant.

    We are a Canadian couple on YouTube and Instagram who 
    mainly make posts about our life in Tokyo, Japan. 

    Our vibe is cozy, charming, polite, casual, light, bright,
    clean, relatable, humble, genuine, and Ghibli-esque.

    Please help us develop content by following the user instructions or answering questions.
    """
    messages = [{"role": "system", "content": _SYSTEM_PROMPT }, {"role": "user", "content": text}]
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        stream=False,
    )
    return stream.choices[0].message.content


