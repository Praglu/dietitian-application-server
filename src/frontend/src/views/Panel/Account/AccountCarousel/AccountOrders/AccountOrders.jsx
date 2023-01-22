import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './AccountOrders.scss';

function AccountOrders() {
    const [ orders, setOrders ] = useState([]);
    const token = localStorage.getItem('authToken');

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}/api/order/`, {
            method: 'GET',
            headers: { 'Authorization': `Token ${token}` }
        })
        .then(response => {
            if(response.ok) {
                return response.json();   
            }
        })
        .then(data => {
            if (data) {
                setOrders(data);
            }
        })
        .catch(error => {
            console.log('Error: ', error);
        });
    }, []);
    
    return (
        <div className='account-orders'>
            <h2>{'Twoje zamówienia'}</h2>
            <div className='account-orders__content'>
                <ul>
                    {orders.map(order => {
                        return (
                            <li key={order.id}>
                                <Link to={`/zamowienie/${order.id}`}>
                                    {`Zamówienie id: ${order.id}`}
                                </Link>
                            </li>
                        );
                    })}
                </ul>
            </div>
        </div>
    );
}

export default AccountOrders;