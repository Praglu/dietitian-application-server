import { useContext, createContext, useState, useEffect } from 'react';

const Blog = createContext();

function BlogContext({ children }) {
    const [ posts, setPosts ] = useState([]);

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}/api/blog/post/`, {
            method: 'GET'
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            }
        })
        .then(data => {
            if(data) {
                setPosts(data);
            }
        })
        .catch(error => {
            console.log('Error: ', error);
        });
    }, []);

    return (
        <Blog.Provider value={{ posts }}>
            {children}
        </Blog.Provider>
    );
}

export default BlogContext;

export const useBlog = () => {
    return useContext(Blog);
};