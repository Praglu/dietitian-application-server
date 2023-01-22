import React from 'react';
import './ExperienceBlock.scss';

function ExperienceBlock({ data }) {
    return (
        <div className='experience'>
            <ul>
                {data.map(item => {
                    return (
                        <li key={item.id}>
                            { item.title && 
                                <h1 className='experience__title'>{item.title}</h1> 
                            }
                            { item.content && 
                                <p className='experience__description'>{item.content}</p> 
                            }
                        </li>
                    );
                })}
            </ul>
        </div>
    );
}

export default ExperienceBlock;