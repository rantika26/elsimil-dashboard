import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

bulan = ["JAN", "FEB", "MAR", "APR", "MEI", "JUN"]


# =====================================================
# STYLE GRAFIK
# =====================================================

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

        margin=dict(

            l=20,

            r=20,

            t=70,

            b=20

        )

    )

    return fig


# =====================================================
# GRAFIK RANKING WILAYAH
# =====================================================

def grafik_tren(df, bulan_filter, kabupaten, kecamatan):

    temp = df.copy()

    temp[bulan_filter] = (

        pd.to_numeric(

            temp[bulan_filter],

            errors="coerce"

        )

        .fillna(0)

    )

    nama_bulan = {

        "JAN":"Januari",

        "FEB":"Februari",

        "MAR":"Maret",

        "APR":"April",

        "MEI":"Mei",

        "JUN":"Juni"

    }

    bulan_lengkap = nama_bulan.get(

        bulan_filter,

        bulan_filter

    )

    # =======================================
    # Semua Kabupaten
    # =======================================

    if kabupaten == "Semua Kabupaten":

        hasil = (

            temp

            .groupby("KABUPATEN")[bulan_filter]

            .sum()

            .reset_index()

            .sort_values(

                by=bulan_filter,

                ascending=False

            )

        )

        kolom = "KABUPATEN"

        judul = (

            "Capaian Entry 7 Kabupaten/Kota\n"

            f"Bulan {bulan_lengkap}"

        )

    # =======================================
    # Semua Kecamatan
    # =======================================

    elif kecamatan == "Semua Kecamatan":

        hasil = (

            temp

            .groupby("KECAMATAN")[bulan_filter]

            .sum()

            .reset_index()

            .sort_values(

                by=bulan_filter,

                ascending=False

            )

        )

        kolom = "KECAMATAN"

        judul = (

            f"Capaian Kecamatan Kabupaten {kabupaten}\n"

            f"Bulan {bulan_lengkap}"

        )

    # =======================================
    # Semua Desa
    # =======================================

    else:

        hasil = (

            temp

            .groupby("DESA/KEL")[bulan_filter]

            .sum()

            .reset_index()

            .sort_values(

                by=bulan_filter,

                ascending=False

            )

        )

        kolom = "DESA/KEL"

        judul = (

            f"Capaian Desa/Kelurahan Kecamatan {kecamatan}\n"

            f"Bulan {bulan_lengkap}"

        )

    #hasil = hasil[

    #    hasil[bulan_filter] > 0

    #]

    fig = px.bar(

        hasil,

        x=bulan_filter,

        y=kolom,

        orientation="h",

        text=bulan_filter,

        title=judul

    )

    fig.update_traces(

        marker_color="#8CA9FF",

        textposition="outside"

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        ),

        xaxis_title="Jumlah Entry",

        yaxis_title="",

        height=max(

            450,

            len(hasil) * 35

        )

    )

    return style_chart(fig)

# =====================================================
# TOP 10 DESA
# =====================================================

def grafik_top_desa(df):

    temp = df.copy()

    temp[bulan] = (
        temp[bulan]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
    )

    temp["TOTAL"] = temp[bulan].sum(axis=1)

    desa = (
        temp
        .groupby("DESA/KEL")["TOTAL"]
        .sum()
        .reset_index()
        .sort_values(
            by="TOTAL",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(

        desa,

        x="TOTAL",

        y="DESA/KEL",

        orientation="h",

        text="TOTAL",

        title="10 Desa/Kelurahan Entry Tertinggi"

    )

    fig.update_traces(

        marker_color="#8CA9FF",

        textposition="outside"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )

    )

    return style_chart(fig)


# =====================================================
# BOTTOM 10 DESA
# =====================================================

def grafik_bottom_desa(df):

    temp = df.copy()

    temp[bulan] = (
        temp[bulan]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
    )

    temp["TOTAL"] = temp[bulan].sum(axis=1)

    desa = (
        temp
        .groupby("DESA/KEL")["TOTAL"]
        .sum()
        .reset_index()
    )

    desa = desa[
        desa["TOTAL"] > 0
    ]

    desa = (
        desa
        .sort_values(
            by="TOTAL",
            ascending=True
        )
        .head(10)
    )

    fig = px.bar(

        desa,

        x="TOTAL",

        y="DESA/KEL",

        orientation="h",

        text="TOTAL",

        title="10 Desa/Kelurahan Entry Terendah"

    )

    fig.update_traces(

        marker_color="#AAC4F5",

        textposition="outside"

    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total descending"
        )

    )

    return style_chart(fig)


# =====================================================
# GRAFIK KECAMATAN
# =====================================================

def grafik_kecamatan(df):

    temp = df.copy()

    temp[bulan] = (
        temp[bulan]
        .apply(pd.to_numeric, errors="coerce")
        .fillna(0)
    )

    temp["TOTAL"] = temp[bulan].sum(axis=1)

    kec = (
        temp
        .groupby("KECAMATAN")["TOTAL"]
        .sum()
        .reset_index()
        .sort_values(
            by="TOTAL",
            ascending=False
        )
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

    fig.update_layout(

        xaxis_title="",

        yaxis_title="Jumlah Entry"

    )

    return style_chart(fig)


# =====================================================
# GRAFIK KEAKTIFAN TPK
# =====================================================

def grafik_keaktifan_tpk(df):

    data = df.copy()

    if "PERSEN" not in data.columns:
        return go.Figure()

    data = data.sort_values(
        "PERSEN",
        ascending=False
    )

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

        title="Sebaran Keaktifan TPK",

        barmode="stack",

        height=max(
            500,
            len(data) * 28
        ),

        paper_bgcolor="#FFF8DE",

        plot_bgcolor="#FFF8DE",

        legend_title="Status",

        xaxis_title="Jumlah TPK",

        yaxis_title=""

    )

    return fig

# =====================================================
# GRAFIK TREN JANUARI - JUNI
# =====================================================

def grafik_tren_bulanan(df):

    temp = df.copy()

    bulan = ["JAN","FEB","MAR","APR","MEI","JUN"]

    for b in bulan:
        temp[b] = pd.to_numeric(
            temp[b],
            errors="coerce"
        ).fillna(0)

    data = pd.DataFrame({

        "Bulan":[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "Mei",
            "Jun"
        ],

        "Jumlah":[
            temp["JAN"].sum(),
            temp["FEB"].sum(),
            temp["MAR"].sum(),
            temp["APR"].sum(),
            temp["MEI"].sum(),
            temp["JUN"].sum()
        ]

    })

    fig = px.bar(

        data,

        x="Bulan",

        y="Jumlah",

        text="Jumlah",

        title="Tren Entry Pendampingan Januari–Juni"

    )

    fig.update_traces(

        marker_color="#AAC4F5",

        textposition="outside"

    )

    fig.update_layout(

        xaxis_title="",

        yaxis_title="Jumlah Entry",

        height=420

    )

    return style_chart(fig)