import pandas as pd

from utils.wilayah import (
    normalisasi_kabupaten,
    normalisasi_kecamatan,
    normalisasi_desa
)

FILE_MASTER = "data/JUMLAH TPK.xlsx"


# ==========================================
# LOAD DATA
# ==========================================

def load_master():

    df = pd.read_excel(FILE_MASTER)

    # isi merge cell
    df["NAMA KABUPATEN"] = df["NAMA KABUPATEN"].ffill()

    # --------------------------
    # Normalisasi Kabupaten
    # --------------------------
    df["NAMA KABUPATEN"] = (
        df["NAMA KABUPATEN"]
        .apply(normalisasi_kabupaten)
    )

    # --------------------------
    # Normalisasi Kecamatan
    # --------------------------
    df["NAMA KECAMATAN"] = (
        df["NAMA KECAMATAN"]
        .fillna("")
        .apply(normalisasi_kecamatan)
    )

    # --------------------------
    # Normalisasi Desa
    # --------------------------
    df["NAMA KELURAHAN/DESA"] = (
        df["NAMA KELURAHAN/DESA"]
        .fillna("")
        .apply(normalisasi_desa)
    )

    return df


# ==========================================
# KABUPATEN
# ==========================================

def get_kabupaten(df):

    return [
        "BANGKA",
        "BANGKA BARAT",
        "BANGKA SELATAN",
        "BANGKA TENGAH",
        "BELITUNG",
        "BELITUNG TIMUR",
        "PANGKAL PINANG"
    ]

# ==========================================
# KECAMATAN
# ==========================================

def get_kecamatan(df, kabupaten):

    kabupaten = normalisasi_kabupaten(kabupaten)

    data = df[
        df["NAMA KABUPATEN"] == kabupaten
    ]

    return sorted(
        data["NAMA KECAMATAN"]
        .dropna()
        .unique()
        .tolist()
    )


# ==========================================
# DESA
# ==========================================

def get_desa(df, kabupaten, kecamatan):

    kabupaten = normalisasi_kabupaten(kabupaten)
    kecamatan = normalisasi_kecamatan(kecamatan)

    data = df[
        (df["NAMA KABUPATEN"] == kabupaten)
        &
        (df["NAMA KECAMATAN"] == kecamatan)
    ]

    return sorted(
        data["NAMA KELURAHAN/DESA"]
        .dropna()
        .unique()
        .tolist()
    )
# ==========================================
# TOTAL TPK
# ==========================================
def get_total_tpk(df, kabupaten=None, kecamatan=None, desa=None):

    hasil = df.copy()

    if kabupaten and kabupaten != "Semua Kabupaten":

        hasil = hasil[
            hasil["NAMA KABUPATEN"] ==
            normalisasi_kabupaten(kabupaten)
        ]

    if kecamatan and kecamatan != "Semua Kecamatan":

        hasil = hasil[
            hasil["NAMA KECAMATAN"] ==
            normalisasi_kecamatan(kecamatan)
        ]

    if desa and desa != "Semua Desa":

        hasil = hasil[
            hasil["NAMA KELURAHAN/DESA"] ==
            normalisasi_desa(desa)
        ]

    if hasil.empty:
        return 0

    return int(
        hasil["JUMLAH TPK"].sum()
    )