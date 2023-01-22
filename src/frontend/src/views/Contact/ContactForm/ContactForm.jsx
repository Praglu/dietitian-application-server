import React, { useState } from 'react';
import './ContactForm.scss';
import { useForm } from 'react-hook-form';
import { useDialog } from '/src/contexts/DialogContext';
import { useLoading } from '/src/contexts/LoadingContext';
import FormInput from '/src/components/other/FormInput/FormInput';

function ContactForm() {
    const [ errors, setErrors ] = useState({});
    const { setLoading } = useLoading();
    const { 
        setError,
        toggleDialog
    } = useDialog();
    const { register, handleSubmit } = useForm();

    const sendMail = (data) => {
        setLoading(true);
    
        fetch(`${import.meta.env.VITE_API_URL}/api/contact-form`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                setLoading(false);
                toggleDialog();
            } else {
                return response.json();
            }
        })
        .then(data => {
            if (data) {
                setLoading(false);
                setErrors(data.invalid_fields);
            }
        })
        .catch(error => {
            console.log('Error: ', error);
            setError('Nieudane połączenie z serwerem');
        });
    };

    return (
        <form className='contact-form' onSubmit={handleSubmit(data => sendMail(data))}>
            <FormInput id={'first_and_last_name'} label={'Imię i Nazwisko *'} type={'text'} maxLength={100} register={{...register('first_and_last_name')}} errorMessage={errors?.first_and_last_name} />
            <FormInput id={'email'} label={'Twój Email *'} type={'text'} maxLength={100} register={{...register('email')}} errorMessage={errors?.email} />
            <FormInput id={'phone'} label={'Numer telefonu *'} type={'text'} minLength={9} maxLength={9} register={{...register('phone')}} errorMessage={errors?.phone} />
            <label htmlFor='message'>{'Wiadomość *'}</label>
            <textarea {...register('message')} name='message' maxLength={300} placeholder={'Treść wiadomości...'} required />
            <button className='btn' type='submit'>
                {'Wyślij'}
            </button>
        </form>
    );
}

export default ContactForm;