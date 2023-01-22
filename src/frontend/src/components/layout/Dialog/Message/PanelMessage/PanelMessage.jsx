import React from 'react';
import { Link } from 'react-router-dom';
import { useDialog } from '/src/contexts/DialogContext';

function PanelMessage({ isRegister, hideRegister }) {
    const { toggleDialog } = useDialog();

    return (
        <div className='message'>
            { isRegister ?
                <>
                    <h2>{'Rejestracja pomyślna !'}</h2>
                    <div className='dialog__buttons'>
                        <button className='btn'
                            onClick={() => {
                                toggleDialog();
                                hideRegister();
                            }}
                        >
                            {'Przejdź do logowania'}
                        </button>
                        <button className='btn' onClick={toggleDialog}>
                            {'Zamknij'}
                        </button>
                    </div>
                </>
            :
                <>
                    <h2>{'Logowanie pomyślne !'}</h2>
                    <div className='dialog__buttons'>
                        <Link to={'/konto'}>
                            <button className='btn'>
                                {'Przejdź do konta'}
                            </button>
                        </Link>
                        <button className='btn' onClick={toggleDialog}>
                            {'Zamknij'}
                        </button>
                    </div>
                </>
            }
        </div>
    );
}

export default PanelMessage;