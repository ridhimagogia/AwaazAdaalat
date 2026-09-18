import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home.jsx";
import Upload from "./pages/Upload.jsx";
import Result from "./pages/Result.jsx";
import Explanation from "./pages/Explanation.jsx";
import LegalAid from "./pages/LegalAid.jsx";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<Upload />} />
        <Route path="/result" element={<Result />} />
        <Route path="/explanation" element={<Explanation />} />
        <Route path="/legal-aid" element={<LegalAid />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;