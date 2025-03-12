from setuptools import setup

setup(name='newm-next',
      version='0.4.3',
      description='newm-next - touchpad and touchscreen centric wayland compositor',
      url="https://github.com/newm-next/newm-next",
      author='newm-next',
      author_email='74566464+Pandademic@users.noreply.github.com',
      packages=['newm', 'newm.helper', 'newm.helper.lang_layout','newm.helper.power_manages', 'newm.resources', 'newm.overlay', 'newm.widget', 'newm.dbus', 'newm.gestures', 'newm.gestures.provider', 'newm_panel_basic'],
      package_data={'newm.resources': ['wallpaper.jpg', 'newm.desktop']},
      scripts=['bin/start-newm', 'bin/.start-newm', 'bin/newm-cmd', 'bin/newm-panel-basic','bin/start-newm-lang-socket','bin/start-newm-sockets'],
      install_requires=[
          'pycairo',
          'psutil',
          'python-pam',
          'pyfiglet',
          'dasbus',
          'thefuzz'
      ])
