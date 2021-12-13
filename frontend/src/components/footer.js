import React from "react";
import { useTranslation } from "react-i18next";

const Footer = () => {
    const { t } = useTranslation("Common");
    return (
        <footer className="footer">
            <div className="container text-center pt-3">
                <span className="copyright">{t("Copyright")}</span>
            </div>
        </footer>
    )
}
export default Footer;