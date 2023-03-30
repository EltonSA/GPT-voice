import speech_recognition as sr

# Cria um objeto de reconhecimento
r = sr.Recognizer()

# Usa o microfone como fonte de entrada de áudio
with sr.Microphone() as source:
    print("Fale alguma coisa:")
    # Aguarda o usuário falar algo e grava o áudio
    audio = r.listen(source)

# Reconhece a fala usando o Google Web Speech API
try:
    text = r.recognize_google(audio, language='pt-BR')
    print("Você disse: " + text)
except sr.UnknownValueError:
    print("Não entendi o que você disse")
except sr.RequestError as e:
    print("Não foi possível se conectar ao servidor do Google Speech Recognition; {0}".format(e))
