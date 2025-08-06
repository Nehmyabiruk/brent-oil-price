import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import './App.css';

// Fetching data from Flask backend
const App = () => {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch('/api/prices')
      .then(response => response.json())
      .then(data => setPrices(data));
    fetch('/api/events')
      .then(response => response.json())
      .then(data => setEvents(data));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Brent Oil Price Analysis</h1>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={prices}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="Price" stroke="#8884d8" />
        </LineChart>
      </ResponsiveContainer>
      <h2 className="text-xl font-bold mt-4">Key Events</h2>
      <ul>
        {events.map(event => (
          <li key={event.Date}>{event.Date}: {event.Event} ({event.Category})</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
