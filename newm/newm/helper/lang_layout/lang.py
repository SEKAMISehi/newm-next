import os
import socket
import json
from newm.layout import Layout
home_dir = os.path.expanduser("~")
SOCKET_PATH = f"{home_dir}/.config/newm/sockets/lang.sock"
def QS_current_lang(command, data=None):
    # Создаём клиентский сокет
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(SOCKET_PATH)

        # Формируем запрос
        request = {"command": command}
        if data is not None:
            request["data"] = data

        # Отправляем запрос
        client.sendall(json.dumps(request).encode("utf-8"))

        # Получаем ответ
        response = client.recv(1024).decode("utf-8")
        return json.loads(response)
    # Установка значения переменной
def QS_current_lang_update(lang_layout):
    get_response = QS_current_lang("get_lang")
    langs = get_response["data"]
    lang_id = langs["lang_id"]
    lang_id = lang_id+1
    max_elem = len(lang_layout)-1
    if lang_id > max_elem:
        lang_id = 0
    lang_layout_chose = lang_layout[lang_id]
    QS_current_lang("set_lang", {"text": lang_layout_chose, "class": "lang_neutral","lang_id":lang_id})
    return True

def QS_xkb_layout():
    get_response = QS_current_lang("get_lang")
    langs = get_response["data"]
    lang_name = langs["text"]
    return lang_name

def QS_xkb_variant(variant_base):
    get_response = QS_current_lang("get_lang")
    langs = get_response["data"]
    lang_name = langs["text"]
    if lang_name in variant_base:
        variant = variant_base[lang_name]
    else:
        variant = ""
    return variant
