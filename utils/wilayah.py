import re
import pandas as pd


# ==========================================
# NORMALISASI TEKS
# ==========================================

def bersihkan(teks):

    if pd.isna(teks):
        return ""

    teks = str(teks).upper()

    teks = teks.replace(".", " ")
    teks = teks.replace("/", " ")
    teks = teks.replace("-", " ")

    teks = re.sub(r"\s+", " ", teks)

    return teks.strip()
# ==========================================
# NAMA DASHBOARD
# ==========================================

def normalisasi_kabupaten(nama):

    nama = normalisasi_teks(nama)

    if "BABAR" in nama or "BANGKA BARAT" in nama:
        return "BANGKA BARAT"

    if "BASEL" in nama or "BANGKA SELATAN" in nama:
        return "BANGKA SELATAN"

    if "BATENG" in nama or "BANGKA TENGAH" in nama:
        return "BANGKA TENGAH"

    if "BELTIM" in nama or "BELITUNG TIMUR" in nama:
        return "BELITUNG TIMUR"

    if (
        "PK PINANG" in nama
        or
        "PKPINANG" in nama
        or
        "PANGKAL PINANG" in nama
        or
        "KOTA PANGKAL PINANG" in nama
    ):
        return "PANGKAL PINANG"

    if "BELITUNG" in nama:
        return "BELITUNG"

    if "BANGKA" in nama:
        return "BANGKA"

    return nama


# ==========================================
# DASHBOARD -> SHEET
# ==========================================

def normalisasi_kabupaten(nama):

    nama = bersihkan(nama)

    if "BABAR" in nama or "BANGKA BARAT" in nama:
        return "BABAR"

    if "BASEL" in nama or "BANGKA SELATAN" in nama:
        return "BASEL"

    if "BATENG" in nama or "BANGKA TENGAH" in nama:
        return "BATENG"

    if "BELTIM" in nama or "BELITUNG TIMUR" in nama:
        return "BELTIM"

    if (
        "PANGKAL PINANG" in nama
        or "PK PINANG" in nama
        or "PKPINANG" in nama
        or "KOTA PANGKAL PINANG" in nama
    ):
        return "PK.PINANG"

    if "BELITUNG" == nama:
        return "BELITUNG"

    if "BANGKA" == nama:
        return "BANGKA"

    return nama
# ==========================================
# KECAMATAN
# ==========================================

def normalisasi_kecamatan(nama):

    return bersihkan(nama)

# ==========================================
# DESA
# ==========================================
def normalisasi_desa(nama):

    return bersihkan(nama)

# ==========================================
# NORMALISASI DATAFRAME
# ==========================================

def normalisasi_dataframe(df):

    df.columns = (
        df.columns
        .astype(str)
        .str.upper()
        .str.strip()
    )

    for kolom in ["KABUPATEN","KECAMATAN","DESA/KEL"]:

        if kolom in df.columns:

            df[kolom] = (
                df[kolom]
                .fillna("")
                .astype(str)
                .str.upper()
                .str.strip()
                .str.replace("\n","",regex=False)
                .str.replace("\r","",regex=False)
                .str.replace("\t","",regex=False)
                .str.replace(r"\s+"," ",regex=True)
            )

    return df
# ==========================================
# KONVERSI NAMA KABUPATEN -> NAMA SHEET EXCEL
# ==========================================

def kabupaten_ke_sheet(kabupaten):

    kabupaten = normalisasi_kabupaten(kabupaten)

    mapping = {

        "BANGKA": "BANGKA",

        "BANGKA BARAT": "BABAR",

        "BANGKA SELATAN": "BASEL",

        "BANGKA TENGAH": "BATENG",

        "BELITUNG": "BELITUNG",

        "BELITUNG TIMUR": "BELTIM",

        "PANGKAL PINANG": "PK.PINANG"

    }

    return mapping.get(kabupaten, kabupaten)