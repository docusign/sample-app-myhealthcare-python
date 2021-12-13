import React from "react";
import Card from "../../components/card";
import { useTranslation } from "react-i18next";
import Hero from "./hero";
import PreFooter from "./preFooter";
import img1 from "../../assets/img/ic-records.svg";
import img2 from "../../assets/img/ic-covid.svg";
import img3 from "../../assets/img/ic-patient.svg";

const Home = () => {
  const { t } = useTranslation("Home")
  return (
    <>
      <Hero />

      <section className="card-info-holder">
        <div className="container-fluid">
          <div className="row justify-content-center text-center d-flex flex-row">

            <Card
              additionalClass="card-1"
              img={img1}
              title={t("Card1.Title")}
              linkTo="/request-medical-records"
              getStarted={t("Card1.Button")}
              featureTitle={t("Card1.FeaturesTitle")}
              featureList={t("Card1.FeaturesList")}
            />

            <div className="w-100 d-block d-md-none"></div>

            <Card
              additionalClass="card-2"
              img={img2}
              title={t("Card2.Title")}
              linkTo="/covid19-consent-form"
              getStarted={t("Card2.Button")}
              featureTitle={t("Card2.FeaturesTitle")}
              featureList={t("Card2.FeaturesList")}
            />

            <div className="w-100 d-block d-md-none"></div>

            <Card
              additionalClass="card-3"
              img={img3}
              title={t("Card3.Title")}
              linkTo="/apply-for-patient-assistance"
              getStarted={t("Card3.Button")}
              featureTitle={t("Card3.FeaturesTitle")}
              featureList={t("Card3.FeaturesList")}
            />

          </div>
        </div>
      </section>

      <PreFooter />
    </>
  );
}
export default Home;