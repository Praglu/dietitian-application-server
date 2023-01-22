import { useContext, createContext, useState, useEffect } from 'react';
import Loader from '/src/components/other/Loader/Loader';
import Overlay from '/src/components/layout/Overlay/Overlay';

const Loading = createContext();

function LoadingContext({ children }) {
    const [ isLoading, setLoading ] = useState(false);

    useEffect(() => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }, [isLoading]);

    return (
        <Loading.Provider value={{ isLoading, setLoading }}>
            {children}
            { isLoading &&
                <>
                    <Loader />
                    <Overlay />
                </>
            }
        </Loading.Provider>
    );
}

export default LoadingContext;

export const useLoading = () => {
    return useContext(Loading);
}