import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  ArrowLeft,
  ArrowRight,
  CalendarDays,
  FileText,
  MapPin,
  Scale,
} from "lucide-react";

import Navbar from "../components/Navbar.jsx";

function Result() {
  const navigate = useNavigate();
  const [data, setData] = useState(null);

  useEffect(() => {
    const raw = localStorage.getItem("awaaz_result");
    if (raw) {
      setData(JSON.parse(raw));
    }
  }, []);

  const caseFacts = data?.case_facts || {};

  return (
    <div className="site">
      <Navbar />

      <main className="inner-page">
        <button className="back-button" onClick={() => navigate("/upload")}>
          <ArrowLeft size={17} />
          Back
        </button>

        <div className="page-heading">
          <p className="eyebrow">DOCUMENT ANALYSIS</p>
          <h1>
            Here's what we <span>found.</span>
          </h1>
          <p>Key information extracted from your uploaded legal notice.</p>
        </div>

        <div className="result-container">
          <div className="result-main">
            <div className="result-header">
              <div className="result-icon">
                <FileText size={25} />
              </div>
              <div>
                <h2>Case Summary</h2>
                <p>Extraction complete</p>
              </div>
            </div>

            <div className="result-fields">
              <div className="result-field">
                <span>
                  <FileText size={16} /> Case Number
                </span>
                <strong>{caseFacts.case_number || "Not found"}</strong>
              </div>

              <div className="result-field">
                <span>
                  <Scale size={16} /> Allegation
                </span>
                <strong>{caseFacts.allegation || "Not specified"}</strong>
              </div>

              <div className="result-field">
                <span>
                  <MapPin size={16} /> Court
                </span>
                <strong>{caseFacts.court_name || "Not found"}</strong>
              </div>

              <div className="result-field">
                <span>
                  <CalendarDays size={16} /> Hearing Date
                </span>
                <strong>{caseFacts.hearing_date || "Not found"}</strong>
              </div>
            </div>
          </div>

          <div className="result-side">
            <div className="result-side-label">NEXT</div>
            <h3>Understand what this means</h3>
            <p>
              Hear a simple spoken explanation in your language and view your action checklist.
            </p>
            <button className="primary-btn full-btn" onClick={() => navigate("/explanation")}>
              Explain Simply
              <ArrowRight size={18} />
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}

export default Result;