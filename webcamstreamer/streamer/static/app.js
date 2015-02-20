( function ( io ) {
    var FPS_WEIGHT = 0.1,

        streamIds,
        socket = io.connect(),
        streams = {};

    [].forEach.call( document.getElementsByClassName('stream'), function ( el ) {
        var canvas = el.getElementsByTagName('canvas')[0];

        canvas.width = CAMERA_WIDTH;
        canvas.height = CAMERA_HEIGHT;

        streams[el.dataset.id] = {
            startTime: new Date().getTime(),
            frameCt: 0,
            fps: el.getElementsByClassName('fps')[0],
            context: canvas.getContext('2d')
        };
    } );

    streamIds = Object.keys( streams );


    socket.on( 'frame', function ( data ) {
        var img, stream = streams[data.id];

        // Each time we receive an image, request a new one
        socket.emit( 'stream', data.id );

        img = new Image();
        img.src = data.raw;
        stream.context.drawImage( img, 0, 0 );
        stream.frameCt++;
    } );

    streamIds.forEach( function ( id ) {
        // Request new image
        socket.emit( 'stream', id );

        // Update fps (loop)
        setInterval( function () {
            var stream = streams[id],
                d = new Date().getTime(),
                currentTime = ( d - stream.startTime ) / 1000,
                result = Math.floor( ( stream.frameCt / currentTime ) );

            if ( currentTime > 1 ) {
                stream.startTime = new Date().getTime();
                stream.frameCt = 0;
            }

            stream.fps.innerText = result;
        }, 100 );
    } );

}( io ) );
