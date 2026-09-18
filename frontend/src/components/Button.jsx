import { ArrowRight } from "lucide-react";

function Button({ children, onClick, type = "button", secondary = false }) {
  return (
    <button
      type={type}
      onClick={onClick}
      className={secondary ? "secondary-btn" : "primary-btn"}
    >
      {children}
      {!secondary && <ArrowRight size={18} />}
    </button>
  );
}

export default Button;