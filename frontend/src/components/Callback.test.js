import React from "react";
import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";

import { Callback } from "./Callback";
import AppContext from "../context/appContext";
import { Router } from "react-router-dom";
import { createMemoryHistory } from 'history';

const setLogged = () => {};
const setModalShow = () => {};
const setNextPage = () => {};
const history = createMemoryHistory();

Storage.prototype.getItem = jest.fn(() => 'some string');

describe("Callback", () => {
  it("render the element", () => {
    render(
      <Router history={history}>
        <AppContext.Provider value={{ setLogged, setModalShow, setNextPage }}>
            <Callback />
        </AppContext.Provider>
      </Router>
    );
  })
});