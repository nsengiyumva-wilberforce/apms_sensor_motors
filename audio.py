import RPi.GPIO as GPIO
import time
import pyaudio
import wave

# Set the GPIO pin numbers
REC_PIN = 19
PLAYE_PIN = 26

# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(REC_PIN, GPIO.OUT)
GPIO.setup(PLAYE_PIN, GPIO.OUT)

# Set REC pin to low, then high to start recording
GPIO.output(REC_PIN, GPIO.LOW)
time.sleep(0.5)
GPIO.output(REC_PIN, GPIO.HIGH)
time.sleep(5)  # Adjust the recording time as needed

# Stop recording by setting REC pin to low
GPIO.output(REC_PIN, GPIO.LOW)

# Define audio parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "recorded_audio.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the audio stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

# Start recording
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Stop recording
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recording to a file
wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b''.join(frames))
wave_file.close()

# Play the recorded audio
GPIO.output(PLAYE_PIN, GPIO.HIGH)
time.sleep(5)  # Adjust the playback time as needed
GPIO.output(PLAYE_PIN, GPIO.LOW)

# Clean up the GPIO settings
GPIO.cleanup()
