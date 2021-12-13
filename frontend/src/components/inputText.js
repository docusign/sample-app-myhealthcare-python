import React, { useState } from "react";

const InputText = props => {
    const [ value, setValue ] = useState("");

    const onChange = event => {
        const val = event.target.value;
        const formError = props.formError;

        setValue(val);
        
        formError[props.formErrorNum] = (!val === true);
        props.setFormError(formError);
    }

    return (
        <div className="form-group">
            <label htmlFor={props.id}>{props.label}</label>
            <input 
                id={props.id}
                className="form-control"
                type="text"
                onChange={onChange}
            />
            {props.submitted && !value && 
                <div className="field-error">{props.errorText}</div>
            }
        </div>
    )
}
export default InputText;