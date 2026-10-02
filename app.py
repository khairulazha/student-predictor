"""
Sistem Prediksi Prestasi Pelajar
=================================
Pensyarah memasukkan 4 input (Ujian, Kuiz, Tugasan, Kehadiran)
dalam skala Rendah / Sederhana / Tinggi.
Sistem menggunakan rule-based logic untuk predict LULUS atau GAGAL.

Run:
    streamlit run app.py
"""

import streamlit as st

# ── Konfigurasi halaman ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Sistem Prediksi Prestasi Pelajar",
    page_icon="🎓",
    layout="centered",
)

# ── CSS custom ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .lulus-box {
        background-color: #d4edda;
        border: 2px solid #28a745;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
    }
    .gagal-box {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
    }
    .risk-box {
        background-color: #fff3cd;
        border: 2px solid #ffc107;
        border-radius: 12px;
        padding: 24px;
        text-align: center;
    }
    .result-title {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 8px;
    }
    .result-sub {
        font-size: 1rem;
        color: #555;
    }
    .score-badge {
        display: inline-block;
        padding: 4px 14px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9rem;
        margin: 2px;
    }
    .rendah  { background-color: #f8d7da; color: #721c24; }
    .sederhana { background-color: #fff3cd; color: #856404; }
    .tinggi  { background-color: #d4edda; color: #155724; }
</style>
""", unsafe_allow_html=True)

# ── Engine prediksi (rule-based) ───────────────────────────────────────────────
SKOR = {"Rendah": 0, "Sederhana": 1, "Tinggi": 2}

def predict(ujian, kuiz, tugasan, kehadiran):
    """
    Rule-based prediction engine.
    
    Logik:
    - Setiap input diberi skor: Rendah=0, Sederhana=1, Tinggi=2
    - Jumlah skor maksimum = 8 (semua Tinggi)
    
    Keputusan:
    - Skor >= 5  → LULUS (selamat)
    - Skor 3–4  → BERISIKO (ada kemungkinan gagal)
    - Skor < 3   → GAGAL (kritikal)
    
    Syarat tambahan (veto rules):
    - Kehadiran RENDAH → terus GAGAL (tanpa mengira yang lain)
    - Ujian RENDAH DAN Kuiz RENDAH → GAGAL
    """
    # Veto rules
    if SKOR[kehadiran] == 0:
        return "GAGAL", "kritikal", "Kehadiran sangat rendah — pelajar berisiko tinggi gagal kursus."

    if SKOR[ujian] == 0 and SKOR[kuiz] == 0:
        return "GAGAL", "kritikal", "Prestasi ujian dan kuiz sangat lemah."

    jumlah = SKOR[ujian] + SKOR[kuiz] + SKOR[tugasan] + SKOR[kehadiran]

    if jumlah >= 5:
        return "LULUS", "selamat", "Prestasi pelajar secara keseluruhan memuaskan."
    elif jumlah >= 3:
        return "BERISIKO", "amaran", "Pelajar berada di zon berisiko — intervensi awal disyorkan."
    else:
        return "GAGAL", "kritikal", "Prestasi keseluruhan sangat rendah — tindakan segera diperlukan."


def badge(label):
    css = label.lower()
    return f'<span class="score-badge {css}">{label}</span>'


# ── UI Utama ───────────────────────────────────────────────────────────────────
st.title("🎓 Sistem Prediksi Prestasi Pelajar")
st.caption(
    "Masukkan maklumat pelajar di bawah. Sistem akan menganalisis dan "
    "menjangkakan sama ada pelajar akan **Lulus** atau **Gagal** kursus."
)

st.divider()

# ── Input ──────────────────────────────────────────────────────────────────────
st.subheader("📋 Maklumat Pelajar")

col1, col2 = st.columns(2)

with col1:
    ujian = st.radio(
        "📝 Markah Ujian",
        options=["Rendah", "Sederhana", "Tinggi"],
        index=1,
        help="Rendah: < 40%  |  Sederhana: 40–69%  |  Tinggi: ≥ 70%",
        horizontal=True,
    )
    kuiz = st.radio(
        "🧩 Markah Kuiz",
        options=["Rendah", "Sederhana", "Tinggi"],
        index=1,
        help="Rendah: < 40%  |  Sederhana: 40–69%  |  Tinggi: ≥ 70%",
        horizontal=True,
    )

with col2:
    tugasan = st.radio(
        "📚 Markah Tugasan",
        options=["Rendah", "Sederhana", "Tinggi"],
        index=1,
        help="Rendah: < 40%  |  Sederhana: 40–69%  |  Tinggi: ≥ 70%",
        horizontal=True,
    )
    kehadiran = st.radio(
        "🏫 Kehadiran",
        options=["Rendah", "Sederhana", "Tinggi"],
        index=1,
        help="Rendah: < 60%  |  Sederhana: 60–79%  |  Tinggi: ≥ 80%",
        horizontal=True,
    )

st.divider()

# ── Butang predict ─────────────────────────────────────────────────────────────
predict_btn = st.button("🔍 Buat Prediksi", type="primary", use_container_width=True)

if predict_btn:
    hasil, tahap, mesej = predict(ujian, kuiz, tugasan, kehadiran)

    st.subheader("📊 Keputusan Prediksi")

    # Paparan ringkasan input
    st.markdown(
        f"**Input:** Ujian {badge(ujian)} &nbsp; Kuiz {badge(kuiz)} &nbsp; "
        f"Tugasan {badge(tugasan)} &nbsp; Kehadiran {badge(kehadiran)}",
        unsafe_allow_html=True,
    )

    st.write("")

    # Kotak keputusan
    if tahap == "selamat":
        st.markdown(f"""
        <div class="lulus-box">
            <div class="result-title">✅ {hasil}</div>
            <div class="result-sub">{mesej}</div>
        </div>
        """, unsafe_allow_html=True)

    elif tahap == "amaran":
        st.markdown(f"""
        <div class="risk-box">
            <div class="result-title">⚠️ {hasil}</div>
            <div class="result-sub">{mesej}</div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div class="gagal-box">
            <div class="result-title">❌ {hasil}</div>
            <div class="result-sub">{mesej}</div>
        </div>
        """, unsafe_allow_html=True)

    # Cadangan tindakan pensyarah
    st.write("")
    st.subheader("💡 Cadangan Tindakan")

    if tahap == "selamat":
        st.success("Pelajar berada dalam keadaan baik. Teruskan pemantauan biasa.")
    elif tahap == "amaran":
        st.warning(
            "**Tindakan yang disyorkan:**\n"
            "- Buat sesi kaunseling akademik dengan pelajar\n"
            "- Semak kefahaman pelajar dalam topik-topik lemah\n"
            "- Galakkan pelajar sertai kelas tambahan atau tutorial\n"
            "- Pantau kehadiran lebih kerap"
        )
    else:
        st.error(
            "**Tindakan segera diperlukan:**\n"
            "- Hubungi pelajar dengan segera\n"
            "- Rujuk kepada penasihat akademik / Unit Kaunseling\n"
            "- Bincang pelan pemulihan (remedial plan)\n"
            "- Maklumkan kepada Ketua Jabatan jika perlu"
        )

    # Rumusan skor
    jumlah_skor = SKOR[ujian] + SKOR[kuiz] + SKOR[tugasan] + SKOR[kehadiran]
    with st.expander("📈 Lihat Butiran Skor"):
        col_a, col_b, col_c, col_d, col_e = st.columns(5)
        col_a.metric("Ujian", f"{SKOR[ujian]}/2")
        col_b.metric("Kuiz", f"{SKOR[kuiz]}/2")
        col_c.metric("Tugasan", f"{SKOR[tugasan]}/2")
        col_d.metric("Kehadiran", f"{SKOR[kehadiran]}/2")
        col_e.metric("Jumlah", f"{jumlah_skor}/8")
