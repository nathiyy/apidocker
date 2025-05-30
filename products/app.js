const express = require('express');
const app = express();
const PORT = 3001;

// Criei uma rota simples pra listar os produtos
app.get('/products', (req, res) => {
  res.json([{ id: 1, name: 'notbook' , price: '3000' }]); // Por enquanto só tem 1 produto fixo
});

// Inicia o servidor na porta 3001
app.listen(PORT, () => {
  console.log(`Products service running on port ${PORT}`); // Só pra saber que tá funcionando
});
