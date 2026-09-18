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


