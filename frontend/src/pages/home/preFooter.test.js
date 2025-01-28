import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import PreFooter from "./preFooter";

jest.mock('react-i18next', () => ({
  useTranslation: () => ({ t: key => key })
}))

describe("pre footer", () => {
  it("render the element", () => {
    const { container } = render(
        <PreFooter />
    );
    expect(screen.getByText(/GetFreeLinkName/)).toBeInTheDocument();
    expect(screen.getByText(/PythonSDKLinkName/)).toBeInTheDocument();
  })
});