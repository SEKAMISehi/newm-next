# newm-qs

## Объявление
- Заранее сообщаю, что некоторые детали документации были просто переведены, также с учётом того, что у ментера даного форка нету сенсорных устройств, потому проверить и разрабатывать имеено сенсорные функции не сможем в обозримом будущем.
Также будем заниматся переводом остальной документации от newm-next и провекркой тех функций которые можем проверить.

родительский чат для общения по теме newm [discord](https://discord.gg/GnCsYRWtBq)

[video couteresy of Audrick Yeu](https://www.youtube.com/watch?v=IkriZGyjoeU).

## Текущая редакция

данный проект является форком проета newm-next и скорее всего будет идти своим независимым путём.
Пока-что лицензия сохраняется MIT но в будущем в случае крупный обновлений проект перейдёт на GNU/GPL.
Текущая редакция лицензии: [./LICENSE](./LICENSE)

## идея

**newm-qs** Wayland композитор ориентирован на работу с ноутбуками и сенсорными устройствами. Особеностью данного композитора является отсуствие класического рабочего пространства вместо которого есть только одно безграничное, вы можете размещать бессконечное количество окон на экране без перекрываний одного другим, это получается за счёт того, что пространство выходит далеко за границы видимой области и вы сами можете перемещатся между активными окнамы тем самым смещая фокус видимой области.

Также композитор позволяет использовать приложений в слоях когда одно окно может быть над другим, также есть поддержка плавающих окон которые можно определить в конфигурации. помимо этого все диалоговые приложения по умолчанию являются плавающими, что делает работу данных утилит такой же как и в других композиторах.

также в композиторе есть механизмы масштабирования для изменения размеров окон и для предпросмотра всего рабочего пространства целиком для удобного переключения между окнами.

Для сенсорный экранов:
- Используйте три пальца, чтобы перемещаться по стене
- Используйте четыре пальца, чтобы увеличить (переместить их вверх) или в (вниз)

Чтобы иметь возможность расположить окна полезно, используйте:
- `logo` (по умолчанию, если не настроен иное) + один палец на сенсорной панели для перемещения Windows
- `logo` (по умолчанию, если не настроено иное) + два пальца на сенсорной панели, чтобы изменить степень окна


Чтобы получить быстрый обзор всех окон, просто нажмите клавишу «Логотип» (по умолчанию, если не настроено иное).
Кроме того, с помощью быстрого смахивания 5-кратного панели может быть открыта пусковая панель.

Эти поведения могут (частично) настроены (см. Ниже для настройки). По умолчанию (проверка [default_config.py] (usr/lib/sqwm/default_config.py)), следующие привязки ключей (среди прочих) существуют:

- `logo-hjkl`: передвигаться
- `Лого-UN`: масштаб
- `logo-hjkl`: переместить окна вокруг
- `logo-ctrl-hjkl`: изменить размер окон
- `Logo-F`: переключить полноэкранный вид сфокусированного окна (возможно, изменение размера)
- ...

## Обновления

начальный проект newm-atha работал на версии 0.3 .
его форк newm-next работает на версии 0.4.2 .
Новый форк newm-qs работает на версии 0.4.4 .

цели проекта 
- [ ] Получите патчи с сенсорным экраном для работы с этой версией - newm-next
- [ ] обноввление к новой версии wlroots - текущая цель нового форка
- [x] модификация системы сборки проекта - newm-qs
## update 0.4.4 03.05.2025
- 1. изменена система сборки, теперь pywm и newm собираются вместе с применением make build(по умолчанию).
Build включает в себя механизм сборки программы в директорию make с уже встроенной иерархией (/usr/...)
для установки вам достаточно либо скопировать её в соответсвии с иерархией, либо собрать с помощью соответстующей утилиты для своего дистрибутива пакета с удоволетворением всех зависимостей.
- 2. в связи с обновленной системой сборки был изменён механизм взаимодействия с python. Теперь корень прокекта /usr/lib/sqwm в котором находятся все модули и библиотеки для работы композитора, для совместимости с окружением site-packages используется скрипт-линковщик который линкует содержимое в соответсвующий site-packages.
также если композитор не запускается можно принудительно запускать линковщик использовав флаг "-" при запуске композитора.
линковщик требует для своей работы права sudo.
в случае когда python переходит на новую версию вам нет потребности повторно собирать пакет для работы композитора, он сам при невозможности найти критические библиотеки и модули (newm) будет запускать линковщик который создаст символические ссылки в новую версию site-packages.
- 3. также с версии 0.4.3 повредилась команда "pkill newm" из-за чего для принудительного отключения композитора нужно использовать "pkill python".

## update 0.4.3 11.03.2025
- 1. Изменена система простоя теперь можно самому определять то как система будет вести себя во время простоя и какие комманды выполнять(изменение яркости экрана, блокировка, режим ожидания, прочее). Файл конфигурации: QS_power.py (в домашней директории проекта) либо QS_power_default.py (по умолчанию в директории проекта с базовой конфигурацией)
- 2. Добавлен сокет для мониторинка текущей раскладки клавиатуры, что позволяет работать таким вещам как отображение текущей раскладки на панели, а также для работы обновленого механихма обработки комбинации клавиш позволяющей пользоватся горячими клавишами на русской и других отличных от английской расскладки клавиатур. дополнять схему обработки комбинаций клавиш для других расскладок можно в пользовательском конфигурационом файле QS_layoyts.py . 
- 3. Было изменено поведение работы комбинаций клавил, теперь можно использоать модификаторы без букв для выполнения системных комманд в соответсвии с главным конфигом композитора.
- 4. базовая поддержка комбинаций клавий для других расскладок: база для сопоставления: english:us, другие расскладки с которых происходит подмена символов в нужный формат: russian:none, ukrainian:none, и japanese:kana.

## Установка

### Arch Linux

[Install on Arch linux](doc/install_Arch_Linux.md)

There is a AUR package, `newm-next-git-qs`.

### NixOS (NEEDS TO BE DONE, NOT WORKING)

временно выпилена из сборщика

### установка через pip

make pip

## Использоание

для запуска newm используйте:

```sh
start-newm -d
```

будет создан `$HOME/.cache/newm/newm_log`, прошлые версии переименуются по данному формату: `$HOME/.cache/newm/newm_log.old.$year-$month-$day-$epoch`(временные метки последнего изменения)

флаг `-d` для более подробной отладочной информации 
флаг `-c` для пользовательского главного конфигурационого файла (не влияет на конфигурационные файлы менеджера питания и словаря расскладок).

## кофигурация

### информация по конфигурированию

- изначально композитор ищет конфиг в домашней директории `$HOME/.config/newm/config.py`, если не находит то ищет в etc `/etc/newm/config.py`, если там тоже нет то берёт базовый из корня проекта `default_config.py`.

The `default_config.py` file can be found in the [repo](newm/default_config.py) or on your computer at `/usr/lib/qswm/newm/default_config.py`

скопируйте содержимое в файла в `$HOME/.config/newm/config.py` для дальнейшей его модифицкации под свои нужды.

- базовый конфиг менеджера питания `/usr/lib/qswm/newm/QS_power_default.py`
QS_power также поддерживает домашнюю и общесистменую директории конфигурации `$HOME/.config/newm/QS_power.py`, `/etc/newm/QS_power.py`.

- базовый конфиг словаря сопоставления расскладки клавиатур `/usr/lib/qswm/newm/helper/lang_layout/layouts.py`
QS_layoyts также поддерживает домашнюю и общесистемную директорию конфигураций `$HOME/.config/newm/QS_layoyts.py`, `/etc/newm/QS_layoyts.py` 

### default_config.py
```py
from __future__ import annotations
from typing import Callable, Any

import os
import pwd
import time
import logging
import random
import subprocess

from pywm import (
    PyWM,
    PyWMModifiers,
    PyWMOutput,
    PyWMDownstreamState,
    PYWM_MOD_CTRL,
    PYWM_PRESSED,
    PYWM_MOD_LOGO,
    PYWM_MOD_ALT,
    PYWM_TRANSFORM_90,
    PYWM_TRANSFORM_180,
    PYWM_TRANSFORM_270,
    PYWM_TRANSFORM_FLIPPED,
    PYWM_TRANSFORM_FLIPPED_90,
    PYWM_TRANSFORM_FLIPPED_180,
    PYWM_TRANSFORM_FLIPPED_270,
)
from newm.layout import Layout
from newm.helper import WobRunner, PaCtl

logger = logging.getLogger(__name__)

def on_startup():
    init_service = (
        "export DISPLAY='$DISPLAY'\
        export WAYLAND_DISPLAY='$WAYLAND_DISPLAY'\
        export XDG_CURRENT_DESKTOP='$XDG_CURRENT_DESKTOP'",
    ),

    for service in init_service:
        service = f"{service} &"
        os.system(service),

background = {
    'path': os.path.dirname(os.path.realpath(__file__)) + '/resources/wallpaper.jpg',
    'anim': True
}
corner_radius = 0		#Скругление обоев
anim_time = 0.30		#Общее время анимации
blend_time = 1.0		#Время анимации запуска и выхода
outputs = [
    { 'name': 'eDP-1', 'anim': True },
    { 'name': 'virt-1', 'pos_x': -1280, 'pos_y': 0, 'width': 1280, 'height': 720, 'anim': True }
]

wob_runner = WobRunner("wob -a bottom -M 100")
pactl = PaCtl(0, wob_runner)

def on_startup():
    init_service = (
        "export DISPLAY='$DISPLAY'\
        export WAYLAND_DISPLAY='$WAYLAND_DISPLAY'\
        export XDG_CURRENT_DESKTOP='$XDG_CURRENT_DESKTOP'",
    ),
    for service in init_service:
        service = f"{service} &"
        os.system(service),

pywm = {
    'xkb_layout':'us,ru,jp,ua',
    'xkb_variant': ',,kana,',
    'xkb_options': "grp:alt_shift_toggle",
    'xkb_model': "",
    'enable_xwayland': True,
    'xcursor_size': 16,
    'tap_to_click': True,
    'natural_scroll': False,
    'focus_follows_mouse': True,
    'contstrain_popups_to_toplevel': True,
    'encourage_csd': False,
    'texture_shaders': 'basic',
    'renderer_mode': 'pywm',
}

def key_bindings(layout: Layout) -> list[tuple[str, Callable[[], Any]]]:
    return [
        ("C-A-t", lambda: os.system("kitty &")),
        ("L-q", lambda: layout.close_focused_view()),

        ("L-Left", lambda: layout.move(-1, 0)),
        ("L-Down", lambda: layout.move(0, 1)),
        ("L-Up", lambda: layout.move(0, -1)),
        ("L-Right", lambda: layout.move(1, 0)),

        ("L-s", lambda: layout.move_in_stack(1)),

        ("L-space", lambda: (layout.toggle_fullscreen()) ),
        ("L-S-space", lambda: layout.toggle_focused_view_floating()),

        ("L-equal", lambda: layout.basic_scale(1)),
        ("L-minus", lambda: layout.basic_scale(-1)),
        ("L-KP_Add", lambda: layout.basic_scale(-1)),
        ("L-KP_Subtract", lambda: layout.basic_scale(1)),

        ("L-S-Left", lambda: layout.move_focused_view(-1, 0)),
        ("L-S-Down", lambda: layout.move_focused_view(0, 1)),
        ("L-S-Up", lambda: layout.move_focused_view(0, -1)),
        ("L-S-Right", lambda: layout.move_focused_view(1, 0)),

        ("L-C-Left", lambda: layout.resize_focused_view(-1, 0)),
        ("L-C-Down", lambda: layout.resize_focused_view(0, 1)),
        ("L-C-Up", lambda: layout.resize_focused_view(0, -1)),
        ("L-C-Right", lambda: layout.resize_focused_view(1, 0)),

        ("L-f", lambda: layout.toggle_fullscreen()),
        ("L-", lambda: layout.toggle_overview(only_active_workspace=True)),
        ("L-A-l", lambda: layout.ensure_locked(dim=True)),
        ("C-A-l", lambda: layout.terminate()),

        ("XF86MonBrightnessUp", lambda: os.system("brightnessctl set 2%+ &")),
        ("XF86MonBrightnessDown", lambda: os.system("brightnessctl set 2%- &")),
        ("XF86AudioRaiseVolume", lambda: os.system("wpctl set-volume @DEFAULT_AUDIO_SINK@ 2%+ &")),
        ("XF86AudioLowerVolume", lambda: os.system("wpctl set-volume @DEFAULT_AUDIO_SINK@ 2%- &")),
        ("XF86AudioMute", lambda: os.system("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle &")),
        ("XF86AudioMicMute", lambda: os.system("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle &")),
    ]

panels = {
    'lock': {
        'cmd': 'kitty -e newm-panel-basic lock',
    },
    'launcher': {
        'cmd': 'kitty -e newm-panel-basic launcher'
    },
    'top_bar': {
        'native': {
            'enabled': True,
            'texts': lambda: [
                pwd.getpwuid(os.getuid())[0],
                time.strftime("%c"),
                subprocess.check_output(["/usr/bin/newm_lang_watch"], text=True).replace('"', '')[:-1]
            ],
        }
    },
    'bottom_bar': {
        'native': {
            'enabled': True,
            'texts': lambda: [
                "newm-qs",
                "version 0.4.4 ALPHA"
            ],
        }
    },
}
```

### QS_power_default
- время в секундах; одна минута = 60 секунд
- QS_operation поддерживает следующие комманды: light, display_off, lock_screen, suspend, hibernate, none
- QS_power_value нужен для работы light и определяет то какой будет яркость. В будущем возможно будут внедрены новые функции для даного предмета.
Он поддерживает как скалярные числа в виде 0-255 так и проценты от 0%-100%, а также их относительные изменения с ипользованием заков "-" и "+" в конце как указано в примере ниже:
```
minute = 60
hour = 60*minute
energy = {
    "QS_idle_times": [minute*10, minute*20, minute*40],
    "QS_operation": {
        minute*10: "light",
        minute*20: "light",
        minute*40: "display_off",
    },
    "QS_power_value": {
        minute*10: "40%-",
        minute*20: "20%-",
    }
}
```
### layouts -> QS_layoyts

letters = {
- Keysyms для основного QWERTY (без него не будет работать система срабатывания комбинаций клавиш на других раскладках)
```
    'english:us' : ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','bracketleft', 'bracketright', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','semicolon', 'apostrophe', 'backslash', 'z', 'x', 'c', 'v', 'b', 'n', 'm','comma', 'period', 'slash'],
```
- Keysyms для русской раскладки
```
    'russian:none' : ['Cyrillic_shorti', 'Cyrillic_tse', 'Cyrillic_u', 'Cyrillic_ka', 'Cyrillic_ie', 'Cyrillic_en', 'Cyrillic_ghe', 'Cyrillic_sha','Cyrillic_shcha', 'Cyrillic_ze', 'Cyrillic_ha', 'Cyrillic_hardsign', 'Cyrillic_ef', 'Cyrillic_yeru', 'Cyrillic_ve', 'Cyrillic_a','Cyrillic_pe', 'Cyrillic_er', 'Cyrillic_o', 'Cyrillic_el', 'Cyrillic_de', 'Cyrillic_zhe', 'Cyrillic_e', 'backslash','Cyrillic_ya', 'Cyrillic_che', 'Cyrillic_es', 'Cyrillic_em', 'Cyrillic_i', 'Cyrillic_te', 'Cyrillic_softsign', 'Cyrillic_be','Cyrillic_yu', 'period'],
```
- Keysyms для украинской раскладки
```
    'ukrainian:none' : ['Cyrillic_shorti', 'Cyrillic_tse', 'Cyrillic_u', 'Cyrillic_ka', 'Cyrillic_ie', 'Cyrillic_en', 'Cyrillic_ghe', 'Cyrillic_sha', 'Cyrillic_shcha', 'Cyrillic_ze', 'Cyrillic_ha', 'Ukrainian_yi', 'Cyrillic_ef', 'Ukrainian_i', 'Cyrillic_ve', 'Cyrillic_a', 'Cyrillic_pe', 'Cyrillic_er', 'Cyrillic_o', 'Cyrillic_el', 'Cyrillic_de', 'Cyrillic_zhe', 'Ukrainian_ie', 'backslash', 'Cyrillic_ya', 'Cyrillic_che', 'Cyrillic_es', 'Cyrillic_em', 'Cyrillic_i', 'Cyrillic_te', 'Cyrillic_softsign', 'Cyrillic_be','Cyrillic_yu', 'Ukrainian_ghe_with_upturn', 'period'],
```
- Keysyms для японской катаканы.
```
    'japanese:kana' : ['kana_TA', 'kana_TE', 'kana_I', 'kana_SU', 'kana_KA', 'kana_N', 'kana_NA', 'kana_NI', 'kana_RA', 'kana_SE', 'voicedsound', 'semivoicedsound', 'kana_CHI', 'kana_TO', 'kana_SHI', 'kana_HA', 'kana_KI', 'kana_KU', 'kana_MA', 'kana_NO', 'kana_RI', 'kana_RE', 'kana_KE', 'kana_MU', 'kana_TSU', 'kana_SA', 'kana_SO', 'kana_HI', 'kana_KO', 'kana_MI','kana_MO', 'kana_NE', 'kana_RU', 'kana_ME'
    ],
}
```

### Configuring

Конфигурация работает путем оценки файла конфигурации Python и извлечения переменных, которые файл экспортирует. Таким образом, в основном вы можете делать все, что вам нужно, чтобы предоставить значения конфигурации,
Следовательно, почему определенные элементы конфигурации являются обратными вызовами. Некоторые элементы являются иерархическими, чтобы установить эти использование DICTS Python - например, для `x.y`:

```py
x = {
    'y': 2.0
}
```

Конфигурация может быть динамически обновлена ​​(кроме пары фиксированных ключей) с использованием `layout.update_config` (по умолчанию, связанным с` mod+c`).

См. [Config] (./ doc/config.md) для документации по всем настраиваемым значениям.

### Troubleshooting: Touchpad

Он очень рекомендуется использовать evdev, а не жесты Python (см. [Config] (./ doc/config.md)), однако они могут не сработать с самого начала. Пытаться:

```
ls -al /dev/input/event*
evtest
```

Это необходимая предпосылка для использования жестов на стороне питона (более плавного). Жесты c-side или dbus не требуют этого.

В качестве примечания, это нет необходимости для композитора Уэйленда в целом, поскольку устройства можно получить через `Systemd-logind` или` seatd` или аналогичный. Однако модуль Python `evdev` не допускает экземпляров с учетом дескриптора файла (только путь, который затем открывается сам),
Таким образом, использование этого модуля больше не будет возможно в этом случае (плюс на первый взгляд нет простого способа получить этот дескриптор файла в сторону питона). Также `wlroots` (`libinput` в бэкэнде) не различает сенсорные панели как то, какие они есть (`touch-down`, `touch-up`, `touch-motion` для любого количества параллельных слотов), но только как указатели (`motion` / `axis`), так что обнаружение жестов вокруг `libinput`-events невозможно тоже.

Поэтому мы застряли с менее безопасным (и намного проще) способом использования группы (вероятно) названной `input`.

## Следующие шаги

- [Tips and tricks](./doc/tips_and_tricks.md)
- [Environment setup](./doc/env_wayland.md)
- [Systemd integration](./doc/systemd.md)
- [Look and feel](./doc/look_and_feel.md)

### использовавание newm-cmd

`newm-cmd` Предоставляет способ взаимодействовать с запущенным экземпляром Newm из командной строки:

- `newm-cmd inhibit-idle` Предотвращает переход Newm в холостое время (затемнение экрана)
- `newm-cmd config` перезапуск конфигурации
- `newm-cmd lock` блокировка экрана
- `newm-cmd open-virtual-output <name>` открывает новый виртуальный выход (see [newm-sidecar](https://github.com/jbuchermn/newm-sidecar))
- `newm-cmd close-virtual-output <name>` Закрыть виртуальный выход
- `newm-cmd clean` Удаляет осильные состояния, что может произойти, но не должно (если вы сталкиваетесь с необходимостью для этого, пожалуйста, подайте ошибку)
- `newm-cmd debug` Отпечатает некоторую отладительную информацию о текущем состоянии
- `newm-cmd unlock` Разблокирует композитор (если явно включен в Config) - это полезно, если у вас возникли проблемы с настройкой экрана блокировки.
- `terminate` выход из сеанса
- `fullscreen_check` проверяет находится ли композитор в полноекранном режиме(полезно для waybar и прочих панелей которые должны прятаться при полноекранном режиме)


### Вход прямо в Newm (Greetd)

Поместите конфигурацию Newm-Next в `/etc/newm/config.py` и проверьте, после входа в систему как` greeter Если это работает, установите

```toml
command = "start-newm"
```

in `/etc/greetd/config.toml`.


## Credits - newm-next message

Thank you to:

- Jonas Bucher for starting newm
- Diego Aguilar for maintaing the atha AUR package and all the support and help you gave newm
- Audrick Yeu for the amazing insight on the project, countless amount of time spent on improving the experience of users, and for the lovely readme video!
- and all the other contributors to both newm, newm-atha and newm-next!
