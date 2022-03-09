
mapboxgl.accessToken = 'pk.eyJ1IjoiYm9uYWxsdXJlIiwiYSI6ImNrbDBjdnFoMTBnNHIyd3FvazNzOG82em8ifQ.rKmF7BO1Q6ALhxkkQCl-Eg';
var map = new mapboxgl.Map({
    container: 'map1',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-97.66, 30.19],
    zoom: 11
});

// Add zoom and rotation controls to the map.
map.addControl(new mapboxgl.NavigationControl());
