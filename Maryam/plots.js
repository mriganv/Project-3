d3.selectAll("#selDataset").on("change", updatePlotly);
function updatePlotly() {
    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selDataset");
    // Assign the value of the dropdown menu option to a variable
    var dataset = dropdownMenu.property("value");
  
    // Initialize x and y arrays
    
    if (dataset === 'dataset1') {
        plot_skill(skills,count)
    }
  
    else if (dataset === 'dataset2') {

      plotCity(city,Job_count)
      
      
    }
    else if (dataset === 'dataset3') {
      chart.render();

      }
  
    // Note the extra brackets around 'x' and 'y'
    Plotly.restyle("plot", "x", [x]);
    Plotly.restyle("plot", "y", [y]);
  }

  