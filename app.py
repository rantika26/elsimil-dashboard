import streamlit as st

from utils.loader import load_data
from utils.metrics import hitung_kpi
from utils.charts import (
    grafik_tren,
    grafik_top_desa,
    grafik_bottom_desa,
    grafik_kecamatan
)

st.set_page_config(
    page_title="Dashboard Monitoring ELSIMIL",
    layout="wide"
)
st.markdown("""
<style>

/* ===========================
BACKGROUND
=========================== */

.stApp{
    background-color:#FFF8DE;
}

/* ===========================
SIDEBAR
=========================== */

[data-testid="stSidebar"]{
    background-color:#FFF2C6;
    border-right:2px solid #AAC4F5;
}

/* ===========================
KPI CARD
=========================== */

[data-testid="metric-container"]{
    background:#FFF2C6;
    border:1px solid #AAC4F5;
    border-radius:14px;
    padding:18px;
    box-shadow:0px 3px 8px rgba(0,0,0,.08);
}

[data-testid="metric-container"]:hover{
    border:1px solid #8CA9FF;
}

/* ===========================
JUDUL KPI
=========================== */

[data-testid="metric-container"] label{
    font-size:15px;
    font-weight:600;
}

/* ===========================
BUTTON
=========================== */

.stButton button{

    background:#AAC4F5;
    color:#222;
    border-radius:10px;
    border:none;
}

.stButton button:hover{

    background:#8CA9FF;
    color:white;
}

/* ===========================
SELECTBOX
=========================== */

.stSelectbox div[data-baseweb="select"]{

    background:#FFF2C6;
    border-radius:10px;
}

/* ===========================
DATAFRAME
=========================== */

[data-testid="stDataFrame"]{

    border:1px solid #AAC4F5;
    border-radius:10px;
}

/* ===========================
HEADERS
=========================== */

h1{

    color:#2F3A56;
    font-weight:700;
}

h2,h3{

    color:#43536F;
}

</style>

""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align:center;'>
Dashboard Monitoring Entry ELSIMIL
</h1>

<p style='text-align:center;
color:#555;
font-size:18px;'>

BKKBN Provinsi Kepulauan Bangka Belitung

</p>

""",unsafe_allow_html=True)

st.write("")

# =====================
# SIDEBAR
# =====================

st.sidebar.markdown("## Dashboard")

st.sidebar.caption(
"Monitoring Entry ELSIMIL"
)

st.sidebar.divider()

st.sidebar.subheader("Filter Data")

jenis = st.sidebar.selectbox(
    "Jenis Data",
    ["CATIN","BADUTA","BUMIL"]
)

kabupaten = st.sidebar.selectbox(
    "Kabupaten",
    [
        "Semua Kabupaten",
        "BANGKA",
        "BABAR",
        "BATENG",
        "BASEL",
        "BELITUNG",
        "BELTIM",
        "PK.PINANG"
    ]
)
st.sidebar.divider()

st.sidebar.info(
"""
Gunakan filter untuk melihat
monitoring Entry ELSIMIL berdasarkan
jenis data dan wilayah.
"""
)
st.subheader("Ringkasan Data")
# =====================
# LOAD DATA
# =====================

df = load_data(jenis, kabupaten)

# =====================
# KPI
# =====================

total_entry,total_desa,total_kecamatan,rata = hitung_kpi(df)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Entry",
    f"{int(total_entry):,}"
)

col2.metric(
    "Total Desa",
    total_desa
)

col3.metric(
    "Total Kecamatan",
    total_kecamatan
)

col4.metric(
    "Rata-rata Entry",
    rata
)
st.divider()
st.write("")
st.subheader("Visualisasi Data")
# =====================
# GRAFIK
# =====================

st.plotly_chart(
    grafik_tren(df),
    use_container_width=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        grafik_top_desa(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        grafik_bottom_desa(df),
        use_container_width=True
    )

st.plotly_chart(
    grafik_kecamatan(df),
    use_container_width=True
)
# =====================
# DATA
# =====================

st.subheader("Data Monitoring")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
st.divider()

st.markdown(
"""
<div style="text-align:center;
color:gray;
font-size:14px;">

Dashboard Monitoring Entry ELSIMIL<br>
BKKBN Provinsi Kepulauan Bangka Belitung

</div>
""",
unsafe_allow_html=True
)