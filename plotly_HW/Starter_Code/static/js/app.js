d3.json("data/samples.json").then((importedData) => {
    var data = importedData;

    var trace1 = {
        x: data.sample_values,
        y: data.otu_ids,
        text: data.otu_labels,
        marker: {
            color: data.otu_ids,
            size: data.sample_values
        },
        type: "bar",
        orientation: "h",
    };

    var data = [trace1];

    var layout = {
        xaxis: {title: "OTU ID"},
    };

    Plotly.newplot('bar', data, layout);
}}

    var trace1 = {
        x: data.otu_ids,
        y: data.sample_values,
        text: data.otu_labels,
        mode: 'markers',
        marker: {
            color: data.otu_ids,
            size: data.sample_values
        }
    };

    var data = [trace1];

    var layout = {
        xaxis: {title: "OTU ID"},
    };

    Plotly.newplot('bubble', data, layout);
    }}