# 🛠️ Jarvis – Python Virtual Assistant

**Jarvis** is a voice‑activated desktop assistant built in Python. It listens to your commands, responds using speech, and can perform a variety of tasks—making it a fun and practical AI helper.

---

## 🔍 Features

- 🎙️ **Speech Recognition**: Uses `speech_recognition` to interpret your voice.
- 🗣️ **Text-to-Speech**: Leveraging `gTTS` (Google Text-to-Speech) to reply audibly.
- ⏰ **Time & Date**: Announces current time on request.
- 🌐 **Web Actions**: Opens web pages (maps, YouTube, Wikipedia, etc.).
- 📁 **File & System Tasks**: Take screenshots, open apps, lock screen.
- 📧 **Email Handling**: (Optional) Check unread Gmail—can be extended.
- 🌦️ **Weather Info**: Announce current weather via OpenWeatherMap API.
- 🤖 **Extras**: Tell jokes, play music, read PDFs, handle Git commands, and more.

---

## 📦 Requirements

```bash
pip install SpeechRecognition gTTS PyAudio requests
sudo apt-get install mpg321   # or mpg123 for playing audio
