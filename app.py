import streamlit as st

from utils.loader import load_data

# ===========================
# KPI
# ===========================

from utils.metrics import hitung_kpi

# ===========================
# CHART
# ===========================

from utils.charts import (
    grafik_tren,
    grafik_top_desa,
    grafik_bottom_desa,
    grafik_kecamatan
)


# ===========================
# PARTISIPASI
# ===========================

from utils.partisipasi import (
    hitung_partisipasi
)

st.set_page_config(
    page_title="Dashboard Monitoring ELSIMIL",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background:#FFF8DE;
}

[data-testid="stSidebar"]{
    background:#FFF2C6;
}

[data-testid="metric-container"]{
    border-radius:15px;
}

</style>
""",unsafe_allow_html=True)

st.title("Dashboard Monitoring Entry ELSIMIL")

st.caption(
    "BKKBN Provinsi Kepulauan Bangka Belitung"
)

st.divider()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("Dashboard")
st.sidebar.markdown("---")

jenis = st.sidebar.selectbox(

    "Jenis Modul Pendampingan",

    [
        "CATIN",
        "BADUTA",
        "BUMIL"
    ]
)
# ==========================================
# LOAD DATA DARI GOOGLE SPREADSHEET
# ==========================================

df = load_data(jenis)
# ==========================================
# FILTER SIDEBAR
# ==========================================
# ==========================================
# FILTER
# ==========================================

kabupaten_list = sorted(
    df["KABUPATEN"]
    .dropna()
    .unique()
)

kabupaten = st.sidebar.selectbox(
    "Kabupaten",
    ["Semua Kabupaten"] + kabupaten_list
)

# -----------------------------------------

df_kec = df.copy()

if kabupaten != "Semua Kabupaten":
    df_kec = df_kec[
        df_kec["KABUPATEN"] == kabupaten
    ]

kecamatan_list = sorted(
    df_kec["KECAMATAN"]
    .dropna()
    .unique()
)

kecamatan = st.sidebar.selectbox(
    "Kecamatan",
    ["Semua Kecamatan"] + kecamatan_list
)

# -----------------------------------------

df_desa = df_kec.copy()

if kecamatan != "Semua Kecamatan":
    df_desa = df_desa[
        df_desa["KECAMATAN"] == kecamatan
    ]

desa_list = sorted(
    df_desa["DESA/KEL"]
    .dropna()
    .unique()
)

desa = st.sidebar.selectbox(
    "Desa/Kelurahan",
    ["Semua Desa"] + desa_list
)

# -----------------------------------------

bulan = st.sidebar.selectbox(
    "Bulan Pendampingan",
    [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MEI",
        "JUN"
    ]
)
# ===============================
# FILTER DATA
# ===============================

if kabupaten != "Semua Kabupaten":

    df = df[
        df["KABUPATEN"] == kabupaten
    ]

if kecamatan != "Semua Kecamatan":

    df = df[
        df["KECAMATAN"] == kecamatan
    ]

if desa != "Semua Desa":

    df = df[
        df["DESA/KEL"] == desa
    ]
# ==========================================
# HITUNG KPI
# ==========================================
(
    jumlah_tpk_pendampingan,
    jumlah_tpk,
    persentase,
    jumlah_entry
) = hitung_kpi(
    df,
    bulan
)
# ==========================
# KPI CARD
# ==========================

if desa == "Semua Desa":

    c1,c2,c3 = st.columns(3)

    with c1:
        st.metric(
            "Jumlah TPK yang Melakukan Pendampingan",
            jumlah_tpk_pendampingan
        )

    with c2:
        st.metric(
            "Jumlah Keseluruhan TPK",
            jumlah_tpk
        )

    with c3:
        st.metric(
            "Jumlah Entry Pendampingan (Januari–Juni)",
            jumlah_entry
        )

else:

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric(
            "Jumlah TPK yang Melakukan Pendampingan",
            jumlah_tpk_pendampingan
        )

    with c2:
        st.metric(
            "Jumlah Keseluruhan TPK",
            jumlah_tpk
        )

    with c3:
        st.metric(
            "Persentase Partisipasi TPK",
            f"{persentase}%"
        )

    with c4:
        st.metric(
            "Jumlah Entry Pendampingan (Januari–Juni)",
            jumlah_entry
        )

st.plotly_chart(
    grafik_tren(df,bulan),
    use_container_width=True,
    key="trend"
)

st.plotly_chart(
    grafik_top_desa(df),
    use_container_width=True,
    key="topdesa"
)

st.plotly_chart(
    grafik_bottom_desa(df),
    use_container_width=True,
    key="bottomdesa"
)

st.plotly_chart(
    grafik_kecamatan(df),
    use_container_width=True,
    key="kecamatan"
)
#st.dataframe(df)