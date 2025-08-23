# 🗣️ Meghal's Voice Assistant

A simple **Python-based voice assistant** that can **open websites, play music, launch applications**, and **interact with the user using voice commands**.
It uses **speech recognition** and **text-to-speech** technologies to listen to your commands and respond back.


## 🚀 Features

* 🎙 **Voice Recognition** → Understands your voice commands using `speech_recognition`.
* 🗣 **Text-to-Speech** → Replies back using `pyttsx3`.
* 🌐 **Open Websites** → Instantly opens popular websites like YouTube, Google, Wikipedia, and ChatGPT.
* 🎵 **Play Music** → Plays your favorite songs from your local system.
* 📄 **Open Applications** → Can open Microsoft Word and Calculator.
* 🔄 **Easily Customizable** → Add more sites, music, or apps by editing the code.


## 🛠️ Technologies Used

* **Python 3**
* [speech\_recognition](https://pypi.org/project/SpeechRecognition/) → For converting speech to text
* [pyttsx3](https://pypi.org/project/pyttsx3/) → For text-to-speech
* `webbrowser` → To open websites
* `os` → To open files and apps


## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2️⃣ Install Required Libraries

```bash
pip install speechrecognition pyttsx3
```

> **Note:** Make sure you have **PyAudio** installed. If you face installation issues, try:

```bash
pip install pipwin
pipwin install pyaudio
```


## ▶️ How to Run

```bash
python voice_assistant.py
```

## 🎯 Usage

Once the program starts, it will greet you:

> "Hello, I am Meghal's Assistance"

Then, you can give commands like:

* **"Open YouTube"** → Opens YouTube in your browser.
* **"Open Google"** → Opens Google Search.
* **"Open Wikipedia"** → Opens Wikipedia.
* **"Play Music"** → Plays your selected song.
* **"Open Word"** → Launches Microsoft Word.
* **"Open Calculator"** → Opens the Windows Calculator.
* **"Open ChatGPT"** → Opens ChatGPT in your browser.


## 🛠️ Project Structure

```
📂 Meghal-Voice-Assistant
 ├── voice_assistant.py   # Main Python file
 ├── README.md            # Project documentation
 └── requirements.txt     # Dependencies (optional)
```

## 🔧 Customization

To add new websites:

```python
sites = [
    ["youtube", "https://www.youtube.com"],
    ["google", "https://www.google.com"],
    ["wikipedia", "https://www.wikipedia.com"],
    ["chatgpt", "https://chatgpt.com"]
]
```

Just add your site in the same format:

```python
["site-name", "site-link"]
```

## 🐞 Troubleshooting

* If you face a **PyAudio** error, install it using:

```bash
pipwin install pyaudio
```

* Make sure your **microphone** is enabled and working.
* If speech recognition fails, check your **internet connection** (Google API is used).

## 🤝 Contributing

Pull requests are welcome! If you have any ideas to improve the assistant, feel free to fork the repo and submit your changes.


## 👨‍💻 Author

**Meghal Ramteke**
🎓 3rd Year | Engineering Student
📧 Email: *meghalramteke@gmail.com*
🌐 GitHub: https://github.com/meghal14


