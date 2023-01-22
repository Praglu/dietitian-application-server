import React from 'react';
import './Carousel.scss';
import ElasticCarousel from '@itseasy21/react-elastic-carousel';

const breakPoints = [
    { width: 1, itemsToShow: 1, itemsToScroll: 1 },
    { width: 550, itemsToShow: 2, itemsToScroll: 1 },
    { width: 768, itemsToShow: 3, itemsToScroll: 1 },
    { width: 1200, itemsToShow: 4, itemsToScroll: 1 }
];

function Carousel({ randomProducts, data, Block, title, page }) {
    const items = randomProducts ? randomProducts : data;

    return (
        <div className='carousel'>
            <h2>{title}</h2>
            <div className='carousel__content'>
                <ElasticCarousel itemPadding={[0, 10]} breakPoints={breakPoints}>
                    {items.map(item => {
                        return (
                            <Block
                                page={page}
                                key={item.id}
                                data={item}
                            />
                        );
                    })}
                </ElasticCarousel>
            </div>
        </div>
    );
}

export default Carousel;