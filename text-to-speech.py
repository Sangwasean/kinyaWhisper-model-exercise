import os
from gtts import gTTS

QA_PAIRS = {
    "Rwanda Coding Academy iherereye he?": "Iherereye mu Karere ka Nyabihu, mu Ntara y’Iburengerazuba.",
    "Umurwa mukuru w’u Rwanda ni uwuhe?": "Ni Kigali.",
    "Paul kagame ninde?": "Ni perezida w'urwanda.",
    "Imbwa niki?": "Ni inyamaswa.",
    "Ngewe banyita nde?": "Bakwita Sean."
}

OUTPUT_DIR = "audio_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_all_answer_audios():
    results = []

    for idx, (question, answer) in enumerate(QA_PAIRS.items(), 1):
        filename = f"answer_{idx}.mp3"
        output_path = os.path.join(OUTPUT_DIR, filename)
        success = False

        try:
            tts = gTTS(text=answer, lang='rw', slow=False)
            tts.save(output_path)
            success = True
        except Exception as e:
            try:
                tts = gTTS(text=answer, lang='sw', slow=False)
                tts.save(output_path)
                success = True
            except:
                try:
                    tts = gTTS(text=answer, lang='sw', slow=False)
                    tts.save(output_path)
                    success = True
                except Exception as final_error:
                    error_msg = str(final_error)

        results.append({
            "question": question,
            "answer": answer,
            "filename": filename,
            "success": success,
            "error": error_msg if not success else None
        })

    return results

generation_report = generate_all_answer_audios()

print(f"{'Status':<8} | {'Question':<45} | {'Filename':<20}")
print("-" * 80)
for item in generation_report:
    status = "✅" if item['success'] else "❌"
    print(f"{status:<8} | {item['question']:<45} | {item['filename']:<20}")

print(f"\nOutput directory: {os.path.abspath(OUTPUT_DIR)}")