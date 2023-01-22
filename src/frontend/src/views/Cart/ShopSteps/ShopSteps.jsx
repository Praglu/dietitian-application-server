import React from 'react';
import './ShopSteps.scss';
import StepCircle from '/src/assets/step-circle.svg';
import WhiteCircle from '/src/assets/white-circle.svg';
import CheckIcon from '/src/assets/check-circle.svg';

function ShopSteps({ cartStep }) {
    let stepOneIcon = cartStep > 1 ? WhiteCircle : StepCircle;
    let stepTwoIcon = cartStep > 2 ? WhiteCircle : StepCircle;
    
    return (
        <div className='steps'>
            <ul>
                <li>
                    <img className='steps__circle' src={stepOneIcon} alt='step' />
                    { cartStep > 1 ?
                        <img className='steps__check' src={CheckIcon} alt='check' />
                    :
                        <b>{'1'}</b>
                    }
                    {'Koszyk'}
                    <span>{'>'}</span>
                </li>
                <li>
                    <img className='steps__circle' src={stepTwoIcon} alt='step' />
                    { cartStep > 2 ?
                        <img className='steps__check' src={CheckIcon} alt='check' />
                    :
                        <b>{'2'}</b>
                    }
                    {'Moje dane'}
                    <span>{'>'}</span>
                </li>
                <li>
                    <img className='steps__circle' src={StepCircle} alt='step' />
                    <b>{'3'}</b>
                    {'Zamówienie'}
                </li>
            </ul>
        </div>
    );
}

export default ShopSteps;