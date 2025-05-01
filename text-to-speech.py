import re
import os
import time
from fuzzywuzzy import fuzz
from gtts import gTTS

os.makedirs("audio_outputs", exist_ok=True)
QA_PAIRS = {
    "Rwanda Coding Academy iherereye he?": "Iherereye mu Karere ka Nyabihu, mu Ntara y’Iburengerazuba.",
    "Umurwa mukuru w’u Rwanda ni uwuhe?": "Ni Kigali.",
    "Paul kagame ninde?": "Ni perezida w'urwanda.",
    "Imbwa niki?": "Ni inyamaswa.",
    "Ngewe banyita nde?": "Bakwita Sean."
}
DEFAULT_RESPONSE = "Ntago mbyumva neza."


def normalize(text):
    return re.sub(r'[^\w\s]', '', text.lower()).strip()


def find_best_match(question):
    if not question:
        return DEFAULT_RESPONSE, None

    clean_question = normalize(question)
    best_match = None
    highest_score = 0

    for possible_question in QA_PAIRS:
        score = fuzz.ratio(normalize(possible_question), clean_question)
        if score > highest_score and score > 60:  # Lowered threshold for better matching
            highest_score = score
            best_match = possible_question

    return (QA_PAIRS[best_match], best_match) if best_match else (DEFAULT_RESPONSE, None)


def generate_response(answer_text):
    """Generate and save TTS response with fallback handling"""
    try:
        # First attempt Kinyarwanda (even if unsupported)
        tts = gTTS(text=answer_text, lang='rw', slow=False)
    except ValueError:
        # Fallback to English if Kinyarwanda fails
        tts = gTTS(text=answer_text, lang='en')

    timestamp = str(int(time.time()))
    output_path = f"audio_outputs/response_{timestamp}.mp3"
    tts.save(output_path)
    return output_path


# Usage example (assuming transcribed_text comes from your ASR system)
if __name__ == "__main__":
    # Simulated input from your transcription system
    transcribed_text = "Rwanda Coding Academy iherereye he?"

    # Find matching answer
    answer, matched_question = find_best_match(transcribed_text)

    # Generate audio response
    audio_path = generate_response(answer)

    print(f"Question: {transcribed_text}")
    print(f"Matched Question: {matched_question}")
    print(f"Answer: {answer}")
    print(f"Audio response saved to: {audio_path}")