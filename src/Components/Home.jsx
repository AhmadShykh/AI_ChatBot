import React from "react";
import "./Home.css";
import p1 from "../assets/p1.png";

const Home = () => {
  return (
    <>
      <div className="homeContainer">
       
        <div className="main">
          <div className="left">
            <h1>
              Artificial Intelligence is the
              <br /> Trend Today
              <br />
              Welcome to the <br /> World of <span>AI</span>
            </h1>
            <p>Create,Explore Collect information</p>
            <button className="button">Explore Now</button>
          </div>
          <div className="right">
           <div className="pic">
            <img src={p1} alt="robot" />
           </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Home;
