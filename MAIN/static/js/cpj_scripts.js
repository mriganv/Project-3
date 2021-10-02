let trace1 = {
    x: degreeData.degrees_list,
    y: degreeData.degree_counts,
    marker: {color: 'rgb(171,34,105)'},
    type: "bar"
  };

  let layout = {
  title: "Jobs vs Degree",
  
};

  let traceData = [trace1];

  Plotly.newPlot("degreebar", traceData, layout);

// **********************************************************************************************

let trace2 = {
      x: regionData.regions_us, 
      y: regionData.regions_count, 
      marker: {color: 'rgb(250, 128, 114)'},
      type: "bar"

  };

  let layout1 = {
  title: "Available Jobs in each state"
};

let traceRegions = [trace2];

Plotly.newPlot("regionsbar",traceRegions, layout1);

// **********************************************************************************************
var trace4 = {
  y: doctorateData.Doctorates_states,
  x: doctorateData.Doctorates_counts, 
  marker: {color: 'rgb(41,0,151)'},
  type: 'bar',
};

var trace3 = {
  x: mastersData.Masters_states,
  y: mastersData.Masters_counts,
  marker: {color: 'rgb(0, 128, 128)'},
  type: 'bar'
};

var data = [trace3,trace4];

var layoutmasters = {
  title: 'Jobs openings for Masters and PhD Degree'}

Plotly.newPlot('mastersbar', data, layoutmasters);

// ************************************************************************************************


var data1 = [trace4];

var layoutdoctorate = {
  title: 'Jobs openings for Doctorate Degree'}

Plotly.newPlot('doctoratebar', data1, layoutdoctorate);

// **************************************************************************************************