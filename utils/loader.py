from utils.spreadsheet import buka_sheet


def load_data(jenis):

    if jenis == "CATIN":
        return buka_sheet("CATIN_BABEL")

    elif jenis == "BADUTA":
        return buka_sheet("BADUTA_BABEL")

    elif jenis == "BUMIL":
        return buka_sheet("BUMIL_BABEL")