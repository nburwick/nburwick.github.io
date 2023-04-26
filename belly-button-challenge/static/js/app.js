// functions to update dashboard
// function that populates the metadata
function get_meta(id)
{
    
    d3.json("static/js/samples.json").then((data) => {
        //grab all data
        let metadata = data.metadata;
        // filter to ID selected
        let result = metadata.filter(entry => entry.id == id)[0];

        //clear existing text
        d3.select("#sample-metadata").html("");

        // Populate demographic info
        Object.entries(result).forEach(([key, value]) => {
            d3.select("#sample-metadata").append("h5").text(`${key}: ${value}`)});
    })
}
// function that builds Bar Chart
function create_bar_chart(id)
{
    d3.json("static/js/samples.json").then(data => {
        // grab sample data
        let samples = data.samples;
        // filter data to item
        let sample = samples.filter(entry => entry.id == id)[0];
        // grab all arrays needed from sample
        let otu_ids = sample.otu_ids;
        let otu_labels = sample.otu_labels;
        let sample_values = sample.sample_values;

        // build bar chart
        let trace = {
            y: otu_ids.slice(0,10).map(id => `OTU ${id}`).reverse(),
            x: sample_values.slice(0,10).reverse(),
            text: otu_labels.slice(0,10).reverse(),
            type: "bar",
            orientation: "h"
        }

        let layout = {
            title: `Top 10 Belly Button Bactieria: ${id}`
        }
        Plotly.newPlot("bar", [trace], layout)
    });
    
}

// function to build Bubble Chart
function create_bubble_chart(id)
{
    d3.json("static/js/samples.json").then(data => {
        // grab sample data
        let samples = data.samples;
        // filter data to item
        let sample = samples.filter(entry => entry.id == id)[0];
        // grab all arrays needed from sample
        let otu_ids = sample.otu_ids;
        let otu_labels = sample.otu_labels;
        let sample_values = sample.sample_values;

        // build bubble chart
        let trace = {
            x: otu_ids,
            y: sample_values,
            text: otu_labels,
            mode: "markers",
            marker: {
                size: sample_values,
                color: otu_ids,
                colorscale: "Earth"
            }
        };

        let layout = {
            title: `Bacteria Cultures in Sample: ${id}`,
            hovermode: "closest",
            xaxis: {title: `OTU ID: ${id}`}
        };
        Plotly.newPlot("bubble", [trace], layout);
    });

}

// function to build a guage chart
function create_guage_chart(id)
{
    d3.json("static/js/samples.json").then(data => {
        // grab sample data
        let samples = data.metadata;
        // filter data to item
        let sample = samples.filter(entry => entry.id == id)[0];

        // build gauge
        let trace = {
            domain: { x: [0, 1], y: [0, 1] },
            value: sample.wfreq,
            title: { text: `<b>Belly Button Washing Frequency</b><br>Scrubs per Week: ID ${id}`, font: {size: 20}},
            type: "indicator", 
            mode: "gauge+number",
            gauge: {
                axis: {range: [null, 9]}, 
                bar: {color: "rgb(68,166,198)"},
                steps: [
                    { range: [0, 1], color: "rgb(233,245,248)" },
                    { range: [1, 2], color: "rgb(218,237,244)" },
                    { range: [2, 3], color: "rgb(203,230,239)" },
                    { range: [3, 4], color: "rgb(188,223,235)" },
                    { range: [4, 5], color: "rgb(173,216,230)" },
                    { range: [5, 6], color: "rgb(158,209,225)" },
                    { range: [6, 7], color: "rgb(143,202,221)" },
                    { range: [7, 8], color: "rgb(128,195,216)" },
                    { range: [8, 9], color: "rgb(113,187,212)" },
                ]
            }};

        let layout = {width: 600, height: 400};

        Plotly.newPlot("gauge", [trace], layout);
    });
}

// function to initialize the dashboard
function initialize()
{    
    // select dropdown
    var dropdown = d3.select("#selDataset");

    // read data to populate ids
    d3.json("static/js/samples.json").then((data) => {
        let ids = data.names;
        
        // populate dropdown using a forEach()
        ids.forEach(element => {
            dropdown.append("option").text(element);
        });
        let sample1 = ids[0];
        get_meta(sample1);
        create_bar_chart(sample1);
        create_bubble_chart(sample1);
        create_guage_chart(sample1);
    });


}

// Option Change Function

function optionChanged(id){
    get_meta(id);
    create_bar_chart(id);
    create_bubble_chart(id);
    create_guage_chart(id);
}



initialize();
