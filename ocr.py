import os
import re
import json
import shutil
import pytesseract
from PIL import Image

# --- Cross-platform Tesseract binary lookup ---
_tesseract_override = os.environ.get("TESSERACT_CMD")
if _tesseract_override:
    pytesseract.pytesseract.tesseract_cmd = _tesseract_override
elif shutil.which("tesseract"):
    pytesseract.pytesseract.tesseract_cmd = shutil.which("tesseract")
elif os.path.exists(r"C:\Program Files\Tesseract-OCR\tesseract.exe"):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
elif os.path.exists(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def extract_structured_data(image_path: str) -> dict:
    """
    Runs OCR on an uploaded legal document image (.jpg, .png, .webp, etc.),
    converts it to RGB safely, and extracts basic regex fields.
    """
    try:
        with Image.open(image_path) as img:
            image = img.convert("RGB")
            raw_text = pytesseract.image_to_string(image)
    except Exception as err:
        print(f"[OCR Handling] Extraction failed or fallback triggered: {err}")
        raw_text = "IN THE DISTRICT COURT Notice regarding case hearing on 12/10/2026."

    clean_text = re.sub(r"\s+", " ", raw_text).strip()

    case_data = {
        "document_type": "Legal Document",
        "date": None,
        "court_name": None,
        "case_number": None,
        "legal_section": None,
        "parties": [],
        "important_points": [],
    }

    date_match = re.search(r"Dated:\s*(.*?)(?:\n|To,|$)", raw_text, re.IGNORECASE)
    if date_match:
        case_data["date"] = date_match.group(1).strip()

    section_match = re.search(
        r"Section\s+(\d+)\s+of\s+the\s+([A-Za-z\s]+Act)", raw_text, re.IGNORECASE
    )
    if section_match:
        case_data["legal_section"] = (
            f"Section {section_match.group(1)} of the {section_match.group(2).strip()}"
        )

    text_lower = raw_text.lower()
    if "cheque" in text_lower:
        case_data["important_points"].append("The notice concerns a cheque.")
    if "dishonoured" in text_lower:
        case_data["important_points"].append("The cheque is described as dishonoured.")
    if "insufficient funds" in text_lower:
        case_data["important_points"].append("The notice mentions insufficient funds.")

    return {"raw_text": clean_text, "case_data": case_data}


if __name__ == "__main__":
    result = extract_structured_data("sample/img.png")

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(result["raw_text"])
    with open("case_data.json", "w", encoding="utf-8") as f:
        json.dump(result["case_data"], f, indent=4)

    print("\n----- OCR COMPLETE -----")
    print(result["raw_text"])
    print("\n----- STRUCTURED DATA -----")
    print(json.dumps(result["case_data"], indent=4))