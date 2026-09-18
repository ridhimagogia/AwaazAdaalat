import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import {
  ArrowLeft,
  ArrowRight,
  FileText,
  UploadCloud,
  X,
  Languages,
} from "lucide-react";

import Navbar from "../components/Navbar";

function Upload() {
  const navigate = useNavigate();

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [language, setLanguage] = useState("hi");

  const handleFile = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const removeFile = () => {
    setFile(null);
  };

  const handleAnalyze = async () => {
    if (!file) {
      alert("Please upload a legal document photo.");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("file", file);
      formData.append("user_id", "user_1");
      formData.append("language", language);

      const response = await axios.post("/analyze-document", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      localStorage.setItem("awaaz_result", JSON.stringify(response.data));
      navigate("/result");
    } catch (err) {
      console.error(err);
      alert("Failed to analyze document. Make sure the backend server is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="site">
      <Navbar />

      <main className="inner-page">
        <button className="back-button" onClick={() => navigate("/")}>
          <ArrowLeft size={17} />
          Back to home
        </button>

        <div className="page-heading">
          <p className="eyebrow">START HERE</p>
          <h1>
            What would you like <span>to understand?</span>
          </h1>
          <p>Upload a legal document image or notice to begin.</p>
        </div>

        {/* Language selector */}
        <div style={{ marginBottom: "25px", display: "flex", alignItems: "center", gap: "10px" }}>
          <Languages size={20} />
          <strong style={{ fontSize: "14px" }}>Target Language:</strong>
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            style={{ padding: "8px 12px", borderRadius: "5px", border: "1px solid #ccc" }}
          >
            <option value="hi">Hindi (हिंदी)</option>
            <option value="en">English</option>
            <option value="pa">Punjabi (ਪੰਜਾਬੀ)</option>
            <option value="ta">Tamil (தமிழ்)</option>
            <option value="te">Telugu (తెలుగు)</option>
            <option value="bn">Bengali (বাংলা)</option>
            <option value="mr">Marathi (मराठी)</option>
          </select>
        </div>

        <div className="upload-grid" style={{ gridTemplateColumns: "1fr" }}>
          {/* File Upload */}
          <div className="upload-card">
            <div className="card-icon">
              <UploadCloud size={27} />
            </div>
            <h2>Upload a document</h2>
            <p>Upload a court notice, FIR, or legal document photo.</p>

            {!file ? (
              <label className="drop-zone">
                <input
                  type="file"
                  accept=".jpg,.jpeg,.png,.webp,.pdf"
                  onChange={handleFile}
                />
                <FileText size={32} />
                <strong>Choose a document</strong>
                <span>WEBP, JPG, PNG, PDF</span>
              </label>
            ) : (
              <div className="selected-file">
                <div className="selected-file-info">
                  <FileText size={25} />
                  <div>
                    <strong>{file.name}</strong>
                    <span>Document ready for analysis</span>
                  </div>
                </div>
                <button type="button" onClick={removeFile} className="remove-file">
                  <X size={18} />
                </button>
              </div>
            )}
          </div>
        </div>

        <div className="upload-actions">
          <button type="button" className="secondary-btn" onClick={() => navigate("/")}>
            Cancel
          </button>
          <button
            type="button"
            className="primary-btn"
            onClick={handleAnalyze}
            disabled={loading || !file}
          >
            {loading ? "Analyzing..." : "Analyze Document"}
            <ArrowRight size={18} />
          </button>
        </div>

        <div className="privacy-note">
          <strong>Privacy note</strong>
          <span>Encrypted processing — legal documents are analyzed and purged immediately.</span>
        </div>
      </main>
    </div>
  );
}

export default Upload;