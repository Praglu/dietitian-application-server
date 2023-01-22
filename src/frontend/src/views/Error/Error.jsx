import React from 'react';
import { Link } from 'react-router-dom';
import './Error.scss';
import data from '/src/data/Error.js';
import Breadcrumbs from '/src/components/layout/Breadcrumbs/Breadcrumbs';

function Error({ isAPI }) {
    const page = isAPI ? data.wrongPage : data.noAPI ;

    return (
        <main className='error'>
            { isAPI &&
                <Breadcrumbs title={page.title} />
            }
            <div className='error__content'>
                <div className='error__container'>
                    <h1>{page.title}</h1>
                    { page.buttonText &&
                        <Link to={'/'}>
                            <button className='btn btn--transparent'>
                                {page.buttonText}
                            </button>
                        </Link>
                    }
                    { page.info &&
                        <h2>{page.info}</h2>
                    }
                </div>
            </div>
        </main>
    );
}

export default Error;