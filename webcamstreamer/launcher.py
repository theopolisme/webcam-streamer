#!/usr/bin/env python

from __future__ import print_function

import os
import subprocess
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

COMMAND = "cd {directory} && gunicorn --worker-class socketio.sgunicorn.GeventSocketIOWorker -b {host}:{port} streamer:app"

def main():
    print("-----------------------------------------------\n"
          "--------------- webcam-streamer ---------------\n"
          "-----------------------------------------------")

    print("webcam-streamer: Checking requirements...")

    try:
        import PIL
    except:
        print("webcam-streamer: PIL must be installed.")
        return False

    try:
        import cv2
    except:
        print("webcam-streamer: OpenCV and its Python bindings must be installed.")
        return False

    print("webcam-streamer: Reading config...")

    config = configparser.ConfigParser()

    from .streamer.defaults import defaults
    defaults_buf = StringIO.StringIO(defaults)
    try:
        config.read_file(defaults_buf)
    except AttributeError:
        config.readfp(defaults_buf)

    config.read(os.path.expanduser('~/.webcam-streamer.cfg'))

    print("webcam-streamer: Launching webserver...")

    subprocess.call(
        COMMAND.format(
            host=config.get('server', 'host'),
            port=config.get('server', 'port'),
            directory=os.path.dirname(os.path.realpath(__file__))
        ),
        shell=True
    )

    print("webcam-streamer: Dying... :(")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("webcam-streamer: Killing thyself...")
