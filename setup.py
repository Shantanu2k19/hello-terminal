from setuptools import setup
from setuptools.command.install import install
import os

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        try:
            from hello_terminal.install_hook import add_hello_to_rc
            add_hello_to_rc()
        except Exception as e:
            print(f"Installation hook failed: {e}")

setup(
    name='hello-terminal',
    version='0.2',
    packages=['hello_terminal'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hello-terminal-uninstall=hello_terminal.uninstall_hook:remove_hello_from_rc',
        ],
    },
    author='zodiac2k19',
    description='Prints Hello World every time a terminal is opened',
    cmdclass={
        'install': CustomInstallCommand,
    },
)
