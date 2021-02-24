import React, { useEffect } from 'react';
import * as d3 from 'd3';

const data = [
  {
    country: 'United States',
    countryCode: 'US',
    region: 'VA',
    regionName: 'Virginia',
    city: 'Ashburn',
    zip: '20149',
    lat: 39.03,
    lon: -77.5,
    timezone: 'America/New_York',
    isp: 'Google LLC',
    org: 'Google Public DNS',
    as: 'AS15169 Google LLC',
    query: '8.8.8.8',
    iteration: 248,
  },
  {
    country: 'Canada',
    countryCode: 'CA',
    region: 'QC',
    regionName: 'Quebec',
    city: 'Montreal',
    zip: 'H1S',
    lat: 45.5808,
    lon: -73.5825,
    timezone: 'America/Toronto',
    isp: 'Le Groupe Videotron Ltee',
    org: 'Videotron Ltee',
    as: 'AS5769 Videotron Telecom Ltee',
    query: '24.48.0.1',
    iteration: 154,
  },
  {
    country: 'China',
    countryCode: 'CN',
    region: 'FJ',
    regionName: 'Fujian',
    city: 'Fuzhou',
    zip: '',
    lat: 26.0745,
    lon: 119.296,
    timezone: 'Asia/Shanghai',
    isp: 'Chinanet',
    org: 'Chinanet FJ',
    as: 'AS4134 CHINANET-BACKBONE',
    query: '110.90.1.0',
    iteration: 177,
  },
  {
    country: 'United States',
    countryCode: 'US',
    region: 'AZ',
    regionName: 'Arizona',
    city: 'Sierra Vista',
    zip: '85613',
    lat: 31.5552,
    lon: -110.35,
    timezone: 'America/Phoenix',
    isp: 'DoD Network Information Center',
    org: 'USAISC',
    as: 'AS335 DoD Network Information Center',
    query: '55.244.122.20',
    iteration: 302,
  },
];

export default function App() {
  useEffect(() => {
    d3.select('#graph')
      .selectAll('rect')
      .data(data, (d) => d)
      .join('rect')
      .attr('x', (d, i) => i * 50)
      .attr('y', (d) => 400 - d.iteration)
      .attr('width', 50)
      .attr('height', (d) => d.iteration)
      .attr('fill', '#F0FFFF')
      .attr('stroke', '#5F9EA0')
      .attr('stroke-width', 1)
      .append('text')
      .text((d) => d.country);
  }, []);

  return (
    <div>
      <svg id="graph" width="400" height="400"></svg>
    </div>
  );
}
