// Websocket connection
let socket = new WebSocket("ws://" +  window.location.host + "/ws/graph/");
console.log("ws://" +  window.location.host + "/ws/graph/")

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

    // graphList is initialized in graph_class.js file
    // updateGraphDataset is initialized in helper_functions.js file
    graphsList.forEach(element => updateGraphDataset(element.graph, djangoData[element.field_name], 0));

    updateSensorReadings(djangoData);
};

socket.onclose = function(e) {
    console.log(e.data);
    console.error('Chat socket closed unexpectedly');
};
