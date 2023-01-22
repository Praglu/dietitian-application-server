import React from 'react';
import './ProductTable.scss';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { AiOutlineClose } from 'react-icons/ai';
import { useCart } from '/src/contexts/CartContext';
import ButtonGroup from '@mui/material/ButtonGroup';
import Button from '@mui/material/Button';

function ProductTable() {
    const {
        state: {
            cart,
            orderSum
        },
        setCart,
        ACTIONS
    } = useCart();

    return (
        <TableContainer className='product-table'>
            <Table sx={{ minWidth: 650 }} aria-label="products table">
                <TableHead>
                    <TableRow>
                        <TableCell align='center'>{'Produkt'}</TableCell>
                        <TableCell align='center'>{'Cena'}</TableCell>
                        <TableCell align='center'>{'Ilość'}</TableCell>
                        <TableCell align='center'>{'Suma'}</TableCell>
                        <TableCell align='center'>{'Usuń'}</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {cart.map(item => {
                        const priceSum = item.priceValue * item.quantity;

                        return (
                            <TableRow key={item.id}>
                                <TableCell>
                                    <div className='product-table__item'>
                                        <div className='product-table__img'>
                                            <img src={item.img} alt='product' />
                                        </div>
                                        <div className='product-table__title'>
                                            {item.title}
                                        </div>
                                    </div>
                                </TableCell>
                                <TableCell align='center'>{item.price}</TableCell>
                                <TableCell align='center'>
                                    <ButtonGroup color='info'>
                                        <Button onClick={() => {
                                            const quantity = item.quantity + 1;

                                            setCart({
                                                type: ACTIONS.CHANGE_ITEM_QTY,
                                                payload: {
                                                    id: item.id,
                                                    quantity: quantity,
                                                    priceValue: item.priceValue
                                                },
                                                operation: '+'
                                            });
                                        }}>{'+'}</Button>
                                        <Button color='success' disabled>{item.quantity}</Button>
                                        <Button onClick={() => {
                                            const quantity = item.quantity === 0 ? 0 : item.quantity - 1;

                                            setCart({
                                                type: ACTIONS.CHANGE_ITEM_QTY,
                                                payload: {
                                                    id: item.id,
                                                    quantity: quantity,
                                                    priceValue: item.priceValue
                                                },
                                                operation: '-'
                                            });
                                        }}>{'-'}</Button>
                                    </ButtonGroup>
                                </TableCell>
                                <TableCell align='center'>{priceSum}{' PLN'}</TableCell>
                                <TableCell align='center'>
                                    <AiOutlineClose 
                                        onClick={() => {
                                            setCart({
                                                type: ACTIONS.REMOVE_FROM_CART,
                                                payload: { 
                                                    id: item.id,
                                                    priceSum: priceSum
                                                }
                                            });
                                        }} 
                                    />
                                </TableCell>
                            </TableRow>
                        );
                    })}
                    <TableRow>
                        <TableCell />
                        <TableCell />
                        <TableCell />
                        <TableCell align='center'>
                            <b>{'Całość: '}</b>
                            {orderSum}{' PLN'}
                        </TableCell>
                        <TableCell />
                    </TableRow>
                </TableBody>
            </Table>
        </TableContainer>
    );
}

export default ProductTable;