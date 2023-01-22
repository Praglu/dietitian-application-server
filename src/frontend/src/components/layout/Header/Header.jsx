import React, { useState } from 'react';
import './Header.scss';
import { Link } from 'react-router-dom';
import Logo from '/src/assets/logo.jpg';
import Links from '/src/components/other/Links/Links';
import { AiOutlineClose, AiOutlineMenu } from 'react-icons/ai';
import Overlay from '../Overlay/Overlay';

function Header() {
    const [ isMobileNav, setMobileNav ] = useState(false);

    const hideMobileNav = () => {
        setMobileNav(false);
    };

    return (
        <header className='header'>
            <Link to={'/'}>
                <img className='header__logo' src={Logo} alt='Logo' />
            </Link>
            <nav className='header__nav'>
                <Links />
            </nav>
            <nav className='header__mobile-nav'>
                <AiOutlineMenu className={`${isMobileNav ? 'hidden' : ''}`} onClick={() => { setMobileNav(true) }} />
                <div className={`header__mobile-links ${isMobileNav ? '' : 'hidden'}`}>
                    <AiOutlineClose className={`${isMobileNav ? '' : 'hidden'}`} onClick={() => { setMobileNav(false) }} />
                    <Links hideMobileNav={hideMobileNav} />
                </div>
            </nav>
            { isMobileNav &&
                <Overlay hideOverlay={hideMobileNav} /> 
            }
        </header>
    );
}

export default Header;