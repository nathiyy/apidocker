const express = require('express');
const app = express();
const PORT = 3001;

app.get('/products', (req, res) => {
  res.json([{ id: 1, name: 'notbook' , price: '3000' }]);
});

app.listen(PORT, () => {
  console.log(`Products service running on port ${PORT}`);
});
