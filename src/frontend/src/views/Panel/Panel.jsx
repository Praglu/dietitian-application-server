import React, { useState } from 'react';
import './Panel.scss';
import Breadcrumbs from '/src/components/layout/Breadcrumbs/Breadcrumbs';
import Dialog from '/src/components/layout/Dialog/Dialog';
import { useDialog } from '/src/contexts/DialogContext';
import PanelMessage from '/src/components/layout/Dialog/Message/PanelMessage/PanelMessage';
import Account from '/src/views/Panel/Account/Account';
import Login from '/src/views/Panel/Login/Login';
import Register from '/src/views/Panel/Register/Register';

function Panel() {
    const [ isRegister, setRegister ] = useState(false);
    const { showDialog } = useDialog();
    const token = localStorage.getItem('authToken');

    const toggleRegister = () => {
        setRegister(!isRegister);
    };

    return (
        <main className='panel'>
            <Breadcrumbs title={'Panel klienta'} />
            { token ?
                <Account />
            :
                <div className='panel__container'>
                    { isRegister ?
                        <Register hideRegister={toggleRegister} />
                    :
                        <Login showRegister={toggleRegister} />
                    }
                </div>
            }
            { showDialog &&
                <Dialog>
                    <PanelMessage 
                        isRegister={isRegister}
                        hideRegister={toggleRegister}
                    />
                </Dialog>
            }
        </main>
    );
}

export default Panel;