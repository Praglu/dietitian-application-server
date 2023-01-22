import React from 'react';
import './Hero.scss';
import { Link } from 'react-router-dom';

function Hero({ data }) {
    return (
        <div className='hero'>
            <div className='hero__content'>
                { data.title &&
                    <h1 className='hero__title'>
                        {data.title}
                    </h1>
                }
                { data.subtitle &&
                    <h2 className='hero__sub-title'>
                        {data.subtitle}
                    </h2>
                }
                { data.logo && 
                    <img className='hero__logo' src={data.logo} alt='Logo' />
                }
                { data.buttonText && data.buttonLink && 
                    <Link to={data.buttonLink}>
                        <button className='btn'>
                            {data.buttonText}
                        </button>
                    </Link>
                }
            </div>
            { data.img && 
                <div className='hero__image'>
                    <img src={data.img} alt='hero' />
                </div>
            }
        </div>
    );
}

export default Hero;