function updateGraphDataset(graph, data, dataset=0) {
    graph.data.datasets[dataset].data.push(data);
    graph.update();
}

function updateSensorReadings(sensor_data){
    Object.keys(sensor_data).forEach(function(key) {
        console.log(key);
        console.log(sensor_data[key]);
        $("#"+key).val(sensor_data[key]);
    });
}
