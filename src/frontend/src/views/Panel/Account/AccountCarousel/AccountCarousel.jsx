import React from 'react';
import './AccountCarousel.scss';
import ElasticCarousel from '@itseasy21/react-elastic-carousel';
import AccountOrders from './AccountOrders/AccountOrders';
import AccountSettings from './AccountSettings/AccountSettings';

const breakPoints = [
    { width: 1, itemsToShow: 1, itemstoScroll: 1}
];

function AccountCarousel() {
    return (
        <div className='panel-carousel'>
            <ElasticCarousel itemPadding={[0, 10]} breakPoints={breakPoints}>
                <AccountOrders />
                {/* TODO */}
                {/* <AccountSettings /> */}
            </ElasticCarousel>
        </div>
    );
}

export default AccountCarousel;