from datetime import datetime, timedelta
import requests
try:
    from . import config
except ImportError:
    import config


def _parse_date(date_str: str):
    """Try a few common formats since OCR'd dates are messy."""
    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def _mock_schedule(hearing_date: str, user_id: str, reminder_days_before: int) -> dict:
    parsed = _parse_date(hearing_date)
    if parsed:
        remind_at = parsed - timedelta(days=reminder_days_before)
        remind_at_str = remind_at.strftime("%d/%m/%Y")
    else:
        remind_at_str = "1 day before hearing (exact date unparseable — check manually)"

    return {
        "status": "scheduled",
        "user_id": user_id,
        "hearing_date": hearing_date,
        "reminder_date": remind_at_str,
        "channel": "sms+push (mock)",
        "source": "mock",
    }


def schedule_reminder(hearing_date: str, user_id: str, reminder_days_before: int = 2) -> dict:
    
    if config.MOCK_MODE:
        return _mock_schedule(hearing_date, user_id, reminder_days_before)

    try:
        response = requests.post(
            config.SMART_ALERTS_ENDPOINT,
            headers={"Authorization": f"Bearer {config.INSIGHTS_API_KEY}"},
            json={
                "user_id": user_id,
                "event_date": hearing_date,
                "remind_days_before": reminder_days_before,
            },
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
        return {
            "status": data.get("status", "unknown"),
            "user_id": user_id,
            "hearing_date": hearing_date,
            "reminder_date": data.get("reminder_date", ""),
            "channel": data.get("channel", "insights_alerts"),
            "source": "insights_api",
        }
    except requests.RequestException as e:
        print(f"[alerts] iNSIGHTS Smart Alerts failed ({e}), falling back to mock "
              f"(in production, fall back to Firebase Cloud Messaging here).")
        return _mock_schedule(hearing_date, user_id, reminder_days_before)


if __name__ == "__main__":
    import json
    print(json.dumps(schedule_reminder("12/10/2026", user_id="demo_user_1"), indent=2))
