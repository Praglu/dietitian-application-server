import React from 'react';
import './Summary.scss';
import { useNavigate, Link } from 'react-router-dom';
import { useCart } from '/src/contexts/CartContext';
import { useDialog } from '/src/contexts/DialogContext';
import { useLoading } from '/src/contexts/LoadingContext';

function Summary({ next, back, orderForm, setErrors }) {
    const additional_info = orderForm.info.length > 0 ? orderForm.info : 'Brak';

    const navigate = useNavigate();
    const { setError } = useDialog();
    const { setLoading } = useLoading();

    const { 
        state: {
            cart,
            orderSum
        },
        setCart, 
        ACTIONS
    } = useCart();

    const finishOrder = () => {
        setLoading(true);

        const products = [];

        cart.forEach(product => {
            const { id, quantity } = product;

            products.push({ id, quantity });
        });

        const data = {
            first_name: orderForm.first_name,
            last_name: orderForm.last_name,
            street: orderForm.street,
            house_number: orderForm.house_number,
            post_code: orderForm.post_code,
            city: orderForm.city,
            email: orderForm.email,
            phone: orderForm.phone,
            are_service_terms_accepted: orderForm.are_service_terms_approved,
            payment_method: orderForm.payment_method,
            additional_info: additional_info,
            products: products,
            sum: orderSum
        };
        
        fetch(`${import.meta.env.VITE_API_URL}/api/order/make-order`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {
                setLoading(false);
                setCart({ type: ACTIONS.CLEAR_CART });
                next();
            } else {
                return response.json();
            }
        })
        .then(data => {
            if (data) {
                setLoading(false);
                setErrors(data.invalid_fields);
                back();
            }
        })
        .catch(error => {
            setCart({ type: ACTIONS.CLEAR_CART });
            console.log('Error: ', error);
            setError('Nieudane połączenie z serwerem');
            navigate('/oferta');
        });
    };

    return (
        <>
            <div className='summary'>
                <div className='summary__products'>
                    <h2>{'Produkty'}</h2>
                    <ul>
                        {cart.map(product => {
                            return (
                                <li key={product.id}>
                                    <Link to={`/oferta/${product.id}`}>
                                        <div className='summary__product-img'>
                                            <img src={product.img} alt='product' />
                                        </div>
                                        <div className='summary__product-info'>
                                            <h4>{product.title}</h4>
                                            <h4>{product.price}</h4>
                                            <h4>{'Ilość: '}{product.quantity}</h4>
                                        </div>
                                    </Link>
                                </li>
                            );
                        })}
                    </ul>
                </div>
                <div className='summary__order'>
                    <h2>{'Szczegóły'}</h2>
                    <div className='summary__info'>
                        <div className='summary__column'>
                            <h4>{'Dane'}</h4>
                            <p>{orderForm.first_name}{' '}{orderForm.last_name}</p>
                            <p>{orderForm.street}{' '}{orderForm.house_number}</p>
                            <p>{orderForm.post_code}{' '}{orderForm.city}</p>
                            <p>{orderForm.email}</p>
                            <p>{orderForm.phone}</p>
                        </div>
                        <div className='summary__column'>
                            <h4>{'Informacje dodatkowe'}</h4>
                            <p>{additional_info}</p>
                        </div>
                        <div className='summary__column'>
                            <h4>{'Sposób płatności'}</h4>
                            <p>{orderForm.payment_method}</p>
                        </div>
                        <div className='summary__column'>
                            <h4>{'Suma'}</h4>
                            <p>{orderSum}{' PLN'}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className='cart__buttons'>
                <button className='btn' onClick={back}>
                    {'< Moje dane'}
                </button>
                <button className='btn' onClick={finishOrder}>
                    {'Zatwierdź >'}
                </button>
            </div>
        </>
    );
}

export default Summary;