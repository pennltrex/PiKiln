const ctx = document.getElementById('tempChart').getContext('2d');
const tempChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature (°C)',
            data: [],
            borderColor: 'red',
            fill: false
        }]
    },
    options: {
        scales: {
            x: { title: { display: true, text: 'Time' } },
            y: { title: { display: true, text: 'Temperature (°C)' } }
        }
    }
});

const socket = io();

socket.on('temperature_update', function(data) {
    tempChart.data.labels.push(data.time);
    tempChart.data.datasets[0].data.push(data.temp);
    tempChart.update();
});
