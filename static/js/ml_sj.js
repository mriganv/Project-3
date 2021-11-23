d3.json("../static/resources/Salary_Prediction.json").then(function(data) {
    const job=data.Job_Title;
    const loc=data.State;
    const sec=data.Sector;
    const ind=data.Industry;
    const own=data.Ownership;
    const sen=data.Seniority;
    dropdown1=d3.select("#selDataset1");
    dropdown2=d3.select("#selDataset2");
    dropdown3=d3.select("#selDataset3");
    dropdown4=d3.select("#selDataset4");
    dropdown5=d3.select("#selDataset5");
    dropdown6=d3.select("#selDataset6");
    for (i=0;i<job.length;i++) {
        let op=dropdown1.append("option").text(job[i])
        op.property('value',job[i])
    }
    for (i=0;i<loc.length;i++) {
        let op1=dropdown2.append("option").text(loc[i])
        op1.property('value',loc[i])
    }

    for (i=0;i<ind.length;i++) {
        let op3=dropdown4.append("option").text(ind[i])
        op3.property('value',ind[i])
    }

    for (i=0;i<sen.length;i++) {
        let op5=dropdown6.append("option").text(sen[i])
        op5.property('value',sen[i])
    }


});