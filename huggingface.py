import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="token",
)

def generate_text_game():
    """Generate text response using Hugging Face API through OpenAI interface."""
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct:novita",
        messages=[
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ],
    )
    return completion.choices[0].message


if __name__ == "__main__":
    # Test the function when running this file directly
    try:
        response = generate_text_game()
        print("Generated response:", response)
    except Exception as e:
        print(f"Error generating text: {e}")