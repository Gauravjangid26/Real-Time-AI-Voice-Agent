
# Real-Time AI Voice Agent 🎙️🤖

This project is a **full-duplex AI-powered voice assistant** that can **listen, process, and respond in real-time**. It supports **interruptions**, **natural conversations**, and **multiple AI & speech processing integrations**.

---

## 🚀 Features

* **Full-Duplex Communication** – Talk and listen simultaneously.
* **Speech-to-Text (STT)** – Convert speech to text in real-time.
* **Text-to-Speech (TTS)** – Respond with natural AI-generated speech.
* **Interruption Handling** – User can interrupt the agent mid-response.
* **Noise Cancellation** – Clear audio input for better accuracy.
* **Customizable AI Brain** – Integrate OpenAI, Gemini, or other LLMs.

---

## 🛠️ Tech Stack

* **[LiveKit Agents](https://github.com/livekit/agents)** – For real-time audio streaming & agent orchestration.
* **STT** – Deepgram .
* **TTS** – Cartesia .
* **Noise Cancellation** – LiveKit Noise Cancellation Plugin.
* **LLM** –  Gemini, or your preferred AI model.

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/voice-agent.git
cd voice-agent
```

### 2️⃣ Install dependencies

```bash
pip install \
  "livekit-agents[deepgram,openai,cartesia,silero,turn-detector]~=1.0" \
  "livekit-plugins-noise-cancellation~=0.2" \
  "python-dotenv"
```

---

## ⚙️ Configuration

Create a **`.env`** file in the project root with your API keys:

```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
OPENAI_API_KEY=your_openai_api_key
GOOGLE_APPLICATION_CREDENTIALS=path/to/google-credentials.json
```

---

## ▶️ Running the Agent

Run the agent with:

```bash
python main.py
```

If you need to **download model/audio resources** before running:

```bash
python main.py download-files
```
  
---

## 📂 Project Structure

```
voice-agent/
│── agent.py               # Main agent script
│── requirements.txt       # Dependencies
│── .env                   # API keys & config
│── README.md              # Project documentation
```

---

## 🔮 Future Enhancements

* Web & mobile app integration.
* Multi-language support.
* Sentiment-aware responses.
* Browser extension.

---

## 📝 License

This project is licensed under the MIT License.

---

I can also make you a **nice badge-based README** with icons and a quick start section so it looks more professional like open-source projects on GitHub.
Do you want me to do that?
