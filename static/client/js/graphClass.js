// Define default configuration
let defaultGraphOptions = {
    scales: {
        x: {
            grid: {
              display: false
            }
        },
        y: {
            beginAtZero: false,
            grid: {
                display: false
            },
        }
    }
}
let defaultGraphLabels = [...Array(61).keys()];


// Class - Graph Class for creating graphs with Chart.js library and data from the database
class CustomGraph {
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

// Prevent same referenced graph data from being drawn multiple times
batteryVoltageData = [];
altitudeData = [];
velocityData = [];
no2Data = [];
coData = [];
h2Data = [];
temperatureData = [];
gpsData = [];

// Define each graph
let batteryVoltageGraph = new CustomGraph('battery-voltage-graph', 'line', 'Battery Voltage (V)', batteryVoltageData, defaultGraphLabels, defaultGraphOptions);
let altitudeGraph = new CustomGraph('altitude-graph', 'line', 'Current (A)', altitudeData, defaultGraphLabels, defaultGraphOptions);
let velocityGraph = new CustomGraph('velocity-graph', 'line', 'Pressure (mBar)', velocityData, defaultGraphLabels, defaultGraphOptions);
let no2Graph = new CustomGraph('no2-graph', 'line', 'Humidity (%)', no2Data, defaultGraphLabels, defaultGraphOptions);
let coGraph = new CustomGraph('co-graph', 'line', 'Loudness (db)', coData, defaultGraphLabels, defaultGraphOptions);
let h2Graph = new CustomGraph('h2-graph', 'line', 'Distance to obstacle (m)', h2Data, defaultGraphLabels, defaultGraphOptions);
let temperatureGraph = new CustomGraph('temperature-graph', 'line', 'Temperature (C)', temperatureData, defaultGraphLabels, defaultGraphOptions);
let gpsGraph = new CustomGraph('gps-graph', 'line', 'Distance to ground (cm)', gpsData, defaultGraphLabels, defaultGraphOptions);

let graphsList = [
    {
        'graph': batteryVoltageGraph.draw(),
        'field_name': 'battery_voltage',
    },
    {
        'graph': altitudeGraph.draw(),
        'field_name': 'altitude',
    },
    {
        'graph': velocityGraph.draw(),
        'field_name': 'velocity',
    },
    {
        'graph': no2Graph.draw(),
        'field_name': 'no2_level_in_ppm',
    },
    {
        'graph': coGraph.draw(),
        'field_name': 'co_level_in_ppm',
    },
    {
        'graph': h2Graph.draw(),
        'field_name': 'h2_level_in_ppm',
    },
    {
        'graph': temperatureGraph.draw(),
        'field_name': 'temperature',
    },
    {
        'graph': gpsGraph.draw(),
        'field_name': 'distance_to_ground',
    }
];
