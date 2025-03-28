from setuptools import setup

setup(name='newm-next-qs',
      version='0.4.3.2',
      description='newm-next-qs - The wayland composer is based on work with a touchpad and touchscreen. He also proposes a new approach to the organization of the workspace and work with the windows making one limitless working space to accommodate applications windows and manter with them using key combinations and gestures',
      url="https://github.com/SEKAMISehi/newm-next.git",
      author='quantum_sehi',
      author_email='117589194+SEKAMISehi@users.noreply.github.com',
      packages=['newm', 'newm.helper', 'newm.helper.lang_layout','newm.helper.power_manages', 'newm.resources', 'newm.overlay', 'newm.widget', 'newm.dbus', 'newm.gestures', 'newm.gestures.provider', 'newm_panel_basic'],
      package_data={'newm.resources': ['wallpaper.jpg', 'newm.desktop']},
      scripts=['bin/start-newm', 'bin/.start-newm', 'bin/newm-cmd', 'bin/newm-panel-basic','bin/start-newm-lang-socket','bin/start-newm-sockets','bin/newm_lang_watch'],
      install_requires=[
          'pycairo',
          'psutil',
          'python-pam',
          'pyfiglet',
          'dasbus',
          'thefuzz'
      ],
      classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Topic :: Desktop Environment :: Wayland Compositor',
        ],)
