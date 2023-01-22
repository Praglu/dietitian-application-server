import React from 'react';
import './OpinionItem.scss';
import { FaUserCircle } from 'react-icons/fa';

function OpinionItem({ data }) {
    return (
        <div className='opinion-item'>
            <div className='opinion-item__header'>
                <FaUserCircle />
                { data.user_name && 
                    <h3>{data.user_name}</h3> 
                }
            </div>
            { data.opinion_text && 
                <div className='opinion-item__content'>{data.opinion_text}</div> 
            }
        </div>
    );
}

export default OpinionItem;