import React from 'react';
import { Link } from 'react-router-dom';
import './Confirm.scss';
import Logo from '/src/assets/logo.jpg';

function Confirm() {
    return (
        <div className='confirm'>
            <h1>{'Dziękujemy !'}</h1>
            <h4>{'Twoje zamówienie zostało przyjęte do realizacji.'}</h4>
            <div className='confirm__image'>
                <img src={Logo} alt='logo' />
            </div>
            <Link to={'/'}>
                <button className="btn">
                    {'Powrót'}
                </button>
            </Link>
        </div>
    );
}

export default Confirm;