import json
from typing import Optional
try:
    from .document_intelligence import extract_case_facts
    from .multilingual import explain_case
    from .tts import speak
    from .alerts import schedule_reminder
    from . import config

except ImportError:
    from document_intelligence import extract_case_facts
    from multilingual import explain_case
    from tts import speak
    from alerts import schedule_reminder
    import config


def run_pipeline(raw_text: str, user_id: str, language: Optional[str] = None) -> dict:

    language = language or config.DEFAULT_LANGUAGE

    # 1. Extract structured facts from the raw document text
    case_facts = extract_case_facts(raw_text)

    # 2. Turn facts into a plain-language spoken explanation + checklist
    explanation_result = explain_case(case_facts, language=language)

    # 3. Speak the explanation aloud
    audio_path = speak(explanation_result["explanation"], language=language)

    # 4. Schedule a reminder before the next hearing
    reminder = schedule_reminder(case_facts["hearing_date"], user_id=user_id)

    return {
        "case_facts": case_facts,
        "explanation": explanation_result["explanation"],
        "checklist": explanation_result["checklist"],
        "language": language,
        "audio_path": audio_path,
        "reminder": reminder,
    }


if __name__ == "__main__":
    sample_ocr_text = """
    IN THE DISTRICT COURT, SAMPLE NAGAR
    Case No.: CR-2026-0417
    The accused is directed to appear on 12/10/2026 in connection with
    an offence under Section 379 IPC.
    """

    result = run_pipeline(sample_ocr_text, user_id="demo_user_1", language="hi")
    print(json.dumps(result, indent=2, ensure_ascii=False))