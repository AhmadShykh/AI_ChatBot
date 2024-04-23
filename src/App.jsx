import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Components/Home";
import "./App.css";
import React from "react";
import Navbar from "./Components/Navbar";
import Prompt from "./Components/Prompt";

function App() {
  return (
    <>
      <div className="appContainer">
        <div className="appGlass">
          <BrowserRouter>
          <Navbar/>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/Prompt" element={<Prompt />} />
            </Routes>
          </BrowserRouter>
        </div>
      </div>
    </>
  );
}

export default App;
