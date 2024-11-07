
    // Step size for x-values
    let h = 0.05;
    let eps = 0.1
    let col1 = 'rgba(255, 0, 0, 1)';
    let col2 = 'rgba(0, 255, 255, 1)';


    // Function to compute the series approximation of ln(1 - x)
    function calcTaylorSeries() {
        let xs = [];
        let ys = [];
        for (let x = -0.9; x < 0.99; x += h) { // Avoid x = 1 due to ln(0) being undefined
            xs.push(x.toFixed(2));
            ys.push(myLnTaylorSeries(x, eps)); // Use an epsilon for precision
        }
        return [xs, ys];
    }

    // Series approximation of ln(1 - x) using Taylor series
    function myLnTaylorSeries(x, eps) {
        let fx = 0;
        let term;
        let n = 1;
        do {
            term = (-1) * (Math.pow(x, n) / n);
            fx += term;
            n++;
        } while (Math.abs(term) > eps && n < 1000); // Limit iterations for safety
        return fx;
    }

    // Function to calculate the actual ln(1 - x) using Math.log
    function calcActualLn() {
        let ys2 = [];
        for (let x = -0.9; x < 0.99; x += h) {
            ys2.push(Math.log(1 - x));
        }
        return ys2;
    }

    // Get the context of the canvas element using its ID
    const ctx = document.getElementById('graphic').getContext('2d');

    // Prepare data for the chart
    const chartData = calcTaylorSeries();
    
    // Initialize Chart.js
    const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: chartData[0], // X-values
        datasets: [
            {
                label: 'Taylor Series Approximation',
                data: chartData[1], // Y-values from Taylor series
                borderColor: col1,
                pointBackgroundColor: col1,
                pointHoverBackgroundColor: 'rgba(255, 255, 255, 1)',
                pointRadius: 2,
                pointHoverRadius: 5,
                animation: {
                    duration: 3000,
                    easing: 'bounce'
                },
                fill: false
            },
            {
                label: 'Math.log(1 - x)',
                data: calcActualLn(), // Y-values from Math.log
                backgroundColor:'rgba(255, 255, 255, 1)',
                borderColor: col2,
                pointBackgroundColor: col2,
                pointHoverBackgroundColor: 'rgba(255, 255, 255, 1)',
                pointRadius: 2,
                pointHoverRadius: 5,
                animation: {
                    duration: 10000,
                    easing: 'easeOutBounce'
                },
                fill: false,
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true,
                position: 'top', // Options: 'top', 'left', 'bottom', 'right'
            },
            title: {
                display: true,
                text: 'Comparison of Taylor Series Approximation and Math.log(1 - x)'
            },
            annotation: {
                annotations: {
                    label1: {
                        type: 'label',
                        xValue: 10.3,
                        yValue: -2.0,
                        backgroundColor: 'rgba(255,255,255)',
                        content: ['Я уменьшил точность,',' чтобы графики не перекрывались'],
                        font: {
                            size: 12
                        }
                    }
                }
            },
            animation: {
                duration: 1000,
                easing: 'linear'
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'X Values'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Y Values'
                }
            }
        }
    }
});

document.getElementById('saveBtn').addEventListener('click', function() {
    // Получаем изображение графика
    const link = document.createElement('a');
    link.href = document.getElementById('graphic').toDataURL('image/png'); // Получаем данные в формате PNG
    link.download = 'graphic.png'; // Имя файла
    link.click(); // Симулируем клик по ссылке
});