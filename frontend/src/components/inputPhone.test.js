import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";

import InputPhone from "./inputPhone";

describe("Input phone group", () => {
    test("rendering input phone group components", () => {
        render(<InputPhone 
            id={"CountryCode"}
            label={"test-label"}
            errorText={"test-error"}
            submitted={true}
        />);
        expect(screen.getByLabelText(/test-label/i)).toBeInTheDocument();
        expect(screen.queryByText(/test-error/)).toBeInTheDocument()
    });
});

describe("events", () => {
    it("checking the data entry into the component Input phone", () => {
        const { container } = render(<InputPhone 
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

        const input2 = container.getElementsByClassName("form-control")[1]

        expect(input2).toBeInTheDocument()
        expect(input2).not.toHaveFocus();
        input2.focus();
        expect(input2).toHaveFocus();

        fireEvent.change(input2, { target: { value: 'test-value' } })
        expect(input2).toHaveValue('test-value')
    });
});