document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('tempChart').getContext('2d');

    const tempChart = new Chart(ctx, {
        type: 'line',
        data: {
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
                        parser: 'yyyy-MM-dd HH:mm:ss', // Match your timestamp format!
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

        // Add new data point as {x, y}
        tempChart.data.datasets[0].data.push({
            x: data.time, // Should be a string like "2024-05-25 09:50:00"
            y: data.temp
        });

        // Keep only the last 100 points
        if (tempChart.data.datasets[0].data.length > 100) {
            tempChart.data.datasets[0].data.shift();
        }

        tempChart.update();
    });
});
