import { useNavigate } from "react-router-dom";

import {
  ArrowRight,
  FileText,
  Mic,
  Languages,
  CheckCircle,
  CalendarDays,
  Scale,
  ShieldCheck,
} from "lucide-react";

import Navbar from "../components/Navbar";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="site">

      <Navbar />

      {/* HERO */}

      <section className="hero">

        <div className="hero-left">

          <p className="eyebrow">
            VOICE-FIRST LEGAL ACCESS
          </p>

          <h1>
            Legal information,
            <span> made understandable.</span>
          </h1>

          <p className="hero-text">
            AwaazAdalat helps people understand legal documents,
            important dates and next steps through simple language
            and voice-based access.
          </p>

          <div className="hero-actions">

            <button
              className="primary-btn"
              onClick={() => navigate("/upload")}
            >
              Understand a Document
              <ArrowRight size={18} />
            </button>

            <button
              className="secondary-btn"
              onClick={() => navigate("/upload")}
            >
              <Mic size={18} />
              Speak Instead
            </button>

          </div>

          <div className="hero-trust">
            <ShieldCheck size={17} />
            <span>
              Designed for accessibility • Not legal advice
            </span>
          </div>

        </div>


        {/* DOCUMENT VISUAL */}

        <div className="hero-visual">

          <div className="scanner-wrapper">

            <div className="scanner-label">
              DOCUMENT UNDERSTANDING
            </div>

            <div className="document-card">

              <div className="document-top">
                <div className="document-emblem">
                  <Scale size={20} />
                </div>

                <div>
                  <div className="document-title">
                    DISTRICT COURT
                  </div>

                  <div className="document-subtitle">
                    NOTICE OF HEARING
                  </div>
                </div>
              </div>

              <div className="document-line long"></div>
              <div className="document-line medium"></div>

              <div className="document-details">

                <div>
                  <small>CASE NUMBER</small>
                  <strong>CR/2026/145</strong>
                </div>

                <div>
                  <small>HEARING DATE</small>
                  <strong>12 OCT 2026</strong>
                </div>

              </div>

              <div className="document-line long"></div>

              <div className="document-paragraph">
                Notice regarding appearance before
                the court on the scheduled hearing date.
              </div>

              <div className="document-line medium"></div>

              <div className="document-sign">
                Authorized Officer
              </div>

              <div className="scan-line"></div>

              <div className="extraction-box">

                <div className="extract-item">
                  <span>Case No.</span>
                  <strong>CR/2026/145</strong>
                </div>

                <div className="extract-item">
                  <span>Hearing</span>
                  <strong>12 Oct 2026</strong>
                </div>

              </div>

            </div>

            <div className="scanner-status">
              <span></span>
              Key information detected
            </div>

          </div>

        </div>

      </section>


      {/* PROBLEM */}

      <section className="intro-section" id="about">

        <div className="intro-content">

          <p className="eyebrow">
            THE PROBLEM
          </p>

          <h2>
            The gap isn't always information.
            <br />
            <span>It's understanding.</span>
          </h2>

          <p>
            Legal documents often contain the information a person
            needs — but complicated language, unfamiliar terms and
            limited access to assistance can make that information
            difficult to understand.
          </p>

          <p>
            AwaazAdalat turns important document information into
            clear, actionable explanations that people can listen
            to and understand.
          </p>

        </div>

      </section>


      {/* HOW IT WORKS */}

      <section className="how-section" id="how-it-works">

        <div className="how-heading">

          <div>
            <p className="eyebrow">
              HOW IT WORKS
            </p>

            <h2>
              From document to
              <span> understanding.</span>
            </h2>
          </div>

          <p>
            A simple four-step journey designed around the user's
            actual legal document.
          </p>

        </div>


        <div className="steps-grid">

          <div className="step-card">

            <div className="step-number">
              01
            </div>

            <FileText size={26} />

            <h3>Upload or Speak</h3>

            <p>
              Upload a legal document or describe your situation
              using your voice.
            </p>

          </div>


          <div className="step-card">

            <div className="step-number">
              02
            </div>

            <FileText size={26} />

            <h3>Extract</h3>

            <p>
              Important information such as case numbers,
              dates and court details is identified.
            </p>

          </div>


          <div className="step-card">

            <div className="step-number">
              03
            </div>

            <Languages size={26} />

            <h3>Explain</h3>

            <p>
              Complex legal information is presented in simpler,
              accessible language.
            </p>

          </div>


          <div className="step-card">

            <div className="step-number">
              04
            </div>

            <CheckCircle size={26} />

            <h3>Act</h3>

            <p>
              Get a simple checklist, reminders and information
              about available legal aid.
            </p>

          </div>

        </div>

      </section>


      {/* FEATURES */}

      <section className="access-section">

        <div className="access-heading">

          <p className="eyebrow">
            ACCESSIBILITY FIRST
          </p>

          <h2>
            Legal information should
            <span> meet people where they are.</span>
          </h2>

        </div>


        <div className="access-list">

          <div className="access-row">

            <div className="access-icon">
              <FileText size={21} />
            </div>

            <div>
              <h3>Document Understanding</h3>

              <p>
                Extract key facts from notices, orders and
                other legal documents.
              </p>
            </div>

          </div>


          <div className="access-row">

            <div className="access-icon">
              <Mic size={21} />
            </div>

            <div>
              <h3>Voice-First Access</h3>

              <p>
                Speak naturally instead of navigating complicated
                forms or interfaces.
              </p>
            </div>

          </div>


          <div className="access-row">

            <div className="access-icon">
              <Languages size={21} />
            </div>

            <div>
              <h3>Simple & Regional Language</h3>

              <p>
                Present information in understandable language
                suitable for the user's needs.
              </p>
            </div>

          </div>


          <div className="access-row">

            <div className="access-icon">
              <CalendarDays size={21} />
            </div>

            <div>
              <h3>Next Steps & Reminders</h3>

              <p>
                Highlight important dates and create a simple
                action checklist.
              </p>
            </div>

          </div>

        </div>

      </section>


      {/* FINAL CTA */}

      <section className="final-cta">

        <div>

          <p className="eyebrow">
            AWAazADALAT
          </p>

          <h2>
            Understand the document.
            <br />
            Know the next step.
          </h2>

          <p>
            Turn complicated legal information into something
            people can actually understand.
          </p>

        </div>

        <button
          className="primary-btn"
          onClick={() => navigate("/upload")}
        >
          Try AwaazAdalat
          <ArrowRight size={18} />
        </button>

      </section>


      {/* FOOTER */}

      <footer className="footer">

        <div>
          <strong>आ AwaazAdalat</strong>

          <p>
            Voice-first legal information access.
          </p>
        </div>

        <div className="footer-disclaimer">
          AwaazAdalat provides informational support
          and does not provide legal advice.
        </div>

      </footer>

    </div>
  );
}

export default Home;