"""
import ollama

# mistral, llama2-uncensored
response = ollama.chat(model='mistral', messages=[
  {
    'role': 'user', # "system", "user" , "assistant"
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content']) 
"""



def mic_test_vosk():   
    from vosk import Model, KaldiRecognizer
    import pyaudio

    model = Model(lang="en-us")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(f"' {text[14:-3]} '")
            



if __name__ == "__main__":

    mic_test_vosk()
    
