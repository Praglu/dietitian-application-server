import React from 'react';
import './ContactBlock.scss';
import { FaRegCopy } from 'react-icons/fa';
import ContactForm from '/src/views/Contact/ContactForm/ContactForm';

const copyToClipboard = e => {
    const parentElement = e.target.parentElement;
    
    navigator.clipboard.writeText(parentElement.innerText);

    if (!parentElement.className) {
        parentElement.className = 'active';
    }

    setTimeout(() => {
        parentElement.className = '';
    }, 700);
};

function ContactBlock({ data }) {
    return (
        <div className='contact-block'>
            <div className='contact-block__content'> 
                <h2>{data.title}</h2> 
                <h3>{data.subtitle}</h3>
                <div className='contact-block__info'>
                    <ul>
                        <li>
                            <img className='contact-block__icon' src='/src/assets/email.svg' alt='Email' />
                            {'kolarstwoodkuchni@gmail.com'}
                            <FaRegCopy onClick={copyToClipboard} />
                        </li>
                        <li>
                            <img className='contact-block__icon' src='/src/assets/phone.svg' alt='Phone' />
                            {'+48 515035890'}
                            <FaRegCopy onClick={copyToClipboard} />
                        </li>
                    </ul>
                </div>
            </div>
            { data.img ?
                <div className='contact-block__image'>
                    <img src={data.img} alt='contact' />
                </div>
            :
                <ContactForm />
            }
        </div>
    );
}

export default ContactBlock;