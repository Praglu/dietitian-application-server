import React from 'react';

function ErrorMessage({ message, closeDialog }) {
    return (
        <div className='message'>
            <h2>{'Błąd'}</h2>
            <h3>{message}</h3>
            <button className='btn' onClick={closeDialog}>
                {'Zamknij'}
            </button>
        </div>
    );
}

export default ErrorMessage;