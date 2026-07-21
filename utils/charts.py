import pandas as pd
import plotly.express as px

bulan = ["JAN", "FEB", "MAR", "APR", "MEI", "JUN"]

# ===============================
# STYLE GRAFIK
# ===============================

def style_chart(fig):
    fig.update_layout(
        template="simple_white",
        paper_bgcolor="#FFF8DE",
        plot_bgcolor="#FFF8DE",
        font=dict(
            family="Segoe UI",
            size=13,
            color="#444444"
        ),
        title_x=0.5,
        margin=dict(l=20, r=20, t=60, b=20),
        height=430
    )

    return fig


# ===============================
# GRAFIK TREND
# ===============================
def grafik_tren(df, bulan):

    data = []

    for b in ["JAN","FEB","MAR","APR","MEI","JUN"]:

        nilai = pd.to_numeric(
            df[b],
            errors="coerce"
        ).fillna(0).sum()

        data.append(nilai)

    fig = px.line(
        x=["JAN","FEB","MAR","APR","MEI","JUN"],
        y=data,
        markers=True,
        title="Trend Entry"
    )

    return style_chart(fig)

# ===============================
# TOP 10 DESA
# ===============================

def grafik_top_desa(df):

    temp = df.copy()

    temp["TOTAL"] = (
        temp[bulan]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
        .sum(axis=1)
    )

    desa = (
        temp.groupby("DESA/KEL")["TOTAL"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        desa,
        x="TOTAL",
        y="DESA/KEL",
        orientation="h",
        text="TOTAL",
        title="10 Desa Entry Tertinggi"
    )

    fig.update_traces(
        marker_color="#8CA9FF",
        textposition="outside"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    return style_chart(fig)


# ===============================
# BOTTOM 10 DESA
# ===============================

def grafik_bottom_desa(df):

    temp = df.copy()

    temp[bulan] = (
        temp[bulan]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
    )

    temp["TOTAL"] = temp[bulan].sum(axis=1)

    desa = (
        temp.groupby("DESA/KEL")["TOTAL"]
        .sum()
        .reset_index()
    )

    # Hilangkan desa dengan total 0 (opsional)
    desa = desa[desa["TOTAL"] > 0]

    desa = (
        desa.sort_values("TOTAL")
        .head(10)
    )

    fig = px.bar(
        desa,
        x="TOTAL",
        y="DESA/KEL",
        orientation="h",
        text="TOTAL",
        title="10 Desa Entry Terendah"
    )

    fig.update_traces(
        marker_color="#AAC4F5",
        textposition="outside"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total descending")
    )

    return style_chart(fig)


# ===============================
# GRAFIK KECAMATAN
# ===============================

def grafik_kecamatan(df):

    temp = df.copy()

    temp["TOTAL"] = (
        temp[bulan]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
        .sum(axis=1)
    )

    kec = (
        temp.groupby("KECAMATAN")["TOTAL"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        kec,
        x="KECAMATAN",
        y="TOTAL",
        text="TOTAL",
        title="Jumlah Entry per Kecamatan"
    )

    fig.update_traces(
        marker_color="#AAC4F5",
        textposition="outside"
    )

    return style_chart(fig)

import plotly.graph_objects as go

def grafik_keaktifan_tpk(df):

    data = df.sort_values("PERSEN", ascending=False)

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=data["DESA/KEL"],
            x=data["AKTIF"],
            orientation="h",
            name="Aktif",
            marker_color="#8CA9FF",
            text=data["AKTIF"],
            textposition="inside"
        )
    )

    fig.add_trace(
        go.Bar(
            y=data["DESA/KEL"],
            x=data["TIDAK_AKTIF"],
            orientation="h",
            name="Belum Aktif",
            marker_color="#FFF2C6",
            text=data["TIDAK_AKTIF"],
            textposition="inside"
        )
    )

    fig.update_layout(

        title="Sebaran Keaktifan TPK per Desa",

        barmode="stack",

        height=max(500, len(data)*28),

        paper_bgcolor="#FFF8DE",

        plot_bgcolor="#FFF8DE",

        legend_title="Status",

        xaxis_title="Jumlah TPK",

        yaxis_title=""
    )

    return fig
