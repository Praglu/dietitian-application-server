import React from 'react';
import './Account.scss';
import AccountCarousel from './AccountCarousel/AccountCarousel';
import { useUser } from '/src/contexts/UserContext';

function Account() {
    const { user } = useUser();
    const token = localStorage.getItem('authToken');

    const logOut = () => {
        fetch(`${import.meta.env.VITE_API_URL}/auth/remove-token`, {
            method: 'POST',
            headers: { 'Authorization': `Token ${token}` }
        })
        .then(response => {
            if (response.ok) {
                localStorage.removeItem('authToken');
                window.location.href = '/panel-klienta';
            }
        })
        .catch(error => console.log('Error: ', error));
    };

    return (
        <div className='account'>
            { user.first_name &&
                <>
                    <h1>{`Witaj ${user.first_name}!`}</h1>
                    <div className='account__content'>
                        <AccountCarousel />
                    </div>
                    <button className='btn' onClick={logOut}>
                        {'Wyloguj'}
                    </button>
                </>
            }
        </div>
    );
}

export default Account;