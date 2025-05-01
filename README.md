 Kinyarwanda Voice Assistant (using KinyaWhisper) 🤖️🎙️
Murakaza neza! Welcome to the Mini Kinyarwanda Voice Assistant project. This application demonstrates a simple voice interaction system for the Kinyarwanda language, simulating how a robot might hear, understand, and respond.

This project fulfills the assignment requirements by:

👂 Hearing: Using the benax-rw/KinyaWhisper model for Kinyarwanda Speech-to-Text (ASR).
🧠 Understanding: Matching the transcribed text to predefined questions using basic dictionary lookup (NLP).
🗣️ Speaking: Generating spoken Kinyarwanda answers using Google Text-to-Speech (TTS).
🎯 Project Goal
To build a functional prototype showcasing core voice AI components (ASR, NLP, TTS) for Kinyarwanda, suitable for demonstrating basic voice interaction in applications like robotics.

✨ How It Works: Code Breakdown

Initialization & Model Loading:

Imports necessary libraries (gradio, gtts, torch, torchaudio, transformers).
Defines constants like the Hugging Face MODEL_ID (benax-rw/KinyaWhisper).
Loads the WhisperProcessor and WhisperForConditionalGeneration model from Hugging Face, automatically downloading them if needed. It detects if a GPU (cuda) is available for faster processing.
# Loads processor and model
processor = WhisperProcessor.from_pretrained(MODEL_ID)
model = WhisperForConditionalGeneration.from_pretrained(MODEL_ID).to(device)
model.eval() # Sets model to evaluation mode
👂 Speech Recognition (ASR - transcribe_kinyarwanda function):

Takes the audio file path as input.
Loads the audio using torchaudio.load().
Converts stereo audio to mono.
Resamples the audio to the required TARGET_ASR_SAMPLE_RATE (16000 Hz) if necessary.
Uses the processor to prepare the audio features for the model.
Feeds the features into the model.generate() method to get predicted token IDs.
Decodes the token IDs back into Kinyarwanda text using processor.batch_decode().
# Inside transcribe_kinyarwanda:
waveform, sample_rate = torchaudio.load(audio_filepath)
# ... (resampling/mono conversion) ...
inputs = processor(waveform.squeeze().numpy(), ...)
input_features = inputs.input_features.to(device)
predicted_ids = model.generate(input_features, ...)
transcription = processor.batch_decode(predicted_ids, ...)[0]
🧠 Natural Language Processing (NLP - find_answer function):

Takes the transcribed text from the ASR step.
Normalizes the text (lowercase, remove trailing punctuation, strip whitespace).
Looks for an exact match of the normalized text in the keys of the predefined qa_pairs dictionary.
# Inside find_answer:
normalized_question = question_text.lower().strip().rstrip('?.!')
answer = qa_pairs.get(normalized_question) # Efficient dictionary lookup
Returns the corresponding answer if found, otherwise returns a default "I don't understand" message.
🗣️ Text-to-Speech (TTS - speak_kinyarwanda function):

Takes the answer text from the NLP step.
Uses the gTTS library to convert the text into speech (lang='rw').
Saves the generated speech as a temporary .mp3 file.
Returns the path to the temporary audio file.
Includes error handling, especially for potential gTTS language support issues.
# Inside speak_kinyarwanda:
tts = gTTS(text=text_to_speak, lang='rw', slow=False)
# ... (create temporary file) ...
tts.save(tts_filepath)
🌐 Web Interface (Gradio - iface object):

Creates an interactive UI using gradio.Interface.
Defines input components (gr.Audio for microphone/upload).
Defines output components (gr.Textbox for transcription/answer, gr.Audio for spoken response).
Connects the UI elements to the main voice_assistant_pipeline function.
Includes a title, description, examples (using your audio_samples), and a theme.
Adds a crucial note about potential gTTS limitations for Kinyarwanda TTS output.
🧹 Cleanup (cleanup_temp_files function):

A helper function to remove temporary TTS audio files created during previous runs, keeping the temp directory clean. Called at the start of the main pipeline.
🚀 Setup and Installation
Follow these steps to get the assistant running:

Clone Your Repository:

# Clone your specific repository
git clone [https://github.com/Sangwasean/kinyaWhisper-model-exercise.git]
cd Kinyarwanda-Voice-Assistant
🛠️ Install System Tools:


▶️ How to Run
🎙️ Record Your Audio: Ensure the audio_samples/ folder contains at least 5 audio files (.wav or .mp3) speaking the exact Kinyarwanda questions listed as keys in the qa_pairs dictionary in src/app.py. (Your repo already has these! 👍)
Activate Environment: If not already active:
source venv/bin/activate # Linux/macOS or venv\Scripts\activate for Windows

Model Link: https://huggingface.co/benax-rw/KinyaWhisper
