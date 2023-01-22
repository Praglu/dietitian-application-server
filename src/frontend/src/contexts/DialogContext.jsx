import { useContext, createContext, useState } from 'react';
import Overlay from '/src/components/layout/Overlay/Overlay';
import DialogContainer from '/src/components/layout/Dialog/Dialog';
import Error from '/src/components/layout/Dialog/Message/Error/Error';

const Dialog = createContext();

function DialogContext({ children }) {
    const [ isDialog, setDialog ] = useState(false);
    const [ errorMessage, setErrorMessage ] = useState('');
    const isError = errorMessage.length > 0;
    const showDialog = isDialog && !isError;

    const toggleDialog = () => {
        setDialog(!isDialog);
        setErrorMessage('');
    }

    const setError = message => {
        setDialog(!isDialog);
        setErrorMessage(message);
    }

    return (
        <Dialog.Provider value={{ showDialog, isError, toggleDialog, setError }}>
            {children}
            { isError &&
                <DialogContainer>
                    <Error 
                        message={errorMessage}
                        closeDialog={toggleDialog}
                    />
                </DialogContainer>
            }
            { isDialog && 
                <Overlay hideOverlay={toggleDialog} />
            }
        </Dialog.Provider>
    );
}

export default DialogContext;

export const useDialog = () => {
    return useContext(Dialog);
}