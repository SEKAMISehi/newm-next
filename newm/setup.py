from setuptools import setup, find_packages

with open("../README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='newm-qs',
    version='0.4.4',
    description='Wayland compositor optimized for touchpad and touchscreen with infinite workspace',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SEKAMISehi/newm-next",
    author='Pandademic',
    author_email='74566464+Pandademic@users.noreply.github.com',
    maintainer='quantum_sehi',
    maintainer_email='117589194+SEKAMISehi@users.noreply.github.com',
    license='MIT',
    packages=find_packages(exclude=["tests"]),
    package_data={
        'newm.resources': ['wallpaper.jpg', 'newm.desktop']
    },
    entry_points={
        'console_scripts': [
            'newm = newm.main:start',
            'newm-panel-basic = newm_panel_basic.cli:main',
        ],
    },
    install_requires=[
        'pycairo',
        'psutil',
        'python-pam',
        'dasbus',
        'rapidfuzz',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Topic :: Desktop Environment :: Wayland Compositor',
    ],
    python_requires='>=3.9',
)
