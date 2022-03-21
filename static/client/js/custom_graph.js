const batteryVoltage = document.getElementById('battery-voltage-graph').getContext('2d');
const altitude = document.getElementById('altitude-graph').getContext('2d');
const velocity = document.getElementById('velocity-graph').getContext('2d');

// define labels as an array of range 60 to indicate time series
let label = [...Array(61).keys()];

// initialize each sensor reading as an empty list to fill up as data comes in
let batteryVoltageData = [];
let altitudeData = [];
let velocityData = [];

// define each graph data and its options
let BatteryVoltageGraphData = {
    type: 'line',
    data: {
        labels: label,
        datasets: [{
            label: 'Battery Voltage',
            data: batteryVoltageData,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

let altitudeGraphData = {
    type: 'line',
    data: {
        labels: label,
        datasets: [{
            label: 'Altitude',
            data: altitudeData,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
};

let velocityGraphData = {
    type: 'line',
    data: {
        labels: label,
        datasets: [{
            label: 'Velocity',
            data: velocityData,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            },
            animation: {
                duration: 0
            }
        }
    }
};

const batteryVoltageGraph = new Chart(batteryVoltage, BatteryVoltageGraphData);
const altitudeGraph = new Chart(altitude, altitudeGraphData);
const velocityGraph = new Chart(velocity, velocityGraphData);

// Websocket connection
let socket = new WebSocket("ws://" +  window.location.host + "/ws/graph/");

// socket.onopen = function(e) {
//     fetch_sensor_readings();
// };
//
// function fetch_sensor_readings() {
//     socket.send(JSON.stringify({
//         'command': 'fetch_sensor_readings',
//     }));
// }

socket.onmessage = function (e) {
    let djangoData = JSON.parse(e.data).sensor_reading;

    console.log(Object.keys(djangoData));

    batteryVoltageGraph.data.datasets[0].data.push(djangoData.battery_voltage);
    altitudeGraph.data.datasets[0].data.push(djangoData.altitude);
    velocityGraph.data.datasets[0].data.push(djangoData.velocity);

    batteryVoltageGraph.update();
    altitudeGraph.update();
    velocityGraph.update();
};

socket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

