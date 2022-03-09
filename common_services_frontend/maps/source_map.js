// order json creation

mapboxgl.accessToken = 'pk.eyJ1IjoiYm9uYWxsdXJlIiwiYSI6ImNrbDBjdnFoMTBnNHIyd3FvazNzOG82em8ifQ.rKmF7BO1Q6ALhxkkQCl-Eg';
var map = new mapboxgl.Map({
    container: 'map2',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-97.74, 30.26],
    zoom: 16
});

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());
var url = 'https://api.mapbox.com/directions/v5/mapbox/driving/-97.7442,30.2679;-97.7286,30.241?access_token=pk.eyJ1IjoiYm9uYWxsdXJlIiwiYSI6ImNrbDBjdnFoMTBnNHIyd3FvazNzOG82em8ifQ.rKmF7BO1Q6ALhxkkQCl-Eg&steps=true&geometries=geojson';
map.on('load', function () {
  var request = new XMLHttpRequest();
  window.setInterval(function () {
    // make a GET request to parse the GeoJSON at the url
    request.open('GET', url, true);
    request.onload = function () {
      if (this.status >= 200 && this.status < 400) {
        // retrieve the JSON from the response
        var json = JSON.parse(this.response);
        json = json.routes[0];
        console.log(json.geometry.coordinates);
        
        // update the drone symbol's location on the map
        map.getSource('drone').setData({
          "type": "FeatureCollection",
          "features": [{
            "type": "Feature",
            "properties": {},
            "geometry": {
              "type": "Point",
              "coordinates": json.geometry.coordinates
              }
            }]
          });
        
        // fly the map to the drone's current location
        map.flyTo({
          center: json.geometry.coordinates[0],
          speed: 0.5
          });
      }
    };
    request.send();
  }, 2000);
  map.addSource('drone', { 
    'type': 'geojson', 
    'data': {
      'type': 'Feature',
      'properties': {},
      'geometry': {
        'type': 'LineString',
        'coordinates' : [
          [
              -97.744318,
              30.267933
          ],
          [
              -97.744475,
              30.267507
          ],
          [
              -97.743156,
              30.267138
          ],
          [
              -97.746875,
              30.257144
          ],
          [
              -97.743735,
              30.253411
          ],
          [
              -97.741254,
              30.25175
          ],
          [
              -97.74018,
              30.250408
          ],
          [
              -97.737704,
              30.249327
          ],
          [
              -97.736166,
              30.248087
          ],
          [
              -97.73363,
              30.247409
          ],
          [
              -97.73121,
              30.24557
          ],
          [
              -97.727852,
              30.241141
          ],
          [
              -97.728422,
              30.240857
          ],
          [
              -97.728553,
              30.241027
          ]
      ]
      }
    }
  });
  map.addLayer({
    'id': 'drone',
    'type': 'symbol',
    'source': 'drone',
    'layout': {
    // This icon is a part of the Mapbox Streets style.
    // To view all images available in a Mapbox style, open
    // the style in Mapbox Studio and click the "Images" tab.
    // To add a new image to the style at runtime see
    // https://docs.mapbox.com/mapbox-gl-js/example/add-image/
    'icon-image': 'rocket-15'
    }
  });
});