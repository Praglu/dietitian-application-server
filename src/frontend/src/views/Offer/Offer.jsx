import React from 'react';
import { Link } from 'react-router-dom';
import './Offer.scss';
import Breadcrumbs from '/src/components/layout/Breadcrumbs/Breadcrumbs';
import Carousel from '/src/components/layout/Carousel/Carousel';
import Item from '/src/components/layout/Carousel/Item/Item';
import Dialog from '/src/components/layout/Dialog/Dialog';
import { useCart } from '/src/contexts/CartContext';
import { useDialog } from '/src/contexts/DialogContext';
import { useBlog } from '/src/contexts/BlogContext';
import ProductAdd from '/src/components/layout/Dialog/Message/ProductAdd/ProductAdd';

function Offer() {
    const { 
        state: { cart },
        setCart,
        ACTIONS,
        products
    } = useCart();

    const {
        showDialog,
        toggleDialog
    } = useDialog();

    const { posts } = useBlog();
    const anyProducts = products.length > 0;
    const anyBlogPosts = posts.length > 0;
    const addedProduct = cart[cart.length - 1];

    return (
        <main className='offer'>
            <Breadcrumbs />
            { anyProducts &&
                <div className='offer__container'>
                    <ul>
                        {products.map(product => {
                            return (
                                <li key={product.id}>
                                    { product.img &&
                                        <>
                                            <div className='offer__image'>
                                                <img className='offer__icon' src='/src/assets/cart.svg' alt='cart'
                                                    onClick={() => {
                                                        const priceValue = parseInt(product.amount_with_currency.split(' ')[0]);

                                                        setCart({
                                                            type: ACTIONS.ADD_TO_CART,
                                                            payload: {
                                                                id: product.id,
                                                                img: product.img,
                                                                title: product.title,
                                                                price: product.amount_with_currency,
                                                                priceValue: priceValue
                                                            }
                                                        });
                                                
                                                        toggleDialog();
                                                    }} 
                                                />
                                                <img src={product.img} alt='product' />
                                            </div>
                                            <div className='offer__content'>
                                                <h3>{product.title}</h3> 
                                                <h4>{product.amount_with_currency}</h4>
                                                <Link to={`/oferta/${product.id}`}>
                                                    <button className='btn'>
                                                        {'Dowiedz się więcej'}
                                                    </button> 
                                                </Link>
                                            </div>
                                        </>
                                    }
                                </li>
                            );
                        })}
                    </ul>
                </div>
            }
            { anyBlogPosts &&
                <Carousel 
                    data={posts} 
                    Block={Item}
                    page={'blog'}
                    title={'Kolarstwo od kuchni - blog'}
                />
            }
            { showDialog &&
                <Dialog>
                    <ProductAdd product={addedProduct} />
                </Dialog>   
            }
        </main>
    );
}

export default Offer;