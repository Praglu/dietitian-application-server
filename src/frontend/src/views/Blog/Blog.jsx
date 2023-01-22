import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Blog.scss';
import Breadcrumbs from '/src/components/layout/Breadcrumbs/Breadcrumbs';
import { useBlog } from '/src/contexts/BlogContext';

function Blog() {
    const [ isShowMoreClicked, setShowMore ] = useState(false);
    const { posts } = useBlog();
    const anyPosts = posts.length > 0;
    const showBtn = posts.length > 6;

    const toggleShowMore = () => {
        setShowMore(!isShowMoreClicked);
    };

    return (
        <main className='blog'>
            <Breadcrumbs />
            <div className='blog__content'>
                <h1 className='blog__title'>
                    {'Kolarstwo oczami zakochanego w nim dietetyka.'}
                </h1> 
                <p className='blog__sub-title'>
                    {'Z przymrużeniem oka o najpiękniejszym sporcie na świecie, a do tego niewielka dawka żywieniowego naukowego bełkotu.'}
                </p> 
                <div className='blog__image'>
                    <img src='/src/assets/logo.jpg' alt='blog' />
                </div>
            </div>
            { anyPosts &&
                <div className='blog__posts'>
                    <div className='blog__section-title'>
                        {'Najnowsze posty'}
                    </div> 
                    <ul className={`${isShowMoreClicked ? '' : 'blog__hide-more'}`}>
                        {posts.map(item => {
                            return (
                                <li key={item.id}>
                                    { item.img &&
                                        <Link to={`/blog/${item.id}`}>
                                            <div className='blog__post-container'>
                                                <div className='blog__post-image'>
                                                    <img src={item.img} alt='post' />
                                                </div>
                                                <div className='blog__post-content'>
                                                    <div className='blog__post-title'>
                                                        {item.title}
                                                    </div> 
                                                    <div className='blog__post-date'>
                                                        {item.date}
                                                    </div> 
                                                </div>
                                            </div>
                                        </Link>
                                    }
                                </li>
                            );
                        })}
                    </ul>
                    { showBtn &&
                        <button className={`blog__button btn btn--transparent ${isShowMoreClicked ? 'blog__button--hidden' : ''}`}
                            onClick={toggleShowMore}
                        >
                            {'Pokaż więcej'}
                        </button>
                    }
                </div>
            }
        </main>
    );
}

export default Blog;