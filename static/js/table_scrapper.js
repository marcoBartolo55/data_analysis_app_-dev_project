// Cargar datos de películas desde la API y mostrarlos en una tabla con Grid.js
fetch('/api/peliculas')
  .then((res) => res.json())
  .then((movies) => {
    const rows = movies.map((m) => {
      const directors = Array.isArray(m.directors)
        ? m.directors.map((d) => d.name).join(', ')
        : '';
      const writers = Array.isArray(m.writers)
        ? m.writers.map((w) => (w.job ? `${w.name} (${w.job})` : w.name)).join(', ')
        : '';
      const genres = Array.isArray(m.genres) ? m.genres.join(', ') : '';
      const fmt = (n) => (typeof n === 'number' ? n.toLocaleString('es-ES') : (n ?? ''));

      return [
        m.id ?? '',
        m.title ?? '',
        m.release_date || '',
        m.runtime ?? '',
        m.language || '',
        genres,
        fmt(m.rating),
        fmt(m.votes),
        fmt(m.budget),
        fmt(m.revenue),
        directors,
        writers
      ];
    });

    // Iniciar Grid.js con los datos de peliculas
    new gridjs.Grid({
      columns: [
        'ID',
        'Título',
        'Fecha',
        'Duración (min)',
        'Idioma',
        'Géneros',
        'Rating',
        'Votos',
        'Presupuesto',
        'Recaudación',
        'Directores',
        'Guionistas'
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