import React from 'react';
import { Link } from 'react-router-dom';
import './LoginForm.scss';
import { useForm } from 'react-hook-form';
import { useDialog } from '/src/contexts/DialogContext';
import { useLoading } from '/src/contexts/LoadingContext';
import FormInput from '/src/components/other/FormInput/FormInput';

function LoginForm() {
    const { setError } = useDialog();
    const { setLoading } = useLoading();
    const { register, handleSubmit } = useForm();

    const authenticateUser = data => {
        setLoading(true);

        fetch(`${import.meta.env.VITE_API_URL}/auth/obtain-token`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            if (data.invalid_fields) {
                setLoading(false);
                setError('Niepoprawny email lub hasło');
            } else if (data.token) {
                localStorage.setItem('authToken', data.token);
                window.location.href = '/panel-klienta';
            }
        })
        .catch(error => {
            setLoading(false);
            console.log('Error: ', error);
            setError('Nieudane połączenie z serwerem');
        });
    };

    return (
        <form className='login-form' onSubmit={handleSubmit(data => authenticateUser(data))}>
            <div className='login-form__wrapper'>
                <h2>{'Logowanie'}</h2>
                <FormInput id={'username'} label={'Email'} type={'text'} maxLength={100} register={{...register('username')}} />
                <FormInput id={'password'} label={'Hasło'} type={'password'} minLength={8} maxLength={50} register={{...register('password')}} />
                <Link to={'#'}>
                    {'Przypomnij hasło'}
                </Link>
            </div>
            <div className='login-form__button'>
                <button className='btn' type='submit'>
                    {'Zaloguj się'}
                </button>
            </div>
        </form>
    );
}

export default LoginForm;