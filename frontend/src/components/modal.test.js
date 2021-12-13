import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import Modal from "./modal";
import AppContext from "../context/appContext";

const setLogged = () => {}
let nextPage = ""
const setNextPage = val => nextPage = val;
let modalShow = true;
const setModalShow = val => modalShow = val;

jest.mock('react-i18next', () => ({
  useTranslation: () => ({ t: key => key })
}))

describe("modal", () => {
  it("render the element", () => {
    const { container } = render(
      <AppContext.Provider value={{ setLogged, nextPage, setNextPage }}>
        <Modal 
          modalShow={true}
          setModalShow={setModalShow}
        />
        </AppContext.Provider>
    );
    expect(screen.getByText(/Title/)).toBeInTheDocument();
    expect(screen.getByText(/LearnMore/)).toBeInTheDocument();
    expect(screen.getByText(/AboutIDVAndSMS/)).toBeInTheDocument();
    expect(screen.getByText(/LoginOauth/)).toBeInTheDocument();
    expect(screen.getByText(/LoginJWT/)).toBeInTheDocument();
    expect(screen.getByText(/Warning/)).toBeInTheDocument();

    const button = screen.getByText(/LoginJWT/);
    button.click();
  })
});