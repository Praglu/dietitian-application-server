import React, { useState } from 'react';
import './AccountSettings.scss';
import { useForm } from 'react-hook-form';
import { useDialog } from '/src/contexts/DialogContext';
import { useUser } from '/src/contexts/UserContext';
import FormInput from '/src/components/other/FormInput/FormInput';

function AccountSettings() {
    const [ edit, setEdit ] = useState(false);
    const { user } = useUser();
    const { register, handleSubmit } = useForm();

    const toggleEdit = () => {
        setEdit(!edit);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    return (
        <div className='account-settings'>
            <h2>{'Ustawienia konta'}</h2>
            <div className="account-settings__content">
                { edit ?
                    <div className='account-settings__edit'>
                        <form className='account-settings__form' onSubmit={handleSubmit(data => console.log(data))}>
                            <FormInput id={'first_name'} label={'Imię *'} type={'text'} maxLength={50} register={{...register('first_name')}} defaultValue={user.first_name} />
                            <FormInput id={'last_name'} label={'Nazwisko *'} type={'text'} maxLength={50} register={{...register('last_name')}} defaultValue={user.last_name} />
                            <div className='form-group'>
                                <div className='form-element'>
                                    <FormInput id={'street'} label={'Ulica *'} type={'text'} maxLength={50} register={{...register('street')}} defaultValue={user.street} />
                                </div>
                                <div className='form-element'>
                                    <FormInput id={'house_number'} label={'Numer budynku *'} type={'text'} maxLength={4} register={{...register('house_number')}} defaultValue={user.house_number} />
                                </div>
                            </div>
                            <div className='form-group'>
                                <div className='form-element'>
                                    <FormInput id={'post_code'} label={'Kod pocztowy *'} type={'text'} maxLength={6} register={{...register('post_code')}} defaultValue={user.post_code} />
                                </div>
                                <div className='form-element'>
                                    <FormInput id={'city'} label={'Miasto *'} type={'text'} maxLength={30} register={{...register('city')}} defaultValue={user.city} />
                                </div>
                            </div>
                            <FormInput id={'email'} label={'Email *'} type={'text'} maxLength={100} register={{...register('email')}} defaultValue={user.email} />
                            <FormInput id={'phone'} label={'Numer telefonu *'} type={'text'} minLength={9} maxLength={9} register={{...register('phone')}} defaultValue={user.phone} />
                            <div className='form-info'>
                                <h3>{'Hasło musi zawierać:'}</h3>
                                {'• min. 8 znaków • mała litera • wielka litera • cyfra •'}
                            </div>
                            <FormInput id={'password'} label={'Hasło *'} type={'password'} minLength={8} maxLength={50} register={{...register('password')}} />
                            <FormInput id={'password_repeat'} label={'Powtórz hasło *'} type={'password'} minLength={8} maxLength={50} register={{...register('password_repeat')}} />
                        </form>
                        <div className='account-settings__buttons'>
                            <button className='btn btn--transparent' onClick={toggleEdit}>
                                {'Anuluj'}
                            </button>
                            <button className='btn btn--transparent'>
                                {'Zatwierdź'}
                            </button>
                        </div>
                    </div>
                :
                    <>
                        <button className='btn btn--transparent' onClick={toggleEdit}>
                            {'Edytuj swoje dane'}
                        </button>
                        <button className='btn btn--transparent'>
                            {'Usuń konto'}
                        </button>
                    </>
                }
            </div>
        </div>
    );
}

export default AccountSettings;