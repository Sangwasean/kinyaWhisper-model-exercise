from gtts import gTTS, tts
import os

def speak_answer(answer: str, output_file: str = "answer.mp3"):
    try:

        tts = gTTS(text=answer, lang='rw', slow=False)
        tts.save(output_file)
        return True
    except Exception as e:
        print(f"TTS Error: {str(e)}")
        return False

qa = {
    "Rwanda Coding Academy iherereye he?": "Iherereye mu Karere ka Nyabihu, mu Ntara y’Iburengerazuba.",
    "Umurwa mukuru w’u Rwanda ni uwuhe?": "Ni Kigali.",
    "Paul kagame ninde?": "Ni perezida w'urwanda.",
    "Imbwa niki ?": "Ni inyamaswa.",
    "Ngewe banyita nde?": "Bakwita Sean.",
}

transcription = "Rwanda Coding Academy iherereye he?"
answer = qa.get(transcription, "Ntago mbyumva neza.")

if speak_answer(answer):
    print(f"Answer saved to answer.mp3 - Play it manually")
    tts.save("answer.mp3")
else:
    print("Failed transcription")