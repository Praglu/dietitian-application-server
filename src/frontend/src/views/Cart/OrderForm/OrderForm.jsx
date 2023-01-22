import React from 'react';
import './OrderForm.scss';
import { useForm } from 'react-hook-form';
import { useUser } from '/src/contexts/UserContext';
import FormInput from '/src/components/other/FormInput/FormInput';

function OrderForm({ next, back, orderForm, setOrderForm, errors }) {
    const { user } = useUser();
    const { handleSubmit, register } = useForm();

    const formValues = {
        first_name: user.first_name ? user.first_name : orderForm?.first_name,
        last_name: user.last_name ? user.last_name : orderForm?.last_name,
        street: user.street ? user.street : orderForm?.street,
        house_number: user.house_number ? user.house_number : orderForm?.house_number,
        post_code: user.post_code ? user.post_code : orderForm?.post_code,
        city: user.city ? user.city : orderForm?.city,
        email: user.email ? user.email : orderForm?.email,
        phone: user.phone ? user.phone : orderForm?.phone,
        are_service_terms_approved: orderForm?.are_service_terms_approved,
        info: orderForm?.info
    };

    const prepareOrder = data => {
        setOrderForm(data);
        next();
    };

    return (
        <form className='order-form' onSubmit={handleSubmit(data => prepareOrder(data))}>
            <div className='order-form__container'>
                <div className="order-form__first">
                    <FormInput id={'first_name'} label={'Imię *'} type={'text'} maxLength={50} register={{...register('first_name')}} errorMessage={errors?.first_name} defaultValue={formValues.first_name} />
                    <FormInput id={'last_name'} label={'Nazwisko *'} type={'text'} maxLength={50} register={{...register('last_name')}} errorMessage={errors?.last_name} defaultValue={formValues.last_name} />
                    <div className='form-group'>
                        <div className='form-element'>
                            <FormInput id={'street'} label={'Ulica *'} type={'text'} maxLength={50} register={{...register('street')}} errorMessage={errors?.street} defaultValue={formValues.street} />
                        </div>
                        <div className='form-element'>
                            <FormInput id={'house_number'} label={'Numer budynku *'} type={'text'} maxLength={4} register={{...register('house_number')}} errorMessage={errors?.house_number} defaultValue={formValues.house_number} />
                        </div>
                    </div>
                    <div className='form-group'>
                        <div className='form-element'>
                            <FormInput id={'post_code'} label={'Kod pocztowy *'} type={'text'} maxLength={6} register={{...register('post_code')}} errorMessage={errors?.post_code} defaultValue={formValues.post_code} />
                        </div>
                        <div className='form-element'>
                            <FormInput id={'city'} label={'Miasto *'} type={'text'} maxLength={30} register={{...register('city')}} errorMessage={errors?.city} defaultValue={formValues.city} />
                        </div>
                    </div>
                    <FormInput id={'email'} label={'Email *'} type={'text'} maxLength={100} register={{...register('email')}} errorMessage={errors?.email} defaultValue={formValues.email} />
                    <FormInput id={'phone'} label={'Numer telefonu *'} type={'text'} minLength={9} maxLength={9} register={{...register('phone')}} errorMessage={errors?.phone} defaultValue={formValues.phone} />
                </div>
                <div className="order-form__second">
                    <div className='order-form__block'>
                        <h2>{'Wybierz sposób płatności'}</h2>
                        <div className='order-form__wrapper'>
                            <label htmlFor='payment_method'>{'Przelew tradycyjny'}</label>
                            <input {...register('payment_method')} type='checkbox' name='payment_method' value='Przelew tradycyjny' required defaultChecked />
                        </div>
                    </div>
                    <div className='order-form__block'>
                        <h2>{'Informacje dodatkowe'}</h2>
                        <textarea {...register('info')} defaultValue={formValues.info} maxLength={300} />
                    </div>
                </div>
            </div>
            <div className='order-form__check'>
                <p>{'Twoje dane osobowe będą użyte do przetworzenia zamówienia, ułatwienia korzystania ze strony internetowej oraz innych celów opisanych w polityka prywatności.'}</p>
                <FormInput id={'are_service_terms_approved'} label={'Przeczytałem/am i akceptuję regulamin *'} type={'checkbox'} register={{...register('are_service_terms_approved')}} isChecked={formValues.are_service_terms_approved} />
            </div>
            <div className='order-form__info'>
                {'* pola wymagane'}
            </div>
            <div className='order-form__buttons'>
                <button className='btn' onClick={back}>
                    {'< Koszyk'}
                </button>
                <button className='btn' type='submit'>
                    {'Podsumowanie >'}
                </button>
            </div>
        </form>
    );
}

export default OrderForm;