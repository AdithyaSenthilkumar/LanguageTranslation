# Language Translation Web Application

## Overview
This is a Django-based web application that allows users to translate text between languages and supports optional audio input for translation. The app utilizes Google Translate for text translation and Google Text-to-Speech for audio output. Users can input text or upload an audio file for speech-to-text processing.

## Features
- **Text Translation**: Translate text from one language to another.
- **Language Detection**: Automatically detect the source language of the input text.
- **Speech-to-Text**: Convert audio input to text for translation.
- **Text-to-Speech**: Generate audio for the translated text.

## Installation
  ### Prerequisites
  - Python 3.10 or higher
  - Django 4.2 or higher
  - Google Translate API
  - Google Text-to-Speech (gTTS)
  - SpeechRecognition
  - pydub

  ### Clone the Repository
  ```bash
  git clone https://github.com/AdithyaSenthilkumar/LanguageTranslation.git
  cd LanguageTranslation
