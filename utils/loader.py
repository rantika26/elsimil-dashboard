import pandas as pd

FILES = {
    "CATIN": "data/CATIN.xlsx",
    "BADUTA": "data/BADUTA.xlsx",
    "BUMIL": "data/BUMIL.xlsx"
}

def get_sheet_names(jenis):
    excel = pd.ExcelFile(FILES[jenis])
    return excel.sheet_names


def load_data(jenis, kabupaten):

    excel = pd.ExcelFile(FILES[jenis])

    # Kalau memilih Semua Kabupaten → pakai sheet BABEL
    if kabupaten == "Semua Kabupaten":
        sheet = "BABEL"

    else:
        # Cari nama sheet yang cocok (tidak peduli huruf besar/kecil)
        daftar_sheet = excel.sheet_names

        sheet = None

        for s in daftar_sheet:
            if s.strip().upper() == kabupaten.strip().upper():
                sheet = s
                break

        # Kalau tidak ketemu, tampilkan semua nama sheet
        if sheet is None:
            raise Exception(
                f"Sheet '{kabupaten}' tidak ditemukan.\n\n"
                f"Daftar sheet:\n{daftar_sheet}"
            )

    df = pd.read_excel(
        FILES[jenis],
        sheet_name=sheet
    )

    df.columns = df.columns.astype(str).str.strip()

    return df