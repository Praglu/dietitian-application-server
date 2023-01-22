import React from 'react';
import { Link } from 'react-router-dom';
import './ContentBlock.scss';

function ContentBlock({ data }) {
    return (
        <div className='content'>
            {data.map((item, index) => {
                const buttonLink = item.button_link ? item.button_link : '#';
                const isBlockEven = ++index % 2 == 0;

                return (
                    <div key={item.id} className={`content__block ${isBlockEven ? 'content__block--reverse' : ''}`}>
                        { item.img &&
                            <>
                                <div className={`content__image ${isBlockEven ? 'content__image--reverse' : ''}`}>
                                    <img src={item.img} alt='content image' />
                                </div>
                                <div className={`content__wrapper ${isBlockEven ? 'content__wrapper--reverse' : ''}`}>
                                    { item.title && 
                                        <h2 className='content__title'>{item.title}</h2> 
                                    }
                                    { item.content_1 && 
                                        <p className='content__text'>{item.content_1}</p> 
                                    }
                                    { item.content_2 && 
                                        <p className='content__text'>{item.content_2}</p> 
                                    }
                                    { item.content && 
                                        <p className='content__text'>{item.content}</p> 
                                    }
                                    { item.button_text && 
                                        <Link to={buttonLink}>
                                            <button className='content__button btn btn--transparent'>
                                                {item.button_text}
                                            </button>
                                        </Link>
                                    }
                                </div>
                            </>
                        }
                    </div>
                );
            })}
        </div>
    );
}

export default ContentBlock;