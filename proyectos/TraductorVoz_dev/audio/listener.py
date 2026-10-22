import sounddevice as sd
import numpy as np
from queue import Queue


class Listener:

    def __init__(
        self,
        samplerate=16000,
        channels=1,
        blocksize=1600,
        threshold=0.02,
        silence_blocks=10,
    ):

        self.samplerate = samplerate
        self.channels = channels
        self.blocksize = blocksize

        self.threshold = threshold
        self.silence_blocks = silence_blocks

        self.queue = Queue()

    def callback(self, indata, frames, time, status):

        if status:
            print(status)

        self.queue.put(indata.copy())

    def listen(self):

        print("\n🎤 Esperando voz...\n")

        frames = []

        speaking = False

        silence = 0

        with sd.InputStream(
            samplerate=self.samplerate,
            channels=self.channels,
            blocksize=self.blocksize,
            callback=self.callback,
            dtype="float32",
        ):

            while True:

                audio = self.queue.get()

                volume = np.abs(audio).mean()

                if volume > self.threshold:

                    if not speaking:

                        print("🟢 Voz detectada")

                        speaking = True

                    silence = 0

                    frames.append(audio)

                elif speaking:

                    frames.append(audio)

                    silence += 1

                    if silence >= self.silence_blocks:

                        print("🔴 Fin de la frase")

                        break

        if len(frames) == 0:
            return None

        return np.concatenate(frames, axis=0)