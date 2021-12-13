import React, { Suspense, useState, useEffect } from "react";
import { Switch, Route } from "react-router-dom";
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

  useEffect(() => {
    getStatus(setLogged);
  }, []);

  return (
    <Suspense fallback="">
      <AppContext.Provider
        value={{ modalShow, setModalShow, logged, setLogged, nextPage, setNextPage, setBackdrop }}
      >
        <Header />
        <Switch>
          <Route path="/request-medical-records" component={RequestMedicalRecords} />
          <Route path="/covid19-consent-form" component={Covid19ConsentForm} />
          <Route path="/apply-for-patient-assistance" component={ApplyForPatientAssistance} />
          <Route path="/success" component={Success} />
          <Route path="/" exact component={Home} />
          <Route path="/callback" component={Callback} />
        </Switch>

        <ModalLogin modalShow={modalShow} setModalShow={setModalShow} />

        <Footer />

        <BackdropLoader backdrop={backdrop} />

      </AppContext.Provider>
    </Suspense>
  );
}
export default App;