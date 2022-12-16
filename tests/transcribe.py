import whisper
import time

start = time.time()
audio_path = 'src\\resources\\JavaScript in 100 Seconds.mp3'

model = whisper.load_model('base')
result = model.transcribe(audio_path, fp16 = False, language = 'en')
print(result['text'])

first_mode = time.time() - start
'''
Not enough memory for cuda
start = time.time()

model = whisper.load_model('medium', device = 'cuda')
result = model.transcribe(audio_path, fp16 = False, language = 'en')
print(result['text'])

second_mode = time.time() - start

print(second_mode)
'''
print(first_mode)
### file = open('tests\\test_output.txt', 'w', encoding='utf-8')
### file.write(result['text'])
### file.close()