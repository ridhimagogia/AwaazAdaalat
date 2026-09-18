import requests
from typing import Optional
try:
    from . import config
except ImportError:
    import config

_TEMPLATES = {
    "hi": {
        "explanation": (
            "आपका केस नंबर {case_number} है। यह मामला {court_name} में चल रहा है। "
            "आप पर {allegation} का आरोप है। आपकी अगली सुनवाई की तारीख {hearing_date} है। "
            "आप अभी जमानत के लिए आवेदन नहीं कर पाए हैं — यह जल्द कर लेना ज़रूरी है।"
        ),
        "checklist": [
            f"अगली सुनवाई की तारीख याद रखें: {{hearing_date}}",
            "नज़दीकी मुफ़्त कानूनी सहायता केंद्र से संपर्क करें",
            "अगर जमानत नहीं मिली है, तो वकील की मदद से आवेदन करें",
            "सुनवाई के दिन ज़रूरी दस्तावेज़ साथ लेकर जाएं",
        ],
    },
    "en": {
        "explanation": (
            "Your case number is {case_number}, being heard at {court_name}. "
            "You are alleged to have committed: {allegation}. "
            "Your next hearing date is {hearing_date}. "
            "You have not yet applied for bail — it's important to do this soon."
        ),
        "checklist": [
            "Remember your next hearing date: {hearing_date}",
            "Contact your nearest free legal aid clinic",
            "If bail hasn't been granted, apply with a lawyer's help",
            "Bring required documents on the hearing date",
        ],
    },
    "pa": {
        "explanation": (
            "ਤੁਹਾਡਾ ਕੇਸ ਨੰਬਰ {case_number} ਹੈ। ਇਹ ਮਾਮਲਾ {court_name} ਵਿੱਚ ਚੱਲ ਰਿਹਾ ਹੈ। "
            "ਤੁਹਾਡੇ ਉੱਤੇ {allegation} ਦਾ ਦੋਸ਼ ਹੈ। ਤੁਹਾਡੀ ਅਗਲੀ ਸੁਣਵਾਈ ਦੀ ਤਾਰੀਖ {hearing_date} ਹੈ। "
            "ਤੁਸੀਂ ਹਾਲੇ ਜ਼ਮਾਨਤ ਲਈ ਅਰਜ਼ੀ ਨਹੀਂ ਦਿੱਤੀ — ਇਹ ਜਲਦੀ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ।"
        ),
        "checklist": [
            "ਅਗਲੀ ਸੁਣਵਾਈ ਦੀ ਤਾਰੀਖ ਯਾਦ ਰੱਖੋ: {hearing_date}",
            "ਨੇੜਲੇ ਮੁਫ਼ਤ ਕਾਨੂੰਨੀ ਸਹਾਇਤਾ ਕੇਂਦਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ",
            "ਜੇ ਜ਼ਮਾਨਤ ਨਹੀਂ ਮਿਲੀ, ਤਾਂ ਵਕੀਲ ਦੀ ਮਦਦ ਨਾਲ ਅਰਜ਼ੀ ਦਿਓ",
            "ਸੁਣਵਾਈ ਵਾਲੇ ਦਿਨ ਜ਼ਰੂਰੀ ਦਸਤਾਵੇਜ਼ ਨਾਲ ਲੈ ਕੇ ਜਾਓ",
        ],
    },
    "ta": {
        "explanation": (
            "உங்கள் வழக்கு எண் {case_number}. இந்த வழக்கு {court_name} இல் நடைபெறுகிறது. "
            "உங்கள் மீது {allegation} என்ற குற்றச்சாட்டு உள்ளது. உங்கள் அடுத்த விசாரணை தேதி {hearing_date}. "
            "நீங்கள் இன்னும் பிணைக்கு விண்ணப்பிக்கவில்லை — இதை விரைவில் செய்வது முக்கியம்."
        ),
        "checklist": [
            "அடுத்த விசாரணை தேதியை நினைவில் கொள்ளுங்கள்: {hearing_date}",
            "அருகிலுள்ள இலவச சட்ட உதவி மையத்தை தொடர்பு கொள்ளுங்கள்",
            "பிணை கிடைக்கவில்லை என்றால், வழக்கறிஞர் உதவியுடன் விண்ணப்பியுங்கள்",
            "விசாரணை நாளில் தேவையான ஆவணங்களை கொண்டு வாருங்கள்",
        ],
    },
    "te": {
        "explanation": (
            "మీ కేసు నంబర్ {case_number}. ఈ కేసు {court_name} లో నడుస్తోంది. "
            "మీపై {allegation} అనే ఆరోపణ ఉంది. మీ తదుపరి విచారణ తేదీ {hearing_date}. "
            "మీరు ఇంకా బెయిల్ కోసం దరఖాస్తు చేయలేదు — దీన్ని త్వరగా చేయడం ముఖ్యం."
        ),
        "checklist": [
            "తదుపరి విచారణ తేదీని గుర్తుంచుకోండి: {hearing_date}",
            "సమీపంలోని ఉచిత న్యాయ సహాయ కేంద్రాన్ని సంప్రదించండి",
            "బెయిల్ రాకపోతే, న్యాయవాది సహాయంతో దరఖాస్తు చేయండి",
            "విచారణ రోజున అవసరమైన పత్రాలను తీసుకురండి",
        ],
    },
    "bn": {
        "explanation": (
            "আপনার মামলা নম্বর {case_number}। এই মামলাটি {court_name} এ চলছে। "
            "আপনার বিরুদ্ধে {allegation} অভিযোগ আছে। আপনার পরবর্তী শুনানির তারিখ {hearing_date}। "
            "আপনি এখনও জামিনের জন্য আবেদন করেননি — এটি শীঘ্রই করা জরুরি।"
        ),
        "checklist": [
            "পরবর্তী শুনানির তারিখ মনে রাখুন: {hearing_date}",
            "নিকটস্থ বিনামূল্যে আইনি সহায়তা কেন্দ্রে যোগাযোগ করুন",
            "জামিন না পেলে, আইনজীবীর সাহায্যে আবেদন করুন",
            "শুনানির দিন প্রয়োজনীয় নথি সাথে আনুন",
        ],
    },
    "mr": {
        "explanation": (
            "तुमचा केस क्रमांक {case_number} आहे. हे प्रकरण {court_name} मध्ये सुरू आहे. "
            "तुमच्यावर {allegation} असा आरोप आहे. तुमची पुढील सुनावणीची तारीख {hearing_date} आहे. "
            "तुम्ही अजून जामिनासाठी अर्ज केलेला नाही — हे लवकर करणे महत्त्वाचे आहे."
        ),
        "checklist": [
            "पुढील सुनावणीची तारीख लक्षात ठेवा: {hearing_date}",
            "जवळच्या मोफत कायदेशीर मदत केंद्राशी संपर्क साधा",
            "जामीन मिळाला नसेल, तर वकिलाच्या मदतीने अर्ज करा",
            "सुनावणीच्या दिवशी आवश्यक कागदपत्रे घेऊन जा",
        ],
    },
}


def _fill(template: str, facts: dict) -> str:
    try:
        return template.format(**facts)
    except KeyError:
        return template


def _mock_explain(facts: dict, language: str) -> dict:
    tpl = _TEMPLATES.get(language, _TEMPLATES["en"])
    return {
        "explanation": _fill(tpl["explanation"], facts),
        "checklist": [_fill(item, facts) for item in tpl["checklist"]],
        "language": language,
        "source": "mock",
    }


def explain_case(facts: dict, language: Optional[str] = None) -> dict:

    language = language or config.DEFAULT_LANGUAGE

    if config.MOCK_MODE:
        return _mock_explain(facts, language)

    try:
        response = requests.post(
            config.MULTILINGUAL_ENDPOINT,
            headers={"Authorization": f"Bearer {config.INSIGHTS_API_KEY}"},
            json={"facts": facts, "language": language, "style": "plain_spoken"},
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
        return {
            "explanation": data.get("explanation", ""),
            "checklist": data.get("checklist", []),
            "language": language,
            "source": "insights_api",
        }
    except requests.RequestException as e:
        print(f"[multilingual] API call failed ({e}), falling back to mock.")
        return _mock_explain(facts, language)


if __name__ == "__main__":
    import json
    sample_facts = {
        "case_number": "CR-2026-0417",
        "court_name": "District Court, Sample Nagar",
        "allegation": "theft under Section 379 IPC",
        "hearing_date": "12/10/2026",
        "accused_status": "Undertrial",
    }
    print(json.dumps(explain_case(sample_facts, "hi"), indent=2, ensure_ascii=False))