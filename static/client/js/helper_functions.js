function updateGraphDataset(graph, data, dataset=0) {
    graph.data.datasets[dataset].data.push(data);
    graph.update();
}
