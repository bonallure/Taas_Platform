var form = document.getElementById('order_form')
form.addEventListener('submit',(e) => {e.preventDefault();})

function submit_order()
{
  //create form variable
  var form = document.getElementById('order_form');

  //capture form data
  var order = {};
  var i;
  for (i = 0; i <form.length; i++)
  {
    if (form.elements[i].name != ""){
        order[form.elements[i].name] =  form.elements[i].value;
    }
  }

  //POST the form data
  var form_action = 'https://demand.team11.sweispring21.tk/demand-back-end/order_api/v1/orders';
  var xhr = new XMLHttpRequest();
  xhr.open("POST", form_action, true);
  // xhr.setRequestHeader("Content-Type", "application/json");

  xhr.onreadystatechange = function() { // Call a function when the state changes.
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
		var json = JSON.parse(xhr.responseText);
		var eta = json.data.eta;
		console.log(eta);
        document.getElementById('order_status').innerHTML = "Your vehicle is on its way. ETA: " + eta;
		form.div = document.getElementById('form_div');
		form.div.innerHTML = "<div id='map1' style='width: 800px; height: 600px;'></div>";
		
		
		mapboxgl.accessToken = 'pk.eyJ1IjoiYm9uYWxsdXJlIiwiYSI6ImNrbDBjdnFoMTBnNHIyd3FvazNzOG82em8ifQ.rKmF7BO1Q6ALhxkkQCl-Eg';
        var map = new mapboxgl.Map({
            container: 'map1',
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [-97.66, 30.19],
            zoom: 11
        });
        var url = 'https://wanderdrone.appspot.com/';
        map.on('load', function () {
            var request = new XMLHttpRequest();
            window.setInterval(function () {
                // make a GET request to parse the GeoJSON at the url
                request.open('GET', url, true);
                request.onload = function () {
                    if (this.status >= 200 && this.status < 400) {
                        // retrieve the JSON from the response
                        var json = JSON.parse(this.response);

                        // update the drone symbol's location on the map
                        map.getSource('drone').setData(json);

                        // fly the map to the drone's current location
                        map.flyTo({
                        center: json.geometry.coordinates,
                        speed: 0.5
                        });
                    }
                };
                request.send();
            }, 2000);
            map.addSource('drone', { type: 'geojson', data: url });
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
    }
  }
  xhr.send(JSON.stringify(order));
}
