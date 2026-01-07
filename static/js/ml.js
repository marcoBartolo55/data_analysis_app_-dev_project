document.addEventListener('DOMContentLoaded', () => {
  const trainBtn = document.getElementById('mlTrainBtn');
  const trainOut = document.getElementById('mlTrainOutput');
  const predictBtn = document.getElementById('mlPredictBtn');
  const genreSel = document.getElementById('mlGenreSelect');
  const budgetInput = document.getElementById('mlBudgetInput');
  const predictRes = document.getElementById('mlPredictResult');

  async function postJSON(url, body) {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: body ? JSON.stringify(body) : undefined,
    });
    return res.json();
  }

  trainBtn?.addEventListener('click', async () => {
    trainOut.textContent = 'Entrenando...';
    try {
      const data = await postJSON('/api/ml/train');
      if (data.error) {
        trainOut.textContent = 'Error: ' + data.error;
      } else {
        trainOut.textContent = JSON.stringify(data, null, 2);
      }
    } catch (e) {
      trainOut.textContent = 'Error: ' + e;
    }
  });

  predictBtn?.addEventListener('click', async () => {
    predictRes.textContent = 'Prediciendo...';
    const genre = genreSel?.value;
    const budget = parseFloat(budgetInput?.value || '0');
    if (!genre || !budget || budget <= 0) {
      predictRes.textContent = 'Ingresa género y presupuesto válido';
      return;
    }
    try {
      const qs = new URLSearchParams({ budget: String(budget), genre });
      const data = await postJSON('/api/ml/predict?' + qs.toString());
      if (data.error) {
        predictRes.textContent = 'Error: ' + data.error;
      } else {
        const { genre, budget, predicted_revenue, predicted_roi_pct } = data;
        predictRes.innerHTML = `
          <div class="result-card">
            <div><strong>Género:</strong> ${genre}</div>
            <div><strong>Presupuesto:</strong> $${budget.toLocaleString()}</div>
            <div><strong>Ingreso estimado:</strong> $${Number(predicted_revenue).toLocaleString()}</div>
            <div><strong>ROI estimado:</strong> ${Number(predicted_roi_pct).toFixed(2)}%</div>
          </div>
        `;
      }
    } catch (e) {
      predictRes.textContent = 'Error: ' + e;
    }
  });
});
