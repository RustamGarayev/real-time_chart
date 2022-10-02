// Websocket connection
let socket = new WebSocket("ws://" +  window.location.host + "/ws/graph/");

$("#start-button").on('click', function (){
    // Set software state on
    $("#software-state").val("On");

    socket.onmessage = function (e) {
        let djangoData = JSON.parse(e.data).sensor_reading;

        // graphList is initialized in graph_class.js file
        // updateGraphDataset is initialized in helper_functions.js file
        graphsList.forEach(element => updateGraphDataset(element.graph, djangoData[element.field_name], 0));
        updateSensorReadings(djangoData);
    };
})

$("#reset-button").on('click', function (){
    socket.close()

    $("#software-state").val("Off");
    window.location.reload()
})

$("#save-stop-button").on('click', function (){
    socket.close()
    $("#software-state").val("Off");
})

// socket.onopen = function(e) {
//     fetch_sensor_readings();
// };
//
// function fetch_sensor_readings() {
//     socket.send(JSON.stringify({
//         'command': 'fetch_sensor_readings',
//     }));
// }

socket.onclose = function(e) {
    console.log(e.data);
    console.error('Chat socket closed unexpectedly');
};
