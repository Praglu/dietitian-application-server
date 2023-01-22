import React from 'react';
import { Link } from 'react-router-dom';

function Links({ hideMobileNav }) {
    return (
        <ul>
            <li>
                <Link to='/' onClick={hideMobileNav}>Home</Link>
            </li>
            <li>
                <Link to='/o-mnie' onClick={hideMobileNav}>O mnie</Link>
            </li>
            <li>
                <Link to='/oferta' onClick={hideMobileNav}>Oferta</Link>
            </li>
            <li>
                <Link to='/blog' onClick={hideMobileNav}>Blog</Link>
            </li>
            <li>
                <Link to='/panel-klienta' onClick={hideMobileNav}>Panel Klienta</Link>
            </li>
            <li>
                <Link to='/koszyk' onClick={hideMobileNav}>Koszyk</Link>
            </li>
        </ul>
    );
}

export default Links;