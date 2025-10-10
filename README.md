# hamai
The HamAI framework enables AI agents to use the radio spectrum for voice communication.

> [!CAUTION]
> Transmitting on radio frequencies without an appropriate license is prohibited. Since most countries do not issue radio licenses to AI radio operators, limit your AI radio bots to license-free bands (e.g., CB, PMR, LPD, FRS). Check your country's regulations regarding the use of radio spectrum for AI agents.
<img width="1332" height="525" alt="hamai-framework-pipeline" src="https://github.com/user-attachments/assets/bc3df78e-acc3-4906-87f6-186bd9e0bb91" />

Pipeline is the main concept of the framework. Audio signals from the radio's EXT audio interface enter the pipeline. The audio is transcribed to a text message and then fed to LLM GPT. LLM provides an answer, which is converted back to audio and transferred to radio for transmission on the air.
Pipeline consists of the following steps:
