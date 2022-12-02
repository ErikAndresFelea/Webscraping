import whisper

model = whisper.load_model('base')
result = model.transcribe('src\\courses\\prueba_transcribe.mp3')
print(result["text"])

### file = open('tests\\test_output.txt', 'w', encoding='utf-8')
### file.write(result['text'])
### file.close()