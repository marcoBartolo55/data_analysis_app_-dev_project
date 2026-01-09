// Dos tablas Grid.js con dos fuentes distintas:
// - Tabla 1: /api/peliculas  -> #wrapper
// - Tabla 2: /api/peliculas/processed -> #wrapper2

function dbg(msg) {
  const d = document.getElementById('fetch-debug');
  if (d) {
    d.textContent += msg + '\n';
    d.scrollTop = d.scrollHeight;
  }
  console.log(msg);
}

const GRID_COLUMNS = [
  'ID',
  'Título',
  async function loadRawTable() {
    const wrapperId = "wrapper";
    const wrapper = document.getElementById(wrapperId);

    if (!wrapper) {
      console.error(`No se encontró el contenedor #${wrapperId}`);
      return;
    }

    wrapper.innerHTML = "";

    try {
      const resp = await fetch("/api/peliculas");
      if (!resp.ok) {
        const msg = await resp.text();
        throw new Error(`HTTP ${resp.status}: ${msg}`);
      }

      const data = await resp.json();
      if (!Array.isArray(data) || data.length === 0) {
        wrapper.innerHTML = "<p>No hay datos para mostrar.</p>";
        return;
      }

      const columns = Object.keys(data[0]);

      new gridjs.Grid({
        columns,
        data: data.map((row) => columns.map((col) => row[col])),
        pagination: { enabled: true, limit: 20 },
        search: true,
        sort: true,
        resizable: true,
        fixedHeader: true,
        height: "600px",
      }).render(wrapper);
    } catch (err) {
      console.error("Error cargando /api/peliculas:", err);
      wrapper.innerHTML = "<p>Error cargando la tabla.</p>";
    }
  }

  document.addEventListener("DOMContentLoaded", loadRawTable);
async function loadProcessedTable() {
  dbg('[table_scrapper] Cargando /api/peliculas/processed...');
  try {
    const movies = await fetchJsonArray('/api/peliculas/processed');
    dbg(`[table_scrapper] /api/peliculas/processed -> items: ${movies.length}`);
    if (movies.length === 0) {
      const wrapper = document.getElementById('wrapper2');
      if (wrapper) wrapper.textContent = 'No hay datos procesados para mostrar.';
      return;
    }
    renderGrid(movies.map(toRow), 'wrapper2');
  } catch (e) {
    console.error('Error cargando películas procesadas:', e);
    dbg('Error cargando películas procesadas: ' + (e && e.message ? e.message : e));
    const wrapper = document.getElementById('wrapper2');
    if (wrapper) wrapper.textContent = 'Error cargando datos procesados.';
  }
}

// Ejecutar ambas cargas al iniciar la página
window.loadRawTable = loadRawTable;
window.loadProcessedTable = loadProcessedTable;

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    loadRawTable();
    loadProcessedTable();
  });
} else {
  loadRawTable();
  loadProcessedTable();
}



