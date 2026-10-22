import sounddevice as sd
import soundfile as sf

def record_audio(filename="audio/temp/grabacion.wav", duration=10, samplerate=16000):
    print("🎤 Grabando durante 10 segundos...")
    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    sf.write(filename, recording, samplerate)

    print(f"✅ Audio guardado en: {filename}")

    return filename