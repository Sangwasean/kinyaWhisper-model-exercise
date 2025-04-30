from TTS.api import TTS
import torch


def speak_answer(answer: str, output_file: str = "answer.wav"):
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False)

    try:
        tts.tts_to_file(
            text=answer,
            file_path=output_file,
            speaker_wav="sample_speaker.wav"
        )
    except Exception as e:
        print(f"TTS Error: {str(e)}")
        return False
    return True


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
    print("Answer spoken successfully! Play answer.wav")
else:
    print("TTS failed")