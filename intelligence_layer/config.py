import os

# --- iNSIGHTS credentials ---
INSIGHTS_API_KEY = os.environ.get("INSIGHTS_API_KEY", "")
INSIGHTS_BASE_URL = os.environ.get("INSIGHTS_BASE_URL", "https://insights-ai.info/api/v1")

DOC_INTELLIGENCE_ENDPOINT = f"{INSIGHTS_BASE_URL}/document-intelligence/extract"
MULTILINGUAL_ENDPOINT = f"{INSIGHTS_BASE_URL}/multilingual/generate"
SMART_ALERTS_ENDPOINT = f"{INSIGHTS_BASE_URL}/alerts/schedule"

MOCK_MODE = os.environ.get("INSIGHTS_MOCK_MODE", "true").lower() == "true"


DEFAULT_LANGUAGE = os.environ.get("DEFAULT_LANGUAGE", "hi")  # hi = Hindi

TTS_OUTPUT_DIR = os.environ.get("TTS_OUTPUT_DIR", "./tts_output")
