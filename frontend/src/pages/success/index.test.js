import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import Success from "./index";
import { BrowserRouter } from "react-router-dom";

const setLogged = () => {}
let nextPage = ""
const setNextPage = val => nextPage = val;

jest.mock('react-i18next', () => ({
  useTranslation: () => ({ t: key => key })
}))

describe("hero", () => {
  it("render the element", () => {
    const { container } = render(
      <BrowserRouter>
        <Success 
          location={{"search": "/"}}
        />
      </BrowserRouter>
    );
    expect(screen.getByText(/BackLink/)).toBeInTheDocument();
    expect(screen.getByText(/SandboxText/)).toBeInTheDocument();
    expect(screen.getByText(/SandboxButton/)).toBeInTheDocument();
    expect(screen.getByText(/Description/)).toBeInTheDocument();
  })
});