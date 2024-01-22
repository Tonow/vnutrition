SOURCE_FILE="data/Table Ciqual 2020_FR_2020 07 07.xls"
ALIM_GRP_CODE_TO_DROP=[1, 8, 11]
ALIM_SSGRP_CODE_TO_DROP=[401,402,403,404,405,406,407,408,409,410,501, 503, 504, 601, 603, 702, 703, 705, 706, 708, 709, 901, 904, 905, 1003, 1008]
ALIM_SSSSGRP_CODE_TO_DROP=[50204, 50203, 50202, 50201, 100103]
TYPE_CASE = ["femme", "enfant", "homme", "grossesse", "allaitement"]
APPORT_QTY = {
    "Besoin moyen estimatif": "BME",
    "Apport nutritionnel recommandé": "ANR",
    "Apport suffisant": "AS",
    "Apport maximal tolérable": "AMT",
    "Besoin énergétique estimatif": "BÉE",
    "Risque réduit de maladies chroniques": "RRMC",
}
APPORT_README_PATH = 'apport'
