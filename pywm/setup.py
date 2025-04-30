import os
import sys
import glob
import shutil
import subprocess
from setuptools import setup

# Проверяем, установлены ли meson и ninja
def check_requirements():
    if not shutil.which("meson"):
        raise RuntimeError("Требуется 'meson'! Установите: pip install meson")
    if not shutil.which("ninja"):
        raise RuntimeError("Требуется 'ninja'! Установите: pip install ninja")

def build_project():
    # Запускаем meson build
    proc = subprocess.run(["meson", "build"], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Ошибка meson:\n{proc.stderr}")

    # Собираем через ninja
    proc = subprocess.run(["ninja", "-C", "build"], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"Ошибка ninja:\n{proc.stderr}")

def copy_library():
    # Ищем .so файл (более точный паттерн)
    so_files = glob.glob('build/_pywm.cpython-*.so')
    if not so_files:
        raise FileNotFoundError("Не найдена собранная библиотека!")

    dest = "pywm/_pywm.so"
    if so_files[0] != dest:
        shutil.copy(so_files[0], dest)

if __name__ == "__main__":
    try:
        check_requirements()
        build_project()
        copy_library()
        setup(
            name='pywm',
            version='0.3.1.1',
            description='wlroots-based Wayland compositor with Python frontend',
            url="https://github.com/jbuchermn/pywm",
            author='Jonas Bucher',
            author_email='j.bucher.mn@gmail.com',
            maintainer='quantum_sehi',
            maintainer_email='117589194+SEKAMISehi@users.noreply.github.com',
            package_data={'pywm': ['_pywm.so', 'py.typed']},
            packages=['pywm'],
            install_requires=['evdev', 'imageio', 'pycairo', 'numpy'],
        )
    finally:
        print("make successful")
