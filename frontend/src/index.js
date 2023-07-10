import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./i18n";

const container = document.getElementById("root");
const root = ReactDOM.createRoot(container);

const app = (
  <BrowserRouter>
    <App />
  </BrowserRouter> 
);
root.render(app);
