import React, { useEffect, useState } from 'react';
import './About.scss';
import ContactBlock from '/src/components/layout/ContactBlock/ContactBlock';
import ContentBlock from '/src/components/layout/ContentBlock/ContentBlock';
import ExperienceBlock from '/src/components/layout/ExperienceBlock/ExperienceBlock';
import data from '/src/data/About';
import contactData from '/src/data/ContactBlock';
import Hero from '/src/components/layout/Hero/Hero';

function About() {
    const [ firstSection, setFirstSection ] = useState([]);
    const [ secondSection, setSecondSection ] = useState([]);
    const isFirstSection = firstSection.length > 0;
    const isSecondSection = secondSection.length > 0;

    useEffect(() => {
        fetch(`${import.meta.env.VITE_API_URL}/api/content-blocks/about/`, {
            method: 'GET',
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            }
        })
        .then(data => {
            if (!data.length) {
                return;
            }

            if (data[0].first_section) {
                setFirstSection([data[0].first_section])
            }

            if (data[0].second_section) {
                setSecondSection(data[0].second_section);
            }
        })
        .catch(error => {
            console.log('Error: ', error);
        });
    }, []);

    return (
        <main className='about'>
            <Hero data={data.hero} />
            { isFirstSection &&
                <ContentBlock data={firstSection} />
            }
            <ExperienceBlock data={data.experienceBlock} />
            { isSecondSection &&
                <ContentBlock data={secondSection} />
            }
            <ContactBlock data={contactData} />
        </main>
    );
}

export default About;