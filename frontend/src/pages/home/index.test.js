import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import Home from "./index";
import AppContext from "../../context/appContext";

const setLogged = () => {}
let nextPage = ""
const setNextPage = val => nextPage = val;

jest.mock('react-i18next', () => ({
  useTranslation: () => ({ t: key => key })
}))

describe("home", () => {
  it("render the element", () => {
    const { container } = render(
      <AppContext.Provider value={{ setLogged, nextPage, setNextPage }}>
        <Home />
        </AppContext.Provider>
    );
    expect(screen.getByText(/Header1.P1/)).toBeInTheDocument();
    expect(screen.getByText(/Header1.P2/)).toBeInTheDocument();
    expect(screen.getByText(/Header2/)).toBeInTheDocument();
  })
});