import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('Carregando...');

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL || 'http://localhost:8000/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage('Erro ao conectar com a API'));
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>FuturoFC ⚽</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
