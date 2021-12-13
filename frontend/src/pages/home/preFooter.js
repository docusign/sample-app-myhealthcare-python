import React from "react";
import { useTranslation } from "react-i18next";

const PreFooter = () => {
    const { t } = useTranslation("Home")
    return (
        <section className="text-center">
            <div className="container cta-section">
                <h2 className="h2 cta-title">{t("PreFooter1")}</h2>
                <div className="cta-description">{t("PreFooter2")}</div>
            </div>
            <div className="cta-links">
                <div className="first-link">
                    <a
                        href={t("GetFreeLink")}
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        {t("GetFreeLinkName")}
                    </a>
                </div>
                <div className="second-link">
                    <a
                        className="second-link"
                        href={t("PythonSDKLink")}
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        {t("PythonSDKLinkName")}
                    </a>
                    </div>
            </div>
        </section>
    );
}
export default PreFooter;