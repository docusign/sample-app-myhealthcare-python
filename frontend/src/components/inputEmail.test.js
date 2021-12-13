import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import InputEmail from "./inputEmail";

describe("Input group", () => {
    test("rendering input group components", () => {
        render(<InputEmail 
            id={"test"}
            label={"test-label"}
            errorText={"test-error"}
            submitted={true}
        />);
        expect(screen.getByLabelText(/test-label/i)).toBeInTheDocument();
        expect(screen.queryByText(/test-error/)).toBeInTheDocument()
    });
});

describe("events", () => {
    it("checking the data entry into the component Input", () => {
        const { container } = render(<InputEmail 
            id={"test-events"}
            label={"test-events-label"}
            errorText={"test-events-error"}
            submitted={true}
            formError={[1]}
            formErrorNum={0}
            setFormError={val => {}}
        />);

        const input = container.getElementsByClassName("form-control")[0]

        expect(input).toBeInTheDocument()
        expect(input).not.toHaveFocus();
        input.focus();
        expect(input).toHaveFocus();

        fireEvent.change(input, { target: { value: 'test-value' } })
        expect(input).toHaveValue('test-value')
    });
});