# DecodeLabs Project 1 — Custom AI Chatbot with Memory

A Python terminal chatbot using Google's `google-genai` SDK and manually managed in-memory conversation history.

## Features
- Gemini API integration via environment variable
- Structured user/model conversation messages
- Sliding-window FIFO pruning by complete turns
- Empty-input validation
- `/memory`, `/clear`, `/help`, and `exit` commands
- Unit tests that mock the API call (no API key required for tests)

## Windows setup (PowerShell)

1. Install Python 3.10+.
2. Open PowerShell in this project folder.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate again.

4. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Copy `.env.example` to `.env` and put your Gemini API key in `.env`:

   ```env
   GEMINI_API_KEY=your_actual_key
   GEMINI_MODEL=gemini-2.5-flash
   ```

6. Run:

   ```powershell
   python main.py
   ```

## Commands
- `/memory` — show retained messages
- `/clear` — clear current session memory
- `/help` — show commands
- `exit` — quit

## Run tests

```powershell
pytest -q
```

Tests do not make API requests. Chat history is stored in RAM and disappears when the program exits; database persistence and web UI are not included in this version.

## Security
Never commit `.env` or share your API key. Check current model availability and API quotas in your Google AI Studio account.
