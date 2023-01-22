import { useContext, createContext, useReducer, useState, useEffect } from 'react';

const Cart = createContext();

const ACTIONS = {
    ADD_TO_CART: 'add-to-cart',
    REMOVE_FROM_CART: 'remove-from-cart',
    CHANGE_ITEM_QTY: 'change-item-qty',
    CLEAR_CART: 'clear-cart'
};

function CartContext({ children }) {
    const [ products, setProducts ] = useState([]);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}/api/offer/`, {
            method: 'GET'
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            }
        })
        .then(data => {
            if(data) {
                setProducts(data);
            }
        })
        .catch(error => {
            console.log('Error: ', error);
        });
    }, []);

    const reducer = (state, action) => {
        const { payload, operation } = action;

        switch (action.type) {
            case ACTIONS.ADD_TO_CART:
                const itemAlreadyAdded = state.cart.find(item => item.id === payload.id);

                if (itemAlreadyAdded) {
                    return {
                        cart: state.cart.map(item => item.id === payload.id ?
                            {
                                ...item,
                                quantity: item.quantity + 1
                            }
                        :
                            item
                        ),
                        orderSum: state.orderSum + payload.priceValue
                    }
                }

                return {
                    cart: [
                        ...state.cart,
                        {
                            ...payload,
                            quantity: 1
                        }
                    ],
                    orderSum: state.orderSum + payload.priceValue
                };
            case ACTIONS.REMOVE_FROM_CART:
                return {
                    cart: state.cart.filter(item => item.id !== payload.id),
                    orderSum: state.orderSum - payload.priceSum
                };
            case ACTIONS.CHANGE_ITEM_QTY:
                return {
                    cart: state.cart.filter(item => item.id === payload.id ?
                        item.quantity = payload.quantity
                    :
                        item.quantity
                    ),
                    orderSum: operation === '+' ?
                        state.orderSum + payload.priceValue
                    :
                        state.orderSum - payload.priceValue
                };
            case ACTIONS.CLEAR_CART:
                return {
                    cart: [],
                    orderSum: 0
                };
            default:
                return state;
        }
    }

    const initState = {
        cart: [],
        orderSum: 0
    };

    const [ state, setCart ] = useReducer(reducer, initState);

    return (
        <Cart.Provider value={{ state, setCart, ACTIONS, products }}>
            {children}
        </Cart.Provider>
    );
}

export default CartContext;

export const useCart = () => {
    return useContext(Cart);
}