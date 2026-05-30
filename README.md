# 👏 Clap to Open — Your Hands are the Remote

> Turn a simple clap into real actions on your computer.  
> Open apps, websites, or trigger automation — just by sound.

---

## 🚀 Demo Idea

👏 Clap → Opens YouTube / Chrome / Any App  
👏 Clap → Triggers automation instantly  
👏 Clap → Your computer listens and responds

---

## ⚡ Why this project?

Most automation tools need:
- clicks 🖱️  
- keyboard ⌨️  
- voice commands 🎤  

This project adds something simpler:

👉 **Just clap. That’s it.**

---

## 🎯 Features

- 👏 Real-time clap detection using microphone
- ⚡ Instant system trigger on sound spike
- 🌐 Open websites with a clap
- 🧠 Lightweight Python implementation
- 🔧 Easy to customize actions
- 📈 Expandable to AI assistant / voice control

---

## 🧠 How it works

1. Microphone listens continuously 🎤  
2. Audio amplitude is measured 📊  
3. Clap = sudden sound spike detected 👏  
4. Action is triggered instantly ⚡  

---

## 🛠️ Tech Stack

- Python 🐍  
- NumPy  
- SoundDevice / PyAudio  
- SciPy  
- OS automation  

---

## 📦 Installation

```bash
git clone https://github.com/mishikabagrecha/clap-to-open.git
cd clap-to-open

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows

pip install -r requirements.txt
