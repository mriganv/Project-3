// Get indeed data with d3
d3.json('../static/resources/indeed_jobs.json').then(function(response) {
  var markers = L.markerClusterGroup();
  var keys = Object.keys(response);
  for(var i = 0; i < keys.length; i++){
    if (response[keys[i]].latitude){
      markers.addLayer(L.marker([response[keys[i]].latitude, response[keys[i]].longitude]).bindPopup(`<h3>${response[keys[i]].job_title}</h3><hr>${response[keys[i]].company_name}<br>(${response[keys[i]].category})`));
    };
  };

  // Get USAjobs data with d3
  d3.json('../static/resources/gov_jobs.json').then(function(response) {

    var markers2 = L.markerClusterGroup();

    var keys2 = Object.keys(response);

    for(var i = 0; i < keys2.length; i++){
      if (response[keys2[i]].LocationLatitude){
        markers2.addLayer(L.marker([response[keys2[i]].LocationLatitude, response[keys2[i]].LocationLongitude]).bindPopup(`<h3>${response[keys2[i]].Title}</h3><hr>${response[keys2[i]].Agency}<br>(${response[keys2[i]].Department})`));
      };
    };


    // Adding the tile layer
    myTileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    var baseMaps = {
      "Jobs": myTileLayer
      };
    
    // Create an overlay object.
    var overlayMaps = {
      "Private Sector": markers,
      "Government": markers2
    };

    // Define a map object.
    var myMap = L.map("map", {
      center: [38.41793880672843, -96.9990462392838],
      zoom: 5,
      layers: [myTileLayer, markers]
      });

    // Pass our map layers to our layer control.
    // Add the layer control to the map.
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);

  });

});
