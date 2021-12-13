import i18n from "i18next";
import Backend from "i18next-xhr-backend";
import { initReactI18next } from "react-i18next";

i18n
  .use(Backend)
  .use(initReactI18next)
  .init({
    fallbackLng: "en",
    debug: false,
    ns: [
      "About",
      "Common",
      "History",
      "Home",
      "Modal",
      "RequestMedicalRecords",
      "Covid19ConsentForm",
      "ApplyForPatientAssistance",
      "Success"
    ],
    transKeepBasicHtmlNodesFor: ["h3", "h4", "strong", "i", "p"],
    keySeparator: ".",
    interpolation: {
      escapeValue: false,
      formatSeparator: ","
    },
    react: {
      wait: true
    }
  });
export default i18n;