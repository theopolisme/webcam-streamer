from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='webcam-streamer',
    version='1.0.5',
    description='Simple USB webcam streaming',
    url='https://github.com/theopolisme/webcam-streamer',
    author='Theo Patt',
    author_email='theo@theopatt.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Multimedia :: Video',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='usb webcam streaming',
    packages=find_packages(),
    install_requires=[
        'Flask>=0.10',
        'Flask-SocketIO>=0.5',
        'gunicorn==18.0', # Locked at 18.0 due to bug <https://github.com/miguelgrinberg/Flask-SocketIO/issues/93>
        'Pillow>=2.7.0'
    ],
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'webcam-streamer=webcamstreamer.launcher:main',
        ],
    }
)
