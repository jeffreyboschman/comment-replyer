def create_flattened_chat_history_messages(
    chat_history: list[tuple[str, str]]
) -> list[dict[str, str]]:
    """
    Creates a flattened list of chat history messages from a given chat history.

    Args:
        chat_history (list[tuple[str,str]]): A list of tuples representing the chat history,
                            where each tuple contains the user's question and the assistant's response.

    Returns:
        list[dict[str,str]]: A flattened list of dictionaries representing individual chat messages.
              Each dictionary contains two key-value pairs: "role" representing the speaker's role ("user" or "assistant"),
              and "content" representing the message content.

    Example:
        >>> chat_history = [
                ("Hello!", "Hi there! How can I assist you?"),
                ("What's the weather like today?", "The weather is sunny with a high of 75°F."),
                ("Thank you!", "You're welcome! Is there anything else I can help with?")
            ]
        >>> create_flattened_chat_history_messages(chat_history)
        [{'role': 'user', 'content': 'Hello!'},
         {'role': 'assistant', 'content': 'Hi there! How can I assist you?'},
         {'role': 'user', 'content': "What's the weather like today?"},
         {'role': 'assistant', 'content': 'The weather is sunny with a high of 75°F.'},
         {'role': 'user', 'content': 'Thank you!'},
         {'role': 'assistant', 'content': "You're welcome! Is there anything else I can help with?"}]
    """
    chat_history_messages = [
        [
            {"role": "user", "content": user_question},
            {"role": "assistant", "content": llm_response},
        ]
        for user_question, llm_response in chat_history
    ]
    flattened_chat_history_messages = [
        message for sublist in chat_history_messages for message in sublist
    ]
    return flattened_chat_history_messages


def create_messages(
    user_input: str, chat_history: list[tuple[str, str]], system_prompt: str
) -> list[dict[str, str]]:
    """
    Creates a list of messages incorporating the user's input, chat history, and a system prompt.

    Args:
        user_input (str): The input provided by the user.
        chat_history (list[tuple[str,str]]): A list of tuples representing the chat history,
                            where each tuple contains the user's question and the assistant's response.
        system_prompt (str): The prompt presented by the system before the user input.

    Returns:
        list[dict[str,str]]: A list of dictionaries representing individual chat messages.
              Each dictionary contains two key-value pairs: "role" representing the speaker's role ("user", "assistant", or "system"),
              and "content" representing the message content.

    Example:
        >>> user_input = "What should I do next?"
        >>> chat_history = [
                ("Hello!", "Hi there! How can I assist you?"),
                ("What's the weather like today?", "The weather is sunny with a high of 75°F.")
            ]
        >>> system_prompt = "Please ask friendly."
        >>> create_messages(user_input, chat_history, system_prompt)
        [{'role': 'system', 'content': 'Please ask your question:'},
         {'role': 'user', 'content': 'Hello!'},
         {'role': 'assistant', 'content': 'Hi there! How can I assist you?'},
         {'role': 'user', 'content': "What's the weather like today?"},
         {'role': 'assistant', 'content': 'The weather is sunny with a high of 75°F.'}
         {'role': 'user', 'content': 'What should I do next?'},
        ]
    """
    system_prompt_message = [{"role": "system", "content": system_prompt}]
    chat_history_messages = create_flattened_chat_history_messages(chat_history)
    input_message = [{"role": "user", "content": user_input}]
    final_messages = system_prompt_message + chat_history_messages + input_message
    return final_messages
