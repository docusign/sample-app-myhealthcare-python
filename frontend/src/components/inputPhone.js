import React, { useState } from "react";

const InputPhone = props => {
    const [ countryValue, setCountryValue ] = useState("");
    const [ phoneValue, setPhoneValue ] = useState("");

    const validatePhone = (phone) => /^(\d+-?)+\d+$/.test(phone);
    const validateCountry = (country) => /^([+]?\d+)$/.test(country)

    const onChangeCountry = event => {
        const val = event.target.value;
        const formError = props.formError;

        setCountryValue(val);

        formError[props.formErrorNum] = (!validateCountry(val) || !validatePhone(phoneValue));
        props.setFormError(formError);
    }

    const onChangePhone = event => {
        const val = event.target.value;
        const formError = props.formError;

        setPhoneValue(val);

        formError[props.formErrorNum] = (!validatePhone(val) || !validateCountry(countryValue));
        props.setFormError(formError);
    }

    const getErrorText = () => {
        if (props.submitted) {
            if (!countryValue && !phoneValue) {
                return <div className="field-error">{props.errorText}</div>;
            }
            else if (!validateCountry(countryValue) || !validatePhone(phoneValue)) {
                return <div className="field-error">{props.errorTextInv}</div>;
            }
            else {
                return false;
            }
        }
    }

    return (
        <div className="form-group phone-number">
            <label htmlFor={props.id}>{props.label}</label>
            <div>
                <input
                    id="CountryCode"
                    className="form-control"
                    type="text"
                    placeholder="+1"
                    onChange={onChangeCountry}
                />
                <input
                    id="PhoneNumber"
                    className="form-control"
                    type="text"
                    placeholder="415-555-1212"
                    onChange={onChangePhone}
                />
            </div>
            {getErrorText()}
        </div>
    )
}
export default InputPhone;