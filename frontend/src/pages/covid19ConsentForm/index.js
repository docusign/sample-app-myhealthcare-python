import React, { useState, useEffect, useContext } from "react";
import AppContext from "../../context/appContext";
import { useTranslation } from "react-i18next";
import { useHistory } from "react-router-dom";
import InputText from "../../components/inputText";
import InputPhone from "../../components/inputPhone";
import SeeMore from "../../components/seeMore";
import { sendRequest } from "../../api/healthcareAPI";
import { getStatus } from "../../api/auth";
import parse from 'html-react-parser';

const Covid19ConsentForm = () => {
    let history = useHistory();

    const { t } = useTranslation("Covid19ConsentForm");

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

    async function  handleSubmit(event) {
        event.preventDefault();

        getStatus(setLogged, history);
        setApiError("")

        setSubmitted(true);
        if (!logged) history.push("")

        if (!isFormValid()) return;

        setBackdrop(true);
        const el = event.target.elements;
        const body = {
            first_name: el.FirstName.value,
            last_name: el.LastName.value,
            country_code: el.CountryCode.value,
            phone_number: el.PhoneNumber.value
        };

        try{
            const response = await sendRequest(body, "/covid19-consent-form");
            if(response.data.message.includes("OPTED_OUT_PHONE_NUMBER_FOR_RECIPIENT"))
              setApiError(t("ErrorOptedOut"));
            else if (response.data.message.includes("SIGNER_CONSENT_PENDING_OR_DECLINED"))
              setApiError(t("ErrorDidNotConsent"));
            else if (response.data.message.includes("SMS"))
                setApiError(t("ErrorSMSNotEnabled"));
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
                                {parse(apiError)}
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
                            <InputPhone
                                label={t("PhoneNumber")}
                                errorText={t("ErrorText")}
                                errorTextInv={t("ErrorTextInv")}
                                setFormError={setFormError}
                                formError={formError}
                                formErrorNum={2}
                                submitted={submitted}
                            />
                            <button className="h-card-button" type="submit">{t("ButtonName")}</button>
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
export default Covid19ConsentForm;