from django.shortcuts import render
from googletrans import Translator
from gtts import gTTS
from .forms import TranslationForm
import speech_recognition as sr
from pydub import AudioSegment
import os
import subprocess

def translate_text(request):
    translator = Translator()
    translated_text = ""
    if request.method == 'POST':
        form = TranslationForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            audio = request.FILES.get('audio')
            target_language = form.cleaned_data['target_language']

            # Handle audio input
            if audio:
                recognizer = sr.Recognizer()
                with sr.AudioFile(audio) as source:
                    audio_data = recognizer.record(source)
                    text = recognizer.recognize_google(audio_data)

            # Translate text
            if text:
                translated = translator.translate(text, dest=target_language)
                translated_text = translated.text
                tts = gTTS(translated.text, lang=target_language)
                tts.save('translated.mp3')

                # Play the translated audio
                if os.path.exists('translated.mp3'):
                    try:
                        if os.name == 'nt':  # Windows
                            os.system('start translated.mp3')
                        else:  # Other OS
                            subprocess.call(['mpg123', 'translated.mp3'])
                    except Exception as e:
                        print(f"Error playing audio: {e}")

    else:
        form = TranslationForm()

    return render(request, 'translate/translate.html', {'form': form, 'translated_text': translated_text})

def detect_language(text):
    translator = Translator()
    return translator.detect(text).lang
