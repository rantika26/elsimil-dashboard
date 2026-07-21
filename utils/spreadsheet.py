import gspread
import pandas as pd

from google.oauth2.service_account import Credentials
from gspread_dataframe import get_as_dataframe

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

SERVICE_ACCOUNT = "service_account.json"

SPREADSHEET_ID = "1Zcy1pB5r1mPYzIqdy8OYHQb9YJmbIvPOokxPCL_KkZM"


def buka_sheet(nama_sheet):

    # Login ke Google Spreadsheet
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT,
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    spreadsheet = client.open_by_key(
        SPREADSHEET_ID
    )

    worksheet = spreadsheet.worksheet(
        nama_sheet
    )

    # Ambil data menjadi DataFrame
    df = get_as_dataframe(
        worksheet,
        evaluate_formulas=True,
        dtype=str
    )

    # Hapus baris kosong
    df = df.dropna(how="all")

    # Rapikan nama kolom
    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.upper()
    )

    # Isi nilai kosong
    df = df.fillna("")

    # Kolom numerik
    kolom_angka = [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MEI",
        "JUN",
        "TOTAL",
        "JUMLAH TPK"
    ]

    # Ubah menjadi integer
    for k in kolom_angka:

        if k in df.columns:

            df[k] = (
                pd.to_numeric(
                    df[k],
                    errors="coerce"
                )
                .fillna(0)
                .astype(int)
            )

    return df