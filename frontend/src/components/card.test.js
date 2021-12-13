import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import Card from "./card";
import AppContext from "../context/appContext";
import { BrowserRouter } from "react-router-dom";

const setModalShow = () => {}
const logged = false;
let nextPage = "";
const setNextPage = (val) => { nextPage = val }

describe("card", () => {
  it("render the element", () => {
    const { container } = render(
    <BrowserRouter>
        <AppContext.Provider value={{ setModalShow, logged, setNextPage}}>
            <Card
                additionalClass={"testAdditionalClass"}
                img={"testImg"}
                title={"testTitle"}
                getStarted={"testGetStarted"}
                linkTo={"testURL"}
                featureTitle={"testFeatureTitle"} 
                featureList={"<p>TestFeatureList</p>"}
            />
        </AppContext.Provider>
    </BrowserRouter>
    );
    expect(container.firstChild).toHaveClass("testAdditionalClass");
    expect(screen.getByText(/testTitle/)).toBeInTheDocument();
    expect(screen.getByText(/testGetStarted/)).toBeInTheDocument();
    expect(screen.getByText(/testFeatureTitle/)).toBeInTheDocument();
    expect(screen.getByText(/TestFeatureList/)).toBeInTheDocument();

    const button = container.getElementsByClassName('h-card-button')[0];
    button.click();

    expect(nextPage).toBe("testURL")
  })
});