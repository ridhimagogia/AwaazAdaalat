import os
import shutil
import uuid

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from ocr import extract_structured_data
from intelligence_layer.pipeline import run_pipeline

app = FastAPI(title="AwaazAdalat Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
TTS_DIR = "tts_output"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TTS_DIR, exist_ok=True)

app.mount("/tts_output", StaticFiles(directory=TTS_DIR), name="tts_output")


@app.get("/")
def health_check():
    return {"status": "AwaazAdalat backend is running"}


@app.post("/analyze-document")
async def analyze_document(
    file: UploadFile = File(...),
    user_id: str = Form("user_1"),
    language: str = Form("hi"),
):
    ext = os.path.splitext(file.filename)[1] or ".jpg"
    temp_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4().hex}{ext}")

    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        ocr_result = extract_structured_data(temp_path)
        raw_text = ocr_result["raw_text"]

        pipeline_result = run_pipeline(raw_text, user_id=user_id, language=language)

        audio_filename = None
        if pipeline_result.get("audio_path"):
            audio_filename = os.path.basename(pipeline_result["audio_path"])

        return {
            "ocr_raw_text": raw_text,
            "ocr_case_data": ocr_result["case_data"],
            "case_facts": pipeline_result["case_facts"],
            "explanation": pipeline_result["explanation"],
            "checklist": pipeline_result["checklist"],
            "language": pipeline_result["language"],
            "audio_url": f"/tts_output/{audio_filename}" if audio_filename else None,
            "reminder": pipeline_result["reminder"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)