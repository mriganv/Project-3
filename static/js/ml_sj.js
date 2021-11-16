d3.json("../static/resources/Salary_Prediction.json").then(function(data) {
    const job=data.Job_Title;
    const loc=data.State;
    dropdown1=d3.select("#selDataset1");
    dropdown2=d3.select("#selDataset2");
    for (i=0;i<job.length;i++) {
        let op=dropdown1.append("option").text(job[i])
        op.property('value',i)
    }
    for (i=0;i<loc.length;i++) {
        let op1=dropdown2.append("option").text(loc[i])
        op1.property('value',i)
    }
});