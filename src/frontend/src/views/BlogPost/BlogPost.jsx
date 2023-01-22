import React, { useEffect, useState } from 'react';
import './BlogPost.scss';
import { useParams } from 'react-router-dom';
import Breadcrumbs from '/src/components/layout/Breadcrumbs/Breadcrumbs';
import contactData from '/src/data/ContactBlock.js';
import Carousel from '/src/components/layout/Carousel/Carousel';
import Item from '/src/components/layout/Carousel/Item/Item';
import ContactBlock from '/src/components/layout/ContactBlock/ContactBlock';
import { useBlog } from '/src/contexts/BlogContext';

function BlogPost() {
    const { id } = useParams();
    const [ post, setPost ] = useState({});
    const { posts } = useBlog();
    const anyPosts = posts.length > 0;

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}/api/blog/post/${id}/`, {
            method: 'GET'
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            }
        })
        .then(data => {
            if(data) {
                setPost(data);
            }
        })
        .catch(error => {
            console.log('Error: ', error);
        });
    }, [id]);

    return (
        <main className='blog-post'>
            { post.title &&
                <>  
                    <Breadcrumbs title={post.title} />
                    <div className='blog-post__container'>
                        <h1 className='blog-post__title'>
                            {post.title}
                        </h1>
                        <div className='blog-post__info'>
                            {`Kolarstwo od kuchni  |  ${post.date}`}
                        </div>
                        <img className='blog-post__image' src={post.img} alt='blog post' />
                        <div className='blog-post__wrapper'>
                            <div className='blog-post__content'>
                                {post.content_1}
                            </div>
                            <img className='blog-post__content-img' src={post.content_img} alt='content' />
                            <div className='blog-post__content'>
                                {post.content_2}
                            </div>
                        </div>
                    </div>
                </>
            }
            { anyPosts &&
                <Carousel 
                    data={posts}
                    page={'blog'}
                    title={'Kolarstwo od kuchni - blog'}
                    Block={Item} 
                />
            }
            <ContactBlock data={contactData} />
        </main>
    );
}

export default BlogPost;