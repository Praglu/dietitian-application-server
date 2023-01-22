import React from 'react';
import './Breadcrumbs.scss';
import { Link } from 'react-router-dom';
import { 
    Breadcrumbs as MUIBreadcrumbs,
    Typography 
} from '@mui/material';

function Breadcrumbs({ title }) {
    const pathnames = location.pathname.split('/').filter(x => x);

    return (
        <MUIBreadcrumbs className='breadcrumbs' aria-label='breadcrumb'>
            <Link to='/'>{'Home'}</Link>
            {pathnames.map((element, index) => {
                const lastElement = index === pathnames.length - 1;
                const link = `/${pathnames.slice(0, index + 1).join('/')}`;

                return lastElement ? (
                    <Typography key={index} color='text.primary'>{title ? title : element}</Typography>
                ) : (
                    <Link key={index} color='inherit' to={link}>{element}</Link>
                );
            })}
        </MUIBreadcrumbs>
    );
}

export default Breadcrumbs;