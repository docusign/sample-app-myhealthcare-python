import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";

import BackdropLoader from "./backdropLoader";

describe("backdrop loader", () => {
  test("checks for the absence of the backdrop-enable class", () => {
    const {container} = render(<BackdropLoader backdrop={false}/>);
    expect(container.firstChild).not.toHaveClass("backdrop-enable");
  })

  test("checks for the presence of the class backdrop-enable", () => {
    const {container} = render(<BackdropLoader backdrop={true}/>);
    expect(container.firstChild).toHaveClass("backdrop-enable");
  })
});