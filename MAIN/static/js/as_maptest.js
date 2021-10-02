let myMap = L.map("map", {
  center: [37.8, -96],
  zoom: 5 ,
  minZoom: 4,
  // layers: [streets, geojson]
});
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  })
  .addTo(myMap);

  geoData = "../static/resources/geojsons/newtest.geojson"
    
    
  let geojson;



  d3.json(geoData).then(function(data) {

    const bigboi = data.features
    for (let i = 0; i < bigboi.length; i++) {
        console.log(bigboi[i].properties.jobs['Job characteristic code'])
    }
      
    dropdown=d3.select("#selDataset");

    for (i=0;i<bigboi.length;i++) {
      let op=dropdown.append("option").text(bigboi[i].properties.jobs['Job characteristic code'])
      op.property('value',i)
  }
    d3.selectAll("#selDataset").on("change", getData);

      // Create a new choropleth layer.
    geojson = L.choropleth(data, {

      // Define which property in the features to use.
      valueProperty: "density",

      // Set the color scale.
      scale: ["#5ba3ff", "#301934"],

      // The number of breaks in the step range
      steps: 8,

      // q for quartile, e for equidistant, k for k-means
      mode: "q",
      style: {
        // Border color
        color: "#fff",
        weight: 1,
        fillOpacity: 0.8
      },

      // Binding a popup to each layer
      onEachFeature: function(feature, layer) {
        layer.bindPopup(feature.properties.name + "<br><hr>Number of Jobs: " +
          feature.properties.density);
      }
    })
    .addTo(myMap)


    // Set up the legend.
    var legend = L.control({ position: "bottomright" });
    legend.onAdd = function() {
      var div = L.DomUtil.create("div", "info legend");
      var limits = geojson.options.limits;
      var colors = geojson.options.colors;
      var labels = [];

      // Add the minimum and maximum.
      var legendInfo = "<h3>Occupation Density</h3>" +
        "<div class=\"labels\">" +
          "<div class=\"min\">" + limits[0] + "</div>" +
          "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
        "</div>";

      div.innerHTML = legendInfo;

      limits.forEach(function(limit, index) {
        labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
      });

      div.innerHTML += "<ul>" + labels.join("") + "</ul>";
      return div;
    };

  //   Adding the legend to the map
    legend.addTo(myMap);

  });



  // var baseMaps = {
  //     "Streets": streets
  // };

  // // var overlayMaps = {
  // //     "Test": geojson
  // // };

  // L.control.layers(baseMaps
  //     // , overlayMaps
  //   ).addTo(myMap);



  
