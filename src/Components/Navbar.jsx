import React from 'react'
import './Navbar.css'
import { Link } from "react-router-dom";
import { AiOutlineHome } from "react-icons/ai";
import { TbPrompt } from "react-icons/tb";
import { FcAbout } from "react-icons/fc";
import { RiContactsLine } from "react-icons/ri";
const Navbar = () => {
  return (
    <>
     <nav>
          <div className="logo">
            <h2>AiProject</h2>
          </div>
          <ul>
            <div className="box">
              <li>
                <Link
                  style={{ textDecoration: "none ", color: "#ffffff33",fontWeight:"bolder" }}
                  to={"/"}
                >
                  Home
                </Link>
              </li>
              <p>
                <AiOutlineHome />
              </p>
            </div>
            <div className="box">
              <li>
                <Link
                  style={{ textDecoration: "none ", color: "#ffffff33" ,fontWeight:"bolder"}}
                  to={"/Prompt"}
                >
                  Prompt
                </Link>
              </li>
              <p>
                <TbPrompt />
              </p>
            </div>
            <div className="box">
              <li>
                <Link
                  style={{ textDecoration: "none ", color: "#ffffff33",fontWeight:"bolder" }}
                  to={"/"}
                >
                  About
                </Link>
              </li>
              <p>
                <FcAbout />
              </p>
            </div>
            <div className="box">
              <li>
                <Link
                  style={{ textDecoration: "none ", color: "#ffffff33",fontWeight:"bolder" }}
                  to={"/"}
                >
                  Contact
                </Link>
              </li>
              <p>
                <RiContactsLine />
              </p>
            </div>
          </ul>
          <div className="signup">
            <button>Sign Up</button>
          </div>
        </nav>
    </>
  )
}

export default Navbar;