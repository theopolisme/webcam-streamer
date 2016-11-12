#!/usr/bin/env python

from __future__ import unicode_literals

import time
import base64
import os
import logging
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, Response, request
from flask.ext.socketio import SocketIO, emit

config = configparser.ConfigParser()

from defaults import defaults
defaults_buf = StringIO.StringIO(defaults)
try:
    config.read_file(defaults_buf)
except AttributeError:
    config.readfp(defaults_buf)

config.read(os.path.expanduser('~/.webcam-streamer.cfg'))

if config.getboolean('cameras', 'use_mock'):
    from camera_mock import Camera, list_camera_ids
else:
    from camera import Camera, list_camera_ids

app = Flask(__name__)
socketio = SocketIO(app)

cameras = {}

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
app.logger.addHandler(stream_handler)

camera_size = (config.getint('cameras', 'width'), config.getint('cameras', 'height'))

@app.route('/')
def home():
    camera_mapping = dict(config.items('camera_names'))
    cameras = [(camera_mapping.get(camera_id, camera_mapping['default'].format(id=camera_id)), camera_id) \
        for camera_id in list_camera_ids()]
    camera_rows = [cameras[x:x+2] for x in xrange(0, len(cameras), 2)]
    return render_template('index.html',
        title=config.get('dashboard', 'title'),
        camera_rows=camera_rows,
        width=camera_size[0],
        height=camera_size[1]
    )

@socketio.on('stream')
def stream(camera_id):

    if camera_id not in cameras:
        cameras[camera_id] = Camera(
            camera_id=camera_id,
            size=camera_size,
            fps=config.get('cameras', 'fps')
        )

    camera = cameras[camera_id]

    data = {
        'id': camera_id,
        'raw': 'data:image/jpeg;base64,' + base64.b64encode(camera.get_frame()),
        'timestamp': time.time()
    }

    emit('frame', data)

if __name__ == '__main__':
    socketio.run(app, host=config.get('server', 'host'), port=config.getint('server', 'port'),
        policy_server=False, transports='websocket, xhr-polling, xhr-multipart')
