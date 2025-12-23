🇮🇳 YojanaAI – Hindi Voice-Based Scheme Eligibility Assistant

YojanaAI is a voice-first Hindi AI assistant that determines eligibility for Indian government schemes using:

1. Speech-to-Text (Vosk Hindi Model)

2. Text-to-Speech (gTTS)

3. Agentic workflow (Planner → Executor → Evaluator)

4. Conversation memory

5. Simple GUI for interaction


The assistant collects age, income, caste, and then checks which schemes you qualify for.

 Features

Full Hindi voice pipeline (STT → AI → TTS)

Automatic eligibility checking

Multi-turn conversation with memory

Handles missing information & errors

GUI with Start/Stop recording buttons

*** Vosk Model Not Included (Important)***

The Vosk Hindi model is larger than GitHub’s 25 MB limit,
so it cannot be uploaded to this repository.

You must download it manually:

Download Hindi Models:

Small (65 MB):
https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip

Large (180 MB):
https://alphacephei.com/vosk/models/vosk-model-hi-0.22.zip

After downloading:

Extract the ZIP

Rename folder to: vosk_hindi_model

Place it inside:

stt/vosk_hindi_model/

▶️ How to Run
Install dependencies:
pip install -r requirements.txt

Start the GUI:
python gui_agent.py


The assistant will:

Speak a welcome message

Ask your name → age → income → caste

Finally tell you eligible schemes

📂 Project Structure
agent/        → planner, executor, evaluator, memory
stt/          → vosk Hindi STT
tts/          → gTTS voice output
tools/        → eligibility engine + scheme retriever
gui_agent.py  → GUI interface
