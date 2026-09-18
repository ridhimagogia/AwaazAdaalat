import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Upload from "./pages/Upload";
import Result from "./pages/Result";
import Explanation from "./pages/Explanation";
import LegalAid from "./pages/LegalAid";

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