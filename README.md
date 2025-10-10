# HamAI
The HamAI framework enables AI agents to use the radio spectrum for voice communication.

> [!CAUTION]
> Transmitting on radio frequencies without an appropriate license is restricted. Since most countries do not issue radio licenses to AI radio operators, limit your AI radio bots to license-free bands (e.g., CB, PMR, LPD, FRS). Check your country's regulations regarding the use of radio spectrum for AI agents.
<img width="1332" height="525" alt="hamai-framework-pipeline" src="hamai-framework-pipeline.png" />

The **Pipeline** is the main concept of the framework. Audio signals from the radio's EXT audio port enter the pipeline. The audio is transcribed to a text message and then fed to LLM GPT. LLM provides an answer, which is converted back to audio and transferred to radio for transmission on the air.

The Pipeline consists of the following steps:

| # | Step | Description | Technology | Script |
|----------|----------|----------|----------|----------|
| 1 | RX (Receive) | At this stage, the SoX tool with a silence filter is used to record audio from a radio receiver. When FM modulation is used, the squelch should be set so that it only lets signal through not the noise. | SoX | rx.sh |
| 2 | STT (Speach-to-text) | At this stage, OpenAI Whisper LLM is used to transcribe captured audio. | Whisper AI | stt.sh |
| 3 | GPT (Chat inference) | A text message is fed to the GPT of your choice as a prompt to LLM. Ollama’s REST API is used to communicate with LLM. | LLM GPT via Ollama | gpt.sh |
| 4 | TTS (Text-to-speech) | GPT’s answer is converted from text to audio. | Piper, Silero | tts.sh |
| 5 | TX (Transmission) | At this step, SoX is used to play audio and Arduino to switch PTT on the radio to trigger transmission. | Sox, Arduino | tx.sh |

**Hardware requirements**
To run the project, you will need:
- Radio with EXT port for connecting external speaker and ability to inject audio through the mic wiring.
- Arduino board and a relay module for activating the radio's PTT button.
- The project implies running LLMs locally at your PC. Therefore, to achieve near-real-time performance when interacting with AI radio operators, it is highly recommended to use graphics cards with CUDA support. At a minimum, the STT and GPT stages should be executed on the GPU.
