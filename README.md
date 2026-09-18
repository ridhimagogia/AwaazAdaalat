# AwaazAdalat — Intelligence Layer (Person 3)

Chain: **Document Intelligence → Multilingual Explanation → TTS → Smart Alerts**

## Files
| File | Stage | Real or Mock right now? |
|---|---|---|
| `document_intelligence.py` | Extracts case number, court, allegation, hearing date from OCR text | Mock (regex-based) until iNSIGHTS key is added |
| `multilingual.py` | Turns facts into a plain spoken-language explanation + checklist | Mock (Hindi/English templates) until iNSIGHTS key is added |
| `tts.py` | Converts explanation text to an `.mp3` | **Real** — uses free gTTS, no key needed |
| `alerts.py` | Schedules a hearing-date reminder | Mock (returns a computed reminder date) until iNSIGHTS key is added |
| `pipeline.py` | Chains all four stages into one function | This is what Person 1 calls |
| `config.py` | Switches between mock and real iNSIGHTS calls | Edit this when API access is confirmed |

## Quick start
```bash
pip install -r requirements.txt
python3 pipeline.py   # runs a smoke test end-to-end
```

## Switching to the real iNSIGHTS API
Once you have API access:
```bash
export INSIGHTS_API_KEY="your_key_here"
export INSIGHTS_MOCK_MODE="false"
```
Double check the endpoint paths in `config.py` against the actual iNSIGHTS docs —
`/document-intelligence/extract`, `/multilingual/generate`, `/alerts/schedule` are
placeholders based on the plan; update them if the real paths differ.

**Important:** don't remove MOCK_MODE even after real API access works. Keep it as
a fallback — every module already falls back to mock automatically if the real API
call throws an error (bad wifi, rate limit, etc.), so your demo never breaks on stage
even if iNSIGHTS has a bad moment.

## What Person 1 needs to do
Just call one function from the FastAPI backend:
```python
from intelligence_layer.pipeline import run_pipeline

result = run_pipeline(ocr_text, user_id=user.id, language="hi")
# result is a single JSON-serializable dict — hand it straight to the frontend
```

## What Person 2 (frontend) receives
```json
{
  "case_facts": { "case_number": "...", "court_name": "...", "allegation": "...", "hearing_date": "...", "accused_status": "..." },
  "explanation": "plain-language text, ready to display and/or read aloud",
  "checklist": ["step 1", "step 2", "..."],
  "language": "hi",
  "audio_path": "tts_output/explanation_xxxx.mp3",
  "reminder": { "status": "scheduled", "reminder_date": "...", "channel": "..." }
}
```
If `audio_path` is `null`, show the text explanation only — TTS failed gracefully,
don't let it block the demo.

## Privacy Mode note
Per the plan, iNSIGHTS Privacy Mode (zero-log/encrypted) isn't a separate feature to
build — just make sure `raw_text` and `case_facts` aren't logged or persisted longer
than needed. Add that as a one-line config flag in the backend, not a task here.
