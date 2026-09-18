# 🛡️ AwaazAdalat (आवाज़ अदालत)
> **Voice-First Legal Information Access for Undertrials & Low-Literacy Citizens**

Millions of poor, rural, and low-literacy citizens in India get stuck in the legal system simply because court notices, FIRs, and bail documents are written in dense legal English or Hindi. People miss hearing dates or remain detained as undertrials simply because they cannot read or comprehend their own case papers[cite: 20, 25].

**AwaazAdalat** bridges this literacy gap by turning dense, terrifying legal notices into clear, plain-language summaries, actionable checklists, and spoken regional audio[cite: 13, 20, 26, 28].

---

## 🔗 How iNSIGHTS AI Powers AwaazAdalat

AwaazAdalat leverages the **iNSIGHTS AI Suite** (`insights-ai.info`) to handle complex legal language processing, multi-dialect translation, privacy compliance, and proactive scheduling.

| iNSIGHTS Module | Project Usage & Integration |
| :--- | :--- |
| **iNSIGHTS Document Intelligence** | Analyzes raw OCR text from scanned notices to extract structured legal entities, including case numbers, allegations, hearing dates, court names, and undertrial bail status[cite: 22, 25]. |
| **iNSIGHTS Multilingual** | Converts dense legal jargon and statutes into simple, spoken-style regional language summaries and actionable checklists across 7 languages (Hindi, English, Punjabi, Tamil, Telugu, Bengali, Marathi)[cite: 22, 26]. |
| **iNSIGHTS Smart Alerts** | Calculates exact hearing dates and automatically schedules SMS/Push reminders 2 days prior to ensure undertrials never miss a court appearance[cite: 22, 23]. |
| **iNSIGHTS Privacy Mode** | Ensures zero-log, end-to-end encrypted processing of sensitive personal legal documents[cite: 22]. Raw texts and case files are analyzed strictly in-memory and purged immediately[cite: 20]. |

> *Note: The system includes a built-in mock fallback mode (`config.py`) to ensure seamless offline or stage-demo reliability even during network disruptions[cite: 22, 24, 25].*
[ Scanned Document / Photo ]
│
▼
[ OCR Processing Engine (Tesseract) ] ──> Raw Extracted Text
│
▼
[ iNSIGHTS Document Intelligence ] ───> Case Facts (Case No, Date, Court)
│
▼
[ iNSIGHTS Multilingual Engine ] ─────> Plain Regional Language & Checklist
│
├───> [ gTTS Speech Synthesis ] ──> Spoken Regional Audio (.mp3)
│
└───> [ iNSIGHTS Smart Alerts ] ───> Hearing Date Reminders
---

## 🧩 Tech Stack

- **Frontend:** React, Vite, React Router, Lucide React Icons, Axios[cite: 4, 9, 16]
- **Backend:** Python 3.11+, FastAPI, Uvicorn[cite: 4, 20]
- **OCR Engine:** Tesseract OCR, Pillow[cite: 4, 21]
- **Speech Engine:** Google Text-to-Speech (`gTTS`)[cite: 4, 28]
- **Deployment:** Vercel (Frontend) + Render / Docker (Backend)

---

## 🚀 Quickstart Guide

### 1. Backend Setup

```bash
# Clone the repository
git clone [https://github.com/ridhimagogia/AwaazAdaalat.git](https://github.com/ridhimagogia/AwaazAdaalat.git)
cd AwaazAdaalat

# Install Python dependencies
pip install -r requirements.txt

# Start FastAPI development server
python -m uvicorn main:app --reload
```
The FastAPI backend runs at http://127.0.0.1:8000[cite: 20].

### 2. Frontend Setup
```bash
# Navigate to frontend folder
cd frontend

# Install Node dependencies
npm install

# Start Vite React server
npm run dev
```
The React frontend runs at http://localhost:5173.

## 🔑 Environment Variables
To activate live iNSIGHTS API integration, set the following environment variables in intelligence_layer/config.py or your server environment[cite: 22, 24]:

```bash
INSIGHTS_API_KEY="your_insights_api_key"
INSIGHTS_MOCK_MODE="false"
```
### ⚖️ Honest Scope & Legal Disclaimer:
AwaazAdalat is designed purely as an informational accessibility tool. It does not provide legal representation, offer formal legal advice, or predict case outcomes. It clarifies document text, outlines deadlines in plain language, and directs users to nearby official legal aid clinics.   
