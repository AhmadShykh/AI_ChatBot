import React from "react";
import "./Prompt.css";
import { useState } from "react";
import { LuSend } from "react-icons/lu";
import p2 from "../assets/p2.png";
const Prompt = () => {
  const [prompt, setPrompt] = useState(" ");
  const setValue = (e) => {
    setPrompt(e.target.value);
  };
  const submit = (e) => {
    e.preventDefault();
    setPrompt(" ");
  };
  return (
    <>
      <div className="promptcontainer">
        <div className="main1">
        <div className="result">
          <p>Your data set</p>
        </div>
        <div className="pic2">
            <img src={p2} alt="pic" />
        </div>
        </div>

        <div className="message">
          <input
            type="text"
            placeholder=" Enter Prompt "
            value={prompt}
            onChange={setValue}
          />
          <button className="btn" onClick={submit}>
            <LuSend style={{ fontSize: "large" ,textAlign:"center"}} />
          </button>
        </div>
      </div>
    </>
  );
};

export default Prompt;
