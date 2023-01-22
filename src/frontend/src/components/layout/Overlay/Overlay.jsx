import React from 'react';
import './Overlay.scss';

function Overlay({ hideOverlay }) {
    return <div className='overlay' onClick={hideOverlay} />
}

export default Overlay;