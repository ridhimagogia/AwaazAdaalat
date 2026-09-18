import { Link, useNavigate } from "react-router-dom";
import { Scale } from "lucide-react";

function Navbar() {
  const navigate = useNavigate();

  return (
    <nav className="navbar">
      <Link to="/" className="logo">
        <span className="logo-mark">
          <Scale size={20} />
        </span>

        <span>
          <strong>आ AwaazAdalat</strong>
        </span>
      </Link>

      <div className="nav-links">
        <a href="/#about">About</a>
        <a href="/#how-it-works">How It Works</a>
        <Link to="/legal-aid">Legal Aid</Link>
      </div>

      <button
        className="nav-cta"
        onClick={() => navigate("/upload")}
      >
        Try AwaazAdalat
      </button>
    </nav>
  );
}

export default Navbar;