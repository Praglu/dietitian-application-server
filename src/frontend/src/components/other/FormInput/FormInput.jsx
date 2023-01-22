import React from 'react';

function FormInput({ id, label, type, register, isChecked, defaultValue, minLength, maxLength, errorMessage }) {
    const checked = isChecked ? isChecked : false;
    
    return (
        <div className='form-input'>
            <label htmlFor={id}>{label}</label>
            <input type={type} id={id} minLength={minLength} maxLength={maxLength} defaultValue={defaultValue} {...register} defaultChecked={checked} required />
            { errorMessage &&
                <span>{errorMessage}</span>
            }
        </div>
    );
}

export default FormInput;