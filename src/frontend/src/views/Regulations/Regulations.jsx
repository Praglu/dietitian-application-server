import React, { useEffect, useState } from 'react';
import './Regulations.scss';
import Breadcrumbs from '/src/components/layout/Breadcrumbs/Breadcrumbs';
import data from '/src/data/Regulations.js';

function Regulations({ page }) {
    const [ pageData, setPageData ] = useState({});

    useEffect(() => {
        switch(page) {
            case 'privacy-policy':
                setPageData(data.privacyPolicy);
                break;
            case 'cookies-policy':
                setPageData(data.cookiesPolicy);
                break;
            case 'regulations':
                setPageData(data.regulations);
                break;
            case 'payment-methods':
                setPageData(data.paymentMethods);
                break;
            default:
                break;
        }
    }, [page]);

    return (
        <main className='regulations'>
            <div className='regulations__header'>
                <Breadcrumbs title={pageData.title} />
                <h1>{pageData.title}</h1>
            </div>
            <div className='regulations__content'>
                { pageData.numberedList &&
                    <ol>
                        {pageData.numberedList.map((item, index) => {
                            return (
                                <li key={index}>
                                    <h3>{item.title}</h3>
                                    <div>{item.description}</div>
                                </li>
                            );
                        })}
                    </ol>
                }
                { pageData.list &&
                    <ul className='regulations__list'>
                        {pageData.list.map((item, index) => {
                            return (
                                <li key={index}>
                                    <h3>{item.title}</h3>
                                    <ul>
                                        {item.sublist.map(((item, index) => {
                                            return (
                                                <li key={index}>
                                                    <span>{item.title}</span>
                                                    {item.description}
                                                </li>
                                            );
                                        }))}
                                    </ul>
                                </li>
                            );
                        })}
                    </ul>
                }
            </div>
        </main>
    );
}

export default Regulations;