import { useNavigate } from "react-router-dom";

import {
  ArrowLeft,
  ArrowRight,
  CheckCircle,
  CalendarDays,
  Languages,
  Volume2,
} from "lucide-react";

import Navbar from "../components/Navbar";

function Explanation() {
  const navigate = useNavigate();

  return (
    <div className="site">

      <Navbar />

      <main className="inner-page">

        <button
          className="back-button"
          onClick={() => navigate("/result")}
        >
          <ArrowLeft size={17} />
          Back
        </button>


        <div className="page-heading">

          <p className="eyebrow">
            SIMPLE EXPLANATION
          </p>

          <h1>
            In simple
            <span> language.</span>
          </h1>

          <p>
            Here's a plain-language explanation of the information
            extracted from your document.
          </p>

        </div>


        <div className="explanation-grid">

          <div className="explanation-main">

            <div className="language-bar">

              <div>
                <Languages size={19} />

                <strong>
                  Simple English
                </strong>
              </div>

              <button className="listen-button">
                <Volume2 size={17} />
                Listen
              </button>

            </div>


            <div className="explanation-text">

              <h2>
                What does this document mean?
              </h2>

              <p>
                This document is a notice about a scheduled
                court hearing. It tells you that a case has a
                hearing on <strong>12 October 2026</strong> at
                the <strong>District Court, Delhi</strong>.
              </p>

              <p>
                The case number mentioned in the document is
                <strong> CR/2026/145</strong>.
              </p>

              <p>
                In simple terms, the important thing is to know
                the hearing date and understand what action may
                be required before or on that date.
              </p>

            </div>

          </div>


          {/* CHECKLIST */}

          <div className="checklist-card">

            <div className="checklist-heading">

              <CheckCircle size={22} />

              <div>
                <span>
                  YOUR CHECKLIST
                </span>

                <h3>
                  What to remember
                </h3>
              </div>

            </div>


            <div className="checklist-item">

              <div className="check-icon">
                1
              </div>

              <div>
                <strong>
                  Note the hearing date
                </strong>

                <p>
                  12 October 2026
                </p>
              </div>

            </div>


            <div className="checklist-item">

              <div className="check-icon">
                2
              </div>

              <div>
                <strong>
                  Keep the document safely
                </strong>

                <p>
                  Carry or retain a copy when needed.
                </p>
              </div>

            </div>


            <div className="checklist-item">

              <div className="check-icon">
                3
              </div>

              <div>
                <strong>
                  Seek legal assistance if needed
                </strong>

                <p>
                  Find information about free legal aid.
                </p>
              </div>

            </div>


            <div className="reminder-box">

              <CalendarDays size={20} />

              <div>
                <strong>
                  Hearing reminder
                </strong>

                <p>
                  Reminder functionality can be connected
                  to the user's preferred notification method.
                </p>
              </div>

            </div>


            <button
              className="primary-btn full-btn"
              onClick={() => navigate("/legal-aid")}
            >
              Find Legal Aid
              <ArrowRight size={18} />
            </button>

          </div>

        </div>


        <div className="legal-note">

          <strong>
            This explanation is informational.
          </strong>
          {" "}
          AwaazAdalat does not provide legal advice,
          represent a person in court or predict case outcomes.

        </div>

      </main>

    </div>
  );
}

export default Explanation;