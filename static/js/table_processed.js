async function loadProcessedTable() {
  const wrapperId = "wrapper-processed";
  const wrapper = document.getElementById(wrapperId);

  if (!wrapper) {
    console.error(`No se encontró el contenedor #${wrapperId}`);
    return;
  }

  wrapper.innerHTML = "";

  try {
    const resp = await fetch("/api/peliculas/processed");
    if (!resp.ok) {
      const msg = await resp.text();
      throw new Error(`HTTP ${resp.status}: ${msg}`);
    }

    const data = await resp.json();
    if (!Array.isArray(data) || data.length === 0) {
      wrapper.innerHTML = "<p>No hay datos procesados para mostrar.</p>";
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
    console.error("Error cargando /api/peliculas/processed:", err);
    wrapper.innerHTML = "<p>Error cargando la tabla de procesadas.</p>";
  }
}

document.addEventListener("DOMContentLoaded", loadProcessedTable);
