mapboxgl.accessToken = 'pk.eyJ1IjoiYm9uYWxsdXJlIiwiYSI6ImNrbDBjdnFoMTBnNHIyd3FvazNzOG82em8ifQ.rKmF7BO1Q6ALhxkkQCl-Eg';
var map = new mapboxgl.Map({
    container: 'map1',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-97.74, 30.26],
    zoom: 16
});

function show_av(){
    var vin = document.forms["vin_form"]["vin"].value;
    // Add zoom and rotation controls to the map.
    map.addControl(new mapboxgl.NavigationControl());
    console.log(vin);
    var marker = new mapboxgl.Marker({ color: 'black', rotation: 45 })
    window.setInterval(function () {
      var url = 'http://localhost:8081/supply-back-end/vehicle_api/v1/vehicle_location?vin=123';
      var request = new XMLHttpRequest();
        // make a GET request to parse the GeoJSON at the url
        request.open('GET', url, true);
        request.onload = function () {
          if (this.status >= 200 && this.status < 400) {
            // retrieve the JSON from the response
            var json = JSON.parse(this.response);
            json = json.data[0];
            console.log(json);

            // update the drone symbol's location on the map
            var marker2 = new mapboxgl.Marker({ color: 'black', rotation: 45 })
                .setLngLat(json)
                .addTo(map);

            // fly the map to the drone's current location
            map.flyTo({
              center: json,
              speed: 0.5
              });
          }
        };
        request.send();
    }, 2000);
}