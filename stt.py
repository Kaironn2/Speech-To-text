import speech_recognition as sr
from pydub import AudioSegment
import openai

openai.api_key = "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"

def convert_mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")

def transcribe_audio(wav_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source) 
        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            return text, True
        except sr.UnknownValueError:
            return "UnknowValueError: NÃO DEU PRA ENTENDER A DESGRAÇA DO AÚDIO", False
        except sr.RequestError as e:
            return f"Deu merda: {e}", False

def obter_opiniao_ia(texto):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um amigo meu e vai me dar uma opinião."},
            {"role": "user", "content": f"O que você acha do seguinte texto transcrito?\n\n'{texto}'"}
        ]
    )
    return response['choices'][0]['message']['content']

file_name = "audio_de_braia_amostradinho"
mp3_folder_path = f"C:\\Users\\jonat\\Desktop\\Speech To Text\\audios\\mp3\\{file_name}.mp3"
wav_folder_path = f"C:\\Users\\jonat\\Desktop\\Speech To Text\\audios\\wav\\{file_name}.wav"

convert_mp3_to_wav(mp3_folder_path, wav_folder_path)

text, alt_key = transcribe_audio(wav_folder_path)

if alt_key:
    print("CHUPA MINHA PICADURA BRAIA E MPEG -> ", text)
    opiniao = obter_opiniao_ia(text)
    print("Chatgpt acha:", opiniao)
else:
    print(text)
