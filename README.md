webcam-streamer
===

*Dead simple USB webcam streaming over the internet*

## Getting started
 - Obtain a USB webcam
 - Find an internet-connected device with a USB port
 - Plug the webcam into the USB port
 - Install [OpenCV](http://opencv.org/)
 - `pip install webcam-streamer`
 - `webcam-streamer`
 - You're live @ [localhost:5000](http://localhost:5000)!

## Customizations

You can customize the streams delivered by creating and modifying a `.webcam-streamer.cfg` in your home directory. 

### Available options

```
[server]
host=0.0.0.0           ; Host to serve the application on
port=5000              ; Port to serve the application on

[dashboard]
title=Webcam Streamer  ; Title displayed at the top of the web dashboard

[cameras]
use_mock=false         ; If true, will simulate camera feeds (useful for testing) 
width=320              ; Width of the camera stream(s)
height=240             ; Height of the camera stream(s)
fps=10                 ; Frames per second to be acquired from camera(s)

[camera_names]
default=Camera #{id}   ; The default title to display above each camera

```

Additionally, custom mappings of `id->name` can be included in camera_names. For example, if Camera #0 is the garage camera, you could add something like `0=Garage camera` to the `camera_names` config section.

## Screenshot
![Because, y'know, why not.](https://cloud.githubusercontent.com/assets/1410202/6306191/fd5c1762-b8f6-11e4-935a-5b0e1aa9db94.png)

## Technical details

`webcam-streamer` uses Flask, deployed with Gunicorn, to serve a web frontend. Individual camera feeds, acquired from cameras using OpenCV, are delivered to clients using WebSockets.

## Requirements
 - OpenCV
 - Python 2.7+, 3+

## Deploying on an NVIDIA Jetson TK1

Unfortunately the NVIDIA-supplied OpenCV library, "[opencv4tegra](http://elinux.org/Jetson/Computer_Vision_Performance#Hardware_Acceleration_of_OpenCV)", doesn't have USB camera support built in to the kernel, so **you'll need to build and install OpenCV from the source**. Although this naturally will require you to forfeit the Tegra CPU optimizations included in the custom library, [endless depressing errors](https://devtalk.nvidia.com/default/topic/752109/-opencv4tegra-2-4-8-2-on-jetson-tk1/) will otherwise befall you so it's probably worth it.

The [instructions on the eLinux wiki](http://elinux.org/Jetson/Installing_OpenCV#Natively_compiling_the_OpenCV_library_from_source_onboard_the_device) have been tested and work using OpenCV 3.0.0-beta.

## License

```
The MIT License (MIT)

Copyright (c) 2015 Theo Patt/Theopolisme <theo@theopatt.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
