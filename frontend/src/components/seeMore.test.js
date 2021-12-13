import React from "react";
import { render, unmountComponentAtNode } from "react-dom";
import { act } from "react-dom/test-utils";

import SeeMore from "./seeMore";

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
    render(<SeeMore 
        title="All "
        text="<p>work</p>"
    />, container);
  });
  expect(container.textContent).toBe("All work");
});