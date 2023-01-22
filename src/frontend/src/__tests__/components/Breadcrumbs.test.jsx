import { render, screen } from '@testing-library/react';
import { describe, it } from 'vitest';
import Breadcrumbs from '/src/components/layout/Breadcrumbs/Breadcrumbs';
import { MemoryRouter as Router } from 'react-router-dom';

describe('first', () => {
    it('Should render Breadcrumbs with title Oferta', () => {
        history.pushState({}, '', '/offer');
        render(<Router><Breadcrumbs title={'Oferta'} /></Router>);

        const title = screen.getByText('Oferta');
        expect(title.textContent).toEqual('Oferta');
    });
});