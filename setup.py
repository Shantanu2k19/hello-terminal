from setuptools import setup

setup(
    name='hello-terminal',
    version='0.1',
    packages=['hello_terminal'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hello-terminal-install=hello_terminal.install_hook:add_hello_to_rc',
        ],
    },
    author='Your Name',
    description='Prints Hello World every time a terminal is opened',
)
