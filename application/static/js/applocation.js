if ("geolocation" in navigator) {

    navigator.geolocation.getCurrentPosition(function (position) {
        
        var lat = position.coords.latitude;
        var long = position.coords.longitude;
        // var latStr = toString lat;
        console.log('my current latitude: '+ lat.toString() +"\n my current longitude: "+ long.toString());

    }, function (err) {
        ipLookup();
    });

} else {
    ipLooukp();

    function ipLookup() {

    }
}