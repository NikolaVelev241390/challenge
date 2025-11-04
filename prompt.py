from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Choose a small chat/instruct model
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

# Load tokenizer and model (downloaded once then cached)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)


def generate_text(prompt: str, max_tokens: int = 120):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs, max_new_tokens=max_tokens, do_sample=True, temperature=0.1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == "__main__":
    print(generate_text("Once upon a time in a land far, far away,"))
