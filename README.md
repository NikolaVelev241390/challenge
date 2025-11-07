# Wordle-like Challenge (challenge)

Small Python project that implements a word-guessing / text-game experience and includes an integration point to an LLM (via an OpenAI-compatible client routed to Hugging Face).

This README was created from the repository contents and shows exactly where and how the LLM model is used.

## Repo structure (important files)

- `game.py` — main game implementation (word game logic).
- `huggingface.py` — LLM integration (the code that calls the model).
- `wordle_words.json` — word list used by the game.
- `README.md` — this file.
- `.gitignore` — files ignored by git.

## Quick start

1. Clone the repository:
   ```bash
   git clone https://github.com/NikolaVelev241390/challenge.git
   cd challenge
   ```

2. Install dependencies (example; adjust to your environment):
   ```bash
   pip install openai
   ```
   Note: The code uses an OpenAI-compatible client object that targets the Hugging Face router. Make sure you have the appropriate client library installed (the repository uses `from openai import OpenAI`).

3. Provide an API key:
   - The repository contains a placeholder API key in `huggingface.py` (see the file and update the value or change the code to read from an environment variable).
   - Replace `"PUT YOUR KEY HERE"` with a valid key (or modify `huggingface.py` to read from `os.environ`).

4. Run the game:
   ```bash
   python game.py
   ```
   (If `game.py` calls the LLM integration, it will use the helper in `huggingface.py`.)

## LLM integration — exact location and code

The LLM is used only in `huggingface.py`. Exact file and lines (as present in the repository):
