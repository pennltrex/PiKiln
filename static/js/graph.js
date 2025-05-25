document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('tempChart').getContext('2d');

    const tempChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [], // timestamps
            datasets: [{
                label: 'Temperature (°C)',
                data: [],
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 2,
                fill: false,
                tension: 0.1
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'time',
                    time: {
                        parser: 'HH:mm:ss',
                        tooltipFormat: 'HH:mm:ss',
                        unit: 'minute',
                        displayFormats: {
                            minute: 'HH:mm'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Time'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Temperature (°C)'
                    }
                }
            }
        }
    });

    const socket = io();

    socket.on('temperature_update', function (data) {
        console.log("Received:", data);

        // Add new data point
        tempChart.data.labels.push({
            x: data.time,
            y: data.temp
        });
        tempChart.data.datasets[0].data.push(data.temp);

        // Keep only the last 100 points
        if (tempChart.data.labels.length > 100) {
            tempChart.data.labels.shift();
            tempChart.data.datasets[0].data.shift();
        }

        tempChart.update();
    });
});
