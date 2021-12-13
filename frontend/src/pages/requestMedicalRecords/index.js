import React, { useState, useEffect, useContext } from "react";
import AppContext from "../../context/appContext";
import { useTranslation } from "react-i18next";
import { useHistory } from "react-router-dom";
import InputText from "../../components/inputText";
import InputEmail from "../../components/inputEmail";
import SeeMore from "../../components/seeMore";
import { sendRequest } from "../../api/healthcareAPI";
import { getStatus } from "../../api/auth";

const RequestMedicalRecords = () => {
    let history = useHistory();

    const { t } = useTranslation("RequestMedicalRecords");

    const [ submitted, setSubmitted ] = useState(false);
    const [ formError, setFormError ] = useState([true, true, true]);
    const [ apiError, setApiError ] = useState("");

    const { setBackdrop, logged, setLogged } = useContext(AppContext)

    useEffect(() => {
        if (!logged) history.push("")
    }, )

    function isFormValid() {
        return formError.every(elem => elem === false)
    }

    async function handleSubmit (event) {
        event.preventDefault();

        getStatus(setLogged, history);
        setApiError("")

        setSubmitted(true);
        if (!logged) history.push("")
        
        if (!isFormValid()) return;
        
        setBackdrop(true);
        const el = event.target.elements;
        const body = {
            name: `${el.FirstName.value} ${el.LastName.value}`,
            email: el.Email.value
        };

        try{
            const response = await sendRequest(body, "/request-medical-records");
            if (response.data.message.includes("IDV")) 
                setApiError(t("ErrorIDVNotEnabled"))
            else 
                history.push("/success");
        } catch (error) {
            setApiError(error.message)
        } finally {
            setBackdrop(false);
        }
    }

    return (
        <section className="content-section">
            <div className="container">
                {apiError &&
                    <div className="text-center">
                            <div className="alert alert-danger" role="alert">
                                {apiError}
                            </div>
                    </div>
                }
                <div className="row justify-content-center">

                    <div className="col form-holder">
                        <form onSubmit={handleSubmit}>
                            <h4 className="card-title">{t("Title")}</h4>
                            <InputText
                                id="FirstName"
                                label={t("FirstName")}
                                errorText={t("ErrorText")}
                                setFormError={setFormError}
                                formError={formError}
                                formErrorNum={0}
                                submitted={submitted}
                            />
                            <InputText
                                id="LastName"
                                label={t("LastName")}
                                errorText={t("ErrorText")}
                                setFormError={setFormError}
                                formError={formError}
                                formErrorNum={1}
                                submitted={submitted}
                            />
                            <InputEmail
                                id="Email"
                                label={t("Email")}
                                errorText={t("ErrorText")}
                                setFormError={setFormError}
                                formError={formError}
                                formErrorNum={2}
                                submitted={submitted}
                            />
                            <button className="h-card-button" type="submit">Submit</button>
                        </form>
                    </div>

                    <div className="w-100 d-block d-md-none"></div>

                    <SeeMore
                        title={t("SeeMore.Title")}
                        text={t("SeeMore.Text")}
                    />

                </div>
            </div>
        </section>
    )
}
export default RequestMedicalRecords;