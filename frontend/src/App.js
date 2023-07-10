import React, { Suspense, useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import { getStatus } from "./api/auth";
import AppContext from "./context/appContext";
import Header from "./components/header";
import Home from "./pages/home"
import RequestMedicalRecords from "./pages/requestMedicalRecords";
import ApplyForPatientAssistance from "./pages/applyForPatientAssistance";
import Covid19ConsentForm from "./pages/covid19ConsentForm";
import Success from "./pages/success";
import ModalLogin from "./components/modal";
import Footer from "./components/footer";
import { Callback } from "./components/Callback";
import BackdropLoader from "./components/backdropLoader";
import "./assets/scss/main.scss";

function App() {
  const [logged, setLogged] = useState(false);
  const [modalShow, setModalShow] = useState(false);
  const [nextPage, setNextPage] = useState("");
  const [backdrop, setBackdrop] = useState(0);
  const axios = require('axios').default;

  useEffect(() => {
    getStatus(setLogged);
  }, []);
/*
  if (window.location.origin === "http://localhost:3000") {
	    axios.defaults.baseURL = "http://127.0.0.1:5001";
  } else {
	    axios.defaults.baseURL = window.location.origin;
  }*/
  return (
    <Suspense fallback="">
      <AppContext.Provider
        value={{ modalShow, setModalShow, logged, setLogged, nextPage, setNextPage, setBackdrop }}
      >
        <Header />
        <Routes>
          <Route path="/request-medical-records" element={<RequestMedicalRecords/>} />
          <Route path="/covid19-consent-form" element={<Covid19ConsentForm/>} />
          <Route path="/apply-for-patient-assistance" element={<ApplyForPatientAssistance/>} />
          <Route path="/success" element={<Success/>} />
          <Route path="/" exact element={<Home/>} />
          <Route path="/callback" element={<Callback/>} />
        </Routes>

        <ModalLogin modalShow={modalShow} setModalShow={setModalShow} />

        <Footer />

        <BackdropLoader backdrop={backdrop} />

      </AppContext.Provider>
    </Suspense>
  );
}
export default App;
