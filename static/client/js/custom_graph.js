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

let batteryVoltageGraph = batteryVoltage.draw();
let altitudeGraph = altitude.draw();
let velocityGraph = velocity.draw();
let no2Graph = no2.draw();
let coGraph = co.draw();
let h2Graph = h2.draw();

socket.onmessage = function (e) {
    let djangoData = JSON.parse(e.data).sensor_reading;

    console.log(Object.keys(djangoData));

    batteryVoltageGraph.data.datasets[0].data.push(djangoData.battery_voltage);
    altitudeGraph.data.datasets[0].data.push(djangoData.altitude);
    velocityGraph.data.datasets[0].data.push(djangoData.velocity);
    no2Graph.data.datasets[0].data.push(djangoData.no2_level_in_ppm);
    coGraph.data.datasets[0].data.push(djangoData.co_level_in_ppm);
    h2Graph.data.datasets[0].data.push(djangoData.h2_level_in_ppm);

    batteryVoltageGraph.update();
    altitudeGraph.update();
    velocityGraph.update();
    no2Graph.update();
    coGraph.update();
    h2Graph.update();
};

socket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
