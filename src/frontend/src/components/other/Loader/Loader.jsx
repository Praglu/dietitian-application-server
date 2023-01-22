import React from 'react';
import { ThreeDots } from 'react-loader-spinner';

function Loader() {
    return (
        <div className='loader'>
            <ThreeDots 
                height="80" 
                width="80" 
                radius="9"
                color="#5A4FF3" 
                ariaLabel="three-dots-loading"
                wrapperStyle={
                    {
                        'position': 'fixed',
                        'top': '50%',
                        'left': '50%',
                        'transform': 'translate(-50%, -50%)'
                    }
                }
                visible={true}
            />
        </div>
    );
}

export default Loader;