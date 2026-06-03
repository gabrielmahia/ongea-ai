# 🎙️ Ongea AI — Swahili Voice AI

> *Ongea* (Swahili) = speak, talk, converse

Voice-first AI interface for Swahili speakers — speech-to-text, text-to-speech, and conversational AI for users who read slowly or not at all. Designed for low-literacy East African users who interact best by voice.

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

## Why Voice Matters

30% of Kenyan adults read below primary school level. But virtually all own a mobile phone and can speak and listen. Voice AI removes the literacy barrier — users speak their question in Swahili and hear the answer. No typing, no reading, no language barrier.

## Architecture

```
User speaks (Swahili) 
  → Whisper (speech-to-text) 
  → Gemini (reasoning in Swahili) 
  → TTS (text-to-speech, Swahili)
  → User hears answer
```

## Use Cases

- 🌾 Farmer asks: "Je, leo ni wakati mzuri wa kupanda mahindi?"
- 💊 Patient asks: "Dawa hii ninaitumia vipi?"
- 💰 Business owner: "Ninaweza kupata mkopo mdogo vipi?"
- 📋 Voter: "Namshinda nani mgombea katika kura yangu?"

## Quickstart

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Research Basis

OpenAI Whisper (Radford et al. 2022) has documented support for Swahili. The voice-first interface pattern is validated by USSD and SMS mHealth research in East Africa (PMC10562967).

---
*gabrielmahia.ai | Part of the Swahili AI Infrastructure Stack*
