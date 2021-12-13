import React, { useState } from "react";

const InputEmail = props => {
    const [ valid, setValid ] = useState(false);

    const validateEmail = email => {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

    const onChange = event => {
        const validated = validateEmail(event.target.value);
        const formError = props.formError;

        setValid(validated);

        formError[props.formErrorNum] = !validated;
        props.setFormError(formError);
    }

    return (
        <div className="form-group last-form-group">
            <label htmlFor={props.id}>{props.label}</label>
            <input 
                id={props.id}
                className="form-control"
                type="text"
                onChange={onChange} 
            />
            {props.submitted && !valid && 
                <div className="field-error">{props.errorText}</div>
            }
        </div>
    )
}
export default InputEmail;