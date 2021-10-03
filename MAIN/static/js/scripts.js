let trace1 = {
    x: major_data.major,
    y: major_data.major_sum,
    type: "bar"
  };
let trace2 = {
    x: major_data.major,
    y: major_data.job_titles,
    type: "bar"
  };
// Data trace array
let traceData = [trace1,trace2];

// Apply the group barmode to the layout
let layout = {
  title: "Job vs Major",
  barmode: 'group'
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", traceData, layout);

let trace3={
  x:comp_data.job_num,
  y: comp_data.major_num,
  type:'scatter'
}

let traceData1 = [trace3];

let layout1 = {
  title: "Job vs Major",
};

Plotly.newPlot("plot4", traceData1, layout1);
