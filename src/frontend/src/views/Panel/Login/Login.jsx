import React from 'react';
import LoginForm from '/src/views/Panel/Login/LoginForm/LoginForm';

function Login({ showRegister }) {
    const checkIcon = <img src='/src/assets/check-circle.svg' alt='check' />;

    return (
        <>
            <div className='panel__block'>
                <LoginForm />
            </div>
            <div className='panel__block'>
                <div className='panel__wrapper'>
                    <h2>{'Nowy klient'}</h2>
                    <div className='panel__subtitle'>
                        {'Załóż konto i zyskaj dostęp do:'}
                    </div>
                    <ul>
                        <li>{checkIcon}{'Szybkiego zakupu jadłospisu'}</li>
                        <li>{checkIcon}{'Szybkiego umówienia się na konsultację'}</li>
                        <li>{checkIcon}{'Pełnej historii dietoterapii'}</li>
                    </ul>
                </div>
                <div className='panel__button'>
                    <button className='btn' onClick={showRegister}>
                        {'Zarejestruj się'}
                    </button>
                </div>
            </div>
        </>
    );
}

export default Login;