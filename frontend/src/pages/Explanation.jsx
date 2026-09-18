import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  ArrowLeft,
  ArrowRight,
  CheckCircle,
  CalendarDays,
  Languages,
  Volume2,
} from "lucide-react";

import Navbar from "../components/Navbar.jsx";

function Explanation() {
  const navigate = useNavigate();
  const [data, setData] = useState(null);
  const [playing, setPlaying] = useState(false);

  useEffect(() => {
    const raw = localStorage.getItem("awaaz_result");
    if (raw) {
      setData(JSON.parse(raw));
    }
  }, []);

  const handleAudio = () => {
    if (!data?.audio_url) {
      alert("No audio stream available for this document.");
      return;
    }

    const audio = new Audio(`${API_URL}${audioUrl}`);
    setPlaying(true);
    audio.play();
    audio.onended = () => setPlaying(false);
    audio.onerror = () => {
      setPlaying(false);
      alert("Unable to play audio file.");
    };
  };

  const checklist = data?.checklist || [];
  const reminder = data?.reminder || {};

  return (
    <div className="site">
      <Navbar />

      <main className="inner-page">
        <button className="back-button" onClick={() => navigate("/result")}>
          <ArrowLeft size={17} />
          Back
        </button>

        <div className="page-heading">
          <p className="eyebrow">SIMPLE EXPLANATION</p>
          <h1>
            In simple <span>language.</span>
          </h1>
        </div>

        <div className="explanation-grid">
          <div className="explanation-main">
            <div className="language-bar">
              <div>
                <Languages size={19} />
                <strong>Spoken Language ({data?.language?.toUpperCase() || "HI"})</strong>
              </div>

              {data?.audio_url && (
                <button className="listen-button" onClick={handleAudio}>
                  <Volume2 size={17} />
                  {playing ? "Playing..." : "Listen"}
                </button>
              )}
            </div>

            <div className="explanation-text">
              <h2>What does this document mean?</h2>
              <p>{data?.explanation || "No explanation generated."}</p>
            </div>
          </div>

          <div className="checklist-card">
            <div className="checklist-heading">
              <CheckCircle size={22} />
              <div>
                <span>YOUR CHECKLIST</span>
                <h3>What to remember</h3>
              </div>
            </div>

            {checklist.map((item, idx) => (
              <div className="checklist-item" key={idx}>
                <div className="check-icon">{idx + 1}</div>
                <div>
                  <strong>Step {idx + 1}</strong>
                  <p>{item}</p>
                </div>
              </div>
            ))}

            <div className="reminder-box">
              <CalendarDays size={20} />
              <div>
                <strong>Hearing Reminder Scheduled</strong>
                <p>
                  Alert set for: {reminder.reminder_date || "Prior to hearing date"}
                </p>
              </div>
            </div>

            <button className="primary-btn full-btn" onClick={() => navigate("/legal-aid")}>
              Find Legal Aid
              <ArrowRight size={18} />
            </button>
          </div>
        </div>

        <div className="legal-note">
          <strong>This explanation is informational.</strong> AwaazAdalat does not provide legal advice or predict case outcomes.
        </div>
      </main>
    </div>
  );
}

export default Explanation;