// Define default configuration
let defaultGraphOptions = {
    scales: {
        y: {
            beginAtZero: true
        }
    }
}
let defaultGraphLabels = [...Array(61).keys()];


// Class - Graph Class for creating graphs with Chart.js library and data from the database
class CustomGraph {
    graph_type = 'line';
    graph_title = '';
    graph_data = [];
    graph_labels = defaultGraphLabels;
    graph_options = defaultGraphOptions;

    constructor(graph_id, graph_type, graph_title, graph_data, graph_labels, graph_options) {
        this.graph_id = graph_id;
        this.graph_type = graph_type;
        this.graph_title = graph_title;
        this.graph_data = graph_data;
        this.graph_options = graph_options;
        this.graph_labels = graph_labels;
    }

    draw() {
        let ctx = document.getElementById(this.graph_id).getContext('2d');
        return new Chart(ctx, {
            type: this.graph_type,
            data: {
                labels: this.graph_labels,
                datasets: [{
                    label: this.graph_title,
                    data: this.graph_data,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            },
            options: this.graph_options
        });
    }
}

batteryVoltageData = [];
altitudeData = [];
velocityData = [];
no2Data = [];
coData = [];
h2Data = [];

let batteryVoltage = new CustomGraph('battery-voltage-graph', 'line', 'Battery Voltage', batteryVoltageData, defaultGraphLabels, defaultGraphOptions);
let altitude = new CustomGraph('altitude-graph', 'line', 'Altitude', altitudeData, defaultGraphLabels, defaultGraphOptions);
let velocity = new CustomGraph('velocity-graph', 'line', 'Velocity', velocityData, defaultGraphLabels, defaultGraphOptions);
let no2 = new CustomGraph('no2-graph', 'line', 'NO2', no2Data, defaultGraphLabels, defaultGraphOptions);
let co = new CustomGraph('co-graph', 'line', 'CO', coData, defaultGraphLabels, defaultGraphOptions);
let h2 = new CustomGraph('h2-graph', 'line', 'H2', h2Data, defaultGraphLabels, defaultGraphOptions);
