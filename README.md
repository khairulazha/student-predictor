# Sistem Prediksi Prestasi Pelajar 🎓

Aplikasi web Streamlit untuk membantu pensyarah menjangka sama ada pelajar akan **Lulus** atau **Gagal** sesuatu kursus berdasarkan 4 input utama.

## Input

| Input | Skala | Keterangan |
|-------|-------|------------|
| Markah Ujian | Rendah / Sederhana / Tinggi | < 40% / 40–69% / ≥ 70% |
| Markah Kuiz | Rendah / Sederhana / Tinggi | < 40% / 40–69% / ≥ 70% |
| Markah Tugasan | Rendah / Sederhana / Tinggi | < 40% / 40–69% / ≥ 70% |
| Kehadiran | Rendah / Sederhana / Tinggi | < 60% / 60–79% / ≥ 80% |

## Output

- ✅ **LULUS** — Prestasi memuaskan
- ⚠️ **BERISIKO** — Perlu intervensi awal
- ❌ **GAGAL** — Tindakan segera diperlukan

Setiap keputusan disertai **cadangan tindakan** untuk pensyarah.

## Cara Guna (Local)

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy (Streamlit Community Cloud)

1. Fork atau push repo ini ke GitHub
2. Pergi ke [share.streamlit.io](https://share.streamlit.io)
3. Log in dengan GitHub
4. Klik **New app** → pilih repo ini → main file: `app.py`
5. Klik **Deploy**
