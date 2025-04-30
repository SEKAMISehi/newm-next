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
#from newm.helper.lang_layout import lang

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
                "newm-next",
                "version 0.4.3 ALPHA"
            ],
        }
    },
}
