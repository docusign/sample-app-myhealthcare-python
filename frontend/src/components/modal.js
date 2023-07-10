import React, { useContext, useState } from "react";
import AppContext from "../context/appContext";
import { getStatus, codeGrantAuth } from "../api/auth";
import { Modal } from "react-bootstrap";
import { jwtAuth } from "../api/auth";
import { useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import parse from "html-react-parser";

const ModalLogin = props => {
    let navigate = useNavigate();

    const { t } = useTranslation("Modal");

    const [error, setError] = useState("");

    const handleClose = () => {
        props.setModalShow(false);
        setError("");
    }

    const { setLogged, nextPage, setNextPage } = useContext(AppContext);

    async function handleLogin(loginType) {
        try {
            if (loginType === "oauth") {
                localStorage.setItem("nextPage", nextPage);
                await codeGrantAuth();
            }
            else {
                await jwtAuth();
                await getStatus(setLogged);
                handleClose();
                navigate(nextPage)
                setNextPage("");
            }
        } catch(error) {
            if (!error.response || error.response.status !== 401) {
                setError(error.message);
            }
        }
    }

    return (
        <Modal
            show={props.modalShow}
            onHide={handleClose}
            keyboard={true}
            centered
        >
            <div className="modal-header">
              <button type="button" className="close" onClick={handleClose}>
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div className="modal-body text-center">
                {error && (
                    <div className="alert alert-danger mt-2">{error}</div>
                )}
                <h2>{t("Title")}</h2>
                <p>
                    {parse(t("LearnMore"))}
                </p>
                <p>
                    {parse(t("AboutIDVAndSMS"))}
                </p>
                <button className="b1" onClick={() => handleLogin("oauth")}>
                    {t("LoginOauth")}
                </button>
                <button className="b2" onClick={() => handleLogin("jwt")}>
                    {t("LoginJWT")}
                </button>
            </div>
            <div className="modal-footer_ text-center">
                {parse(t("Warning"))}
            </div>
        </Modal>
    );
}
export default ModalLogin;