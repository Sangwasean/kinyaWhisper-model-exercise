from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio
from torchaudio.transforms import Resample
import warnings

# Suppress specific warnings
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

# Load model and processor
model = WhisperForConditionalGeneration.from_pretrained("benax-rw/KinyaWhisper")
processor = WhisperProcessor.from_pretrained("benax-rw/KinyaWhisper")

# Load audio and convert to mono, resample to 16kHz
waveform, sample_rate = torchaudio.load("audios/ukorahe.wav")

# Convert stereo to mono if needed
if waveform.shape[0] > 1:
    waveform = waveform.mean(dim=0, keepdim=True)

# Resample if necessary
if sample_rate != 16000:
    resampler = Resample(sample_rate, 16000)
    waveform = resampler(waveform)

# Process audio input
inputs = processor(
    waveform.squeeze().numpy(),
    sampling_rate=16000,
    return_tensors="pt"
)

# Explicitly define generation config
generation_config = model.generation_config
generation_config.update(
    suppress_tokens=[],
    begin_suppress_tokens=[],
    forced_decoder_ids=None
)

predicted_ids = model.generate(
    inputs["input_features"],
    generation_config=generation_config,
    attention_mask=inputs.get("attention_mask", None)
)

transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
with open("transcription_data.txt", "w", encoding="utf-8") as file:
    file.write(transcription)

print("Transcription saved successfully to transcription_data.txt")