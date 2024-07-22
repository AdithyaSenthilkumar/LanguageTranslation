from django.shortcuts import render
from googletrans import Translator
from gtts import gTTS
from .forms import TranslationForm
import speech_recognition as sr
import os

def translate_text(request):
    translator = Translator()
    translated_text = ""
    audio_file_path = 'translated.mp3'  # This will be a relative path, use MEDIA_ROOT in production
    
    if request.method == 'POST':
        form = TranslationForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data['text']
            audio = request.FILES.get('audio')
            target_language = form.cleaned_data['target_language']

            # Handle audio input
            if audio:
                recognizer = sr.Recognizer()
                try:
                    with sr.AudioFile(audio) as source:
                        audio_data = recognizer.record(source)
                        text = recognizer.recognize_google(audio_data)
                except sr.UnknownValueError:
                    translated_text = "Google Speech Recognition could not understand the audio"
                except sr.RequestError:
                    translated_text = "Could not request results from Google Speech Recognition service"

            # Translate text
            if text:
                try:
                    translated = translator.translate(text, dest=target_language)
                    translated_text = translated.text
                    tts = gTTS(translated_text, lang=target_language)
                    tts.save(audio_file_path)
                except Exception as e:
                    translated_text = f"Error translating text: {e}"

    else:
        form = TranslationForm()

    # Ensure file exists before rendering
    audio_file_url = None
    if os.path.exists(audio_file_path):
        audio_file_url = os.path.join('media', audio_file_path)

    return render(request, 'translate/translate.html', {
        'form': form,
        'translated_text': translated_text,
        'audio_file_url': audio_file_url
    })
