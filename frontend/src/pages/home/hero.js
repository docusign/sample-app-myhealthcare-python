import React from "react";
import { useTranslation } from "react-i18next";

const Hero = () => {
    const { t } = useTranslation("Home")
    return (
        <section className="hero-section bg-prop">
            <div className="container-fluid">
                <div className="hero-text text-center">
                    <h1 className="h1">
                        {t("Header1.P1")}
                        <div className="w-100 d-block d-md-none"></div>
                        {t("Header1.P2")}
                    </h1>
                    <div className="sub-title">{t("Header2")}</div>
                </div>
            </div>
        </section>
    );
}
export default Hero;