from os import path

FER_CLN = "Fer (mg/100 g)"
NAME = "alim_nom_fr"
ALIM_SSGRP_NOM_FR = "alim_ssgrp_nom_fr"
CIQUAL_FILE = path.join("data", "Table Ciqual 2020_FR_2020 07 07.xls")
ALIM_GRP_CODE_TO_DROP = [1, 8, 11]
ALIM_SSGRP_CODE_TO_DROP = [
    401,
    402,
    403,
    404,
    405,
    406,
    407,
    408,
    409,
    410,
    501,
    503,
    504,
    601,
    603,
    702,
    703,
    705,
    706,
    708,
    709,
    901,
    904,
    905,
    1003,
    1008,
]
ALIM_SSSSGRP_CODE_TO_DROP = [50204, 50203, 50202, 50201, 100103]
STRINGS_TO_DROP = ["(", ")", "/", "jour"]
NEEDS_COL = "Besoin"
PART_SIZE = "Portion g"
