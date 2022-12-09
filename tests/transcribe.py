import whisper

audio_path = 'src\\resources\\JavaScript in 100 Seconds.mp3'

model = whisper.load_model('small')
result = model.transcribe(audio_path, fp16 = False, language = 'es')
print(result['text'])


''' Atempt to write the results on a file '''
### file = open('tests\\test_output.txt', 'w', encoding='utf-8')
### file.write(result['text'])
### file.close()