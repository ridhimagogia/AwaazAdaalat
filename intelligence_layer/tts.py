import os
import uuid
from typing import Optional
from gtts import gTTS
try:
    from . import config
except ImportError:
    import config

_LANG_MAP = {
    "hi": "hi",   # Hindi
    "pa": "pa",   # Punjabi
    "ta": "ta",   # Tamil
    "te": "te",   # Telugu
    "bn": "bn",   # Bengali
    "mr": "mr",   # Marathi
    "en": "en",
}


def speak(text: str, language: Optional[str] = None, filename: Optional[str] = None) -> str:
  
    language = language or config.DEFAULT_LANGUAGE
    gtts_lang = _LANG_MAP.get(language, "en")

    os.makedirs(config.TTS_OUTPUT_DIR, exist_ok=True)
    filename = filename or f"explanation_{uuid.uuid4().hex[:8]}.mp3"
    out_path = os.path.join(config.TTS_OUTPUT_DIR, filename)

    try:
        tts = gTTS(text=text, lang=gtts_lang, slow=False)
        tts.save(out_path)
        return out_path
    except Exception as e:
        print(f"[tts] gTTS failed ({e}). Returning None — frontend should "
              f"show text-only fallback.")
        return None


if __name__ == "__main__":
    path = speak(
        "आपका केस नंबर CR-2026-0417 है। अगली सुनवाई की तारीख 12 अक्टूबर 2026 है।",
        language="hi",
    )
    print(f"Saved audio to: {path}")