fetch('/api/peliculas')
  .then((res) => res.json())
  .then((movies) => {
    const rows = movies.map((m) => [
      m.title,
      m.release_date || '',
      m.rating ?? '',
      m.runtime ?? '',
      Array.isArray(m.genres) ? m.genres.join(', ') : '',
      m.votes ?? '',
      m.language || '',
      m.budget ?? '',
      m.revenue ?? ''
    ]);

    new gridjs.Grid({
      columns: [
        'Título',
        'Fecha',
        'Rating',
        'Duración (min)',
        'Géneros',
        'Votos',
        'Idioma',
        'Presupuesto',
        'Recaudación'
      ],
      data: rows,
      search: true,
      sort: true,
      pagination: { enabled: true, limit: 20 }
    }).render(document.getElementById('wrapper'));
  })
  .catch((err) => {
    console.error('Error cargando películas:', err);
    const wrapper = document.getElementById('wrapper');
    if (wrapper) wrapper.textContent = 'Error cargando datos de películas.';
  });