import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import './Order.scss';

function Order() {
    const { id } = useParams();
    const [ order, setOrder ] = useState({});
    const [ products, setProducts ] = useState([]);
    const token = localStorage.getItem('authToken');

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}/api/order/${id}/`, {
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
                setOrder(data);
                setProducts(data.products);
            }
        })
        .catch(error => {
            console.log('Error: ', error);
        });
    }, []);

    return (
        <main className='order'>
            { token ?
                <div className='order__content'>
                    <h1>{`Zamówienie id: ${id}`}</h1>
                    <div className='order__products'>
                        <h2>{'Produkty'}</h2>
                        <ul>
                            {products.map(product => {
                                return (
                                    <li key={product.id}>
                                        <Link to={`/oferta/${product.id}`}>
                                            <div className='order__product-img'>
                                                <img src={product.img} alt='product' />
                                            </div>
                                            <div className='order__product-info'>
                                                <h4>{product.title}</h4>
                                                <h4>{'Cena: '}{product.amount}{' PLN'}</h4>
                                                <h4>{'Ilość: '}{product.quantity}</h4>
                                            </div>
                                        </Link>
                                    </li>
                                );
                            })}
                        </ul>
                    </div>
                    <div className='order__info'>
                        <h2>{'Szczegóły'}</h2>
                        <div className="order__wrapper">
                            <div className='order__column'>
                                <h4>{'Dane'}</h4>
                                <p>{order.first_name}{' '}{order.last_name}</p>
                                <p>{order.street}{' '}{order.house_number}</p>
                                <p>{order.post_code}{' '}{order.city}</p>
                                <p>{order.email}</p>
                                <p>{order.phone}</p>
                            </div>
                            <div className='order__column'>
                                <h4>{'Informacje dodatkowe'}</h4>
                                <p>{order.additional_info}</p>
                            </div>
                            <div className='order__column'>
                                <h4>{'Sposób płatności'}</h4>
                                <p>{order.payment_method}</p>
                            </div>
                            <div className='order__column'>
                                <h4>{'Suma'}</h4>
                                <p>{order.sum}{' PLN'}</p>
                            </div>
                        </div>
                    </div>
                    <div className='order__buttons'>
                        <Link to={'/panel-klienta'}>
                            <button className='btn'>
                                {'Panel klienta'}
                            </button>
                        </Link>
                    </div>
                </div>
            :
                <div className='order__error'>
                    <h2>{'Najpierw musisz się zalogować !'}</h2>
                    <Link to={'/panel-klienta'}>
                        <button className='btn'>
                            {'Logowanie'}
                        </button>
                    </Link>
                </div>
            }
        </main>
    );
}

export default Order;