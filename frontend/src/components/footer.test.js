import React from "react";
import { render, unmountComponentAtNode } from "react-dom";
import { act } from "react-dom/test-utils";
import { useTranslation } from "react-i18next";

import Footer from "./footer";

jest.mock('react-i18next', () => ({
  useTranslation: () => ({ t: key => key })
}));

const { t } = useTranslation("Common");

let container = null;
beforeEach(() => {
  container = document.createElement("div");
  document.body.appendChild(container);
});

afterEach(() => {
  unmountComponentAtNode(container);
  container.remove();
  container = null;
});

it("renders component", () => {
  act(() => {
    render(<Footer />, container);
  });
  expect(container.textContent).toBe(t("Copyright"));
});