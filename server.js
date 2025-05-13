const express = require('express');
const app = express();
const PORT = 3000;

// Middleware pour gérer les données du formulaire
app.use(express.urlencoded({ extended: true }));

// Route pour la recherche
app.get('/search', (req, res) => {
  const query = req.query.query; // Récupérer le terme de recherche
  console.log(`Recherche effectuée pour : ${query}`);

  // Simuler une base de données (exemple)
  const database = [
    { id: 1, name: 'Petit-déjeuner' },
    { id: 2, name: 'Déjeuner' },
    { id: 3, name: 'Dîner' },
    { id: 4, name: 'Entrées' },
    { id: 5, name: 'Dessert' },
  ];

  // Filtrer les résultats
  const results = database.filter(item =>
    item.name.toLowerCase().includes(query.toLowerCase())
  );

  // Retourner les résultats
  res.json({
    query,
    results,
  });
});

// Lancer le serveur
app.listen(PORT, () => {
  console.log(`Serveur en écoute sur http://localhost:${PORT}`);
});
