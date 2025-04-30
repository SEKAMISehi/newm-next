from __future__ import annotations
from typing import TypeVar, Optional, Callable, Any, Generic, Union, cast
#imports
import os
import subprocess
import pathlib
import importlib
import sys
#home_directory, and import manage_energy configuration
module_path = "~/.config/newm"
module_path = os.path.expanduser(module_path)

path_file = os.path.expanduser("~/.config/newm/QS_layoyts.py")
if os.path.exists(path_file):
    sys.path.append(module_path)
    import QS_layoyts
    letters = QS_layoyts.letters
else:
    path_file = os.path.expanduser("/etc/newm/QS_layoyts.py")
    module_path = "/etc/newm/"
    module_path = os.path.expanduser(module_path)
    if os.path.exists(path_file):
        sys.path.append(module_path)
        import QS_layoyts
        letters = QS_layoyts.letters
    else:
        letters = {
        # Keysyms для QWERTY
            'english:us' : ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','bracketleft', 'bracketright', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','semicolon', 'apostrophe', 'backslash', 'z', 'x', 'c', 'v', 'b', 'n', 'm','comma', 'period', 'slash'],
            # Keysyms для русской раскладки
            'russian:none' : ['Cyrillic_shorti', 'Cyrillic_tse', 'Cyrillic_u', 'Cyrillic_ka', 'Cyrillic_ie', 'Cyrillic_en', 'Cyrillic_ghe', 'Cyrillic_sha','Cyrillic_shcha', 'Cyrillic_ze', 'Cyrillic_ha', 'Cyrillic_hardsign', 'Cyrillic_ef', 'Cyrillic_yeru', 'Cyrillic_ve', 'Cyrillic_a','Cyrillic_pe', 'Cyrillic_er', 'Cyrillic_o', 'Cyrillic_el', 'Cyrillic_de', 'Cyrillic_zhe', 'Cyrillic_e', 'backslash','Cyrillic_ya', 'Cyrillic_che', 'Cyrillic_es', 'Cyrillic_em', 'Cyrillic_i', 'Cyrillic_te', 'Cyrillic_softsign', 'Cyrillic_be','Cyrillic_yu', 'period'],

            # Keysyms для украинской раскладки
            'ukrainian:none' : ['Cyrillic_shorti', 'Cyrillic_tse', 'Cyrillic_u', 'Cyrillic_ka', 'Cyrillic_ie', 'Cyrillic_en', 'Cyrillic_ghe', 'Cyrillic_sha', 'Cyrillic_shcha', 'Cyrillic_ze', 'Cyrillic_ha', 'Ukrainian_yi', 'Cyrillic_ef', 'Ukrainian_i', 'Cyrillic_ve', 'Cyrillic_a', 'Cyrillic_pe', 'Cyrillic_er', 'Cyrillic_o', 'Cyrillic_el', 'Cyrillic_de', 'Cyrillic_zhe', 'Ukrainian_ie', 'backslash', 'Cyrillic_ya', 'Cyrillic_che', 'Cyrillic_es', 'Cyrillic_em', 'Cyrillic_i', 'Cyrillic_te', 'Cyrillic_softsign', 'Cyrillic_be','Cyrillic_yu', 'Ukrainian_ghe_with_upturn', 'period'],
            # Keysyms для японской раскладки
            'japanese:kana' : ['kana_TA', 'kana_TE', 'kana_I', 'kana_SU', 'kana_KA', 'kana_N', 'kana_NA', 'kana_NI', 'kana_RA', 'kana_SE', 'voicedsound', 'semivoicedsound', 'kana_CHI', 'kana_TO', 'kana_SHI', 'kana_HA', 'kana_KI', 'kana_KU', 'kana_MA', 'kana_NO', 'kana_RI', 'kana_RE', 'kana_KE', 'kana_MU', 'kana_TSU', 'kana_SA', 'kana_SO', 'kana_HI', 'kana_KO', 'kana_MI','kana_MO', 'kana_NE', 'kana_RU', 'kana_ME'
            ],
        }
