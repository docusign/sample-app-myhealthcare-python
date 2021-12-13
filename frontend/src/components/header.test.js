import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import Header from "./header";
import AppContext from "../context/appContext";
import { BrowserRouter } from "react-router-dom";

const setModalShow = () => {}
let logged = false;
const setLogged = (val) => { logged = val }

jest.mock('react-i18next', () => ({
  useTranslation: () => ({ t: key => key })
}))

describe("header", () => {
  it("render the element", () => {
    const { container } = render(
    <BrowserRouter>
        <AppContext.Provider value={{ setModalShow, logged, setLogged }}>
            <Header />
        </AppContext.Provider>
    </BrowserRouter>
    );
    expect(screen.getByText(/GitHubLinkText/)).toBeInTheDocument();
    expect(screen.getByText(/LogInText/)).toBeInTheDocument();

    const button = container.getElementsByClassName('login-btn')[0];
    button.click();
  })
});