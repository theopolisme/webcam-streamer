#!/usr/bin/env python

from StringIO import StringIO

from PIL import Image

def list_camera_ids():
    return ['0', '1']

class Camera(object):

    def __init__(self, camera_id, size, fps):
        self.width = size[0]
        self.height = size[1]

    def get_frame(self):
        image = Image.new('RGB', (self.width, self.height), 'black')
        buf = StringIO()
        image.save(buf, 'JPEG')

        return buf.getvalue()
