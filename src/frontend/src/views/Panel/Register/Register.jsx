import React from 'react';
import RegisterForm from '/src/views/Panel/Register/RegisterForm/RegisterForm';

function Register({ hideRegister }) {
    return (
        <div className='panel__block panel__block--register'>
            <RegisterForm hideRegister={hideRegister} />
        </div>
    );
}

export default Register;