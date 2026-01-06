document.addEventListener('DOMContentLoaded', async () => {
  const corrImg = document.getElementById('corrMatrixImg');
  const roiImg = document.getElementById('roiChartImg');
  const genreSelect = document.getElementById('genreSelect');
  const roiGenreImg = document.getElementById('roiGenreImg');
  const scatterImg = document.getElementById('scatterImg');
  const scatterX = document.getElementById('scatterX');
  const scatterY = document.getElementById('scatterY');

  async function postJSON(url, body) {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: body ? JSON.stringify(body) : undefined,
    });
    return res.json();
  }

  // Generar matriz de correlación al cargar la página
  try {
    const data = await postJSON('/api/financial/matrix_correlation');
    if (data.image) {
      corrImg.src = data.image + `?t=${Date.now()}`;
    }
  } catch (e) { console.error(e); }

  // ROI gráfico
  document.getElementById('genRoiBtn')?.addEventListener('click', async () => {
    try {
      const data = await postJSON('/api/financial/roi_chart');
      if (data.image) {
        roiImg.src = data.image + `?t=${Date.now()}`;
      }
    } catch (e) { console.error(e); }
  });

  // ROI por genero
  document.getElementById('genRoiGenreBtn')?.addEventListener('click', async () => {
    const genre = genreSelect?.value;
    if (!genre) return;
    try {
      const data = await postJSON(`/api/financial/roi_chart_by_genre?genre=${encodeURIComponent(genre)}`);
      if (data.image) {
        roiGenreImg.src = data.image + `?t=${Date.now()}`;
      }
    } catch (e) { console.error(e); }
  });

  // Gráfico de dispersión
  document.getElementById('genScatterBtn')?.addEventListener('click', async () => {
    const x = scatterX?.value;
    const y = scatterY?.value;
    if (!x || !y) return;
    try {
      const data = await postJSON(`/api/financial/scatter?x_var=${encodeURIComponent(x)}&y_var=${encodeURIComponent(y)}`);
      if (data.image) {
        scatterImg.src = data.image + `?t=${Date.now()}`;
      }
    } catch (e) { console.error(e); }
  });
});
