import React from "react";
import axios from "axios";
import "./Prompt.css";
import { useState } from "react";
import { LuSend } from "react-icons/lu";
import p2 from "../assets/p2.png";
const Prompt = () => {
  const [prompt, setPrompt] = useState(" ");
  const [response, setResponse] = useState("");

  const setValue = (e) => {
    setPrompt(e.target.value);
  };
  const submit = async () => {
    try {
      const { data } = await axios.post("http://127.0.0.1:5000/chat", {
        prompt,
      });
      setResponse(data.response);
      console.log(data);
    } catch (error) {
      console.error("Error:", error);
    }
  };
  return (
    <>
      <div className="promptcontainer">
        <div className="main1">
          <div className="result">
            <p>{response}</p>
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
            <LuSend style={{ fontSize: "large", textAlign: "center" }} />
          </button>
        </div>
      </div>
    </>
  );
};

export default Prompt;
