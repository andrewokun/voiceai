from ollama import chat, ResponseError

def send_prompt(prompt, model):
    try:
        response = chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.message.content

    except ResponseError as e:
        if e.status_code == 404:
            raise ValueError(
                f"Error Found: Please Find Model"
            ) from e
        raise
