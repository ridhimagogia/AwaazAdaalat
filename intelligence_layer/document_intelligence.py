import re
import requests
try:
    from . import config
except ImportError:
    import config


def _mock_extract(raw_text: str) -> dict:

    case_number_match = re.search(r"(Case No\.?|CR No\.?|FIR No\.?)\s*[:\-]?\s*([A-Za-z0-9/\-]+)", raw_text, re.I)
    date_match = re.search(r"(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4})", raw_text)
    # Capture up to 2 words BEFORE "Court" (e.g. "Punjab and Haryana High Court")
    # and stop immediately — don't run on until the next comma/period, since
    # OCR text has no real line breaks and can run for a long way.
    court_match = re.search(
        r"(?:[A-Za-z]+\s+){0,2}(District|Sessions|High|Magistrate)\s+Court",
        raw_text,
        re.I,
    )

    return {
        "case_number": case_number_match.group(2) if case_number_match else "CR-2026-0417",
        "court_name": court_match.group(0) if court_match else "District Court, Sample Nagar",
        "allegation": "Alleged offence under Section 379 IPC (theft) — pending framing of charges",
        "hearing_date": date_match.group(1) if date_match else "12/10/2026",
        "accused_status": "Undertrial — bail application not yet filed",
        "source": "mock",
    }


def extract_case_facts(raw_text: str) -> dict:
    
    if config.MOCK_MODE:
        return _mock_extract(raw_text)

    try:
        response = requests.post(
            config.DOC_INTELLIGENCE_ENDPOINT,
            headers={"Authorization": f"Bearer {config.INSIGHTS_API_KEY}"},
            json={"text": raw_text},
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
        return {
            "case_number": data.get("case_number", "Not found"),
            "court_name": data.get("court_name", "Not found"),
            "allegation": data.get("allegation", "Not found"),
            "hearing_date": data.get("hearing_date", "Not found"),
            "accused_status": data.get("accused_status", "Unknown"),
            "source": "insights_api",
        }
    except requests.RequestException as e:
        # Fail safe to mock rather than killing the whole demo pipeline
        print(f"[document_intelligence] API call failed ({e}), falling back to mock.")
        return _mock_extract(raw_text)


if __name__ == "__main__":
    sample = """
    IN THE DISTRICT COURT, SAMPLE NAGAR
    Case No.: CR-2026-0417
    The accused is directed to appear on 12/10/2026 in connection with
    an offence under Section 379 IPC.
    """
    import json
    print(json.dumps(extract_case_facts(sample), indent=2))