import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import Hero from "./hero";

jest.mock('react-i18next', () => ({
  useTranslation: () => ({ t: key => key })
}))

describe("hero", () => {
  it("render the element", () => {
    const { container } = render(
        <Hero />
    );
    expect(screen.getByText(/Header1.P1/)).toBeInTheDocument();
    expect(screen.getByText(/Header1.P2/)).toBeInTheDocument();
    expect(screen.getByText(/Header2/)).toBeInTheDocument();
  })
});