import React from 'react';

function Mail({ closeDialog }) {
    return (
        <div className='message'>
            <h3>{'Wiadomość wysłana !'}</h3>
            <button className='btn' onClick={closeDialog}>
                {'Zamknij'}
            </button>
        </div>
    );
}

export default Mail;