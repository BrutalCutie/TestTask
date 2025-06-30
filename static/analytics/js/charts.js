function initCharts(data) {
    // Гистограмма цен
    if (data.priceData.length > 0) {
        const priceCtx = document.getElementById('priceChart').getContext('2d');
        new Chart(priceCtx, {
            type: 'bar',
            data: {
                labels: data.priceData.map(item => item.range),
                datasets: [{
                    label: 'Количество товаров',
                    data: data.priceData.map(item => item.count),
                    backgroundColor: 'rgba(54, 162, 235, 0.6)'
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } else {
        document.getElementById('priceChart').closest('.chart').innerHTML =
            '<p>Нет данных для гистограммы цен</p>';
    }

    // График скидок
    if (data.discountData.length > 0) {
        const discountCtx = document.getElementById('discountChart').getContext('2d');
        new Chart(discountCtx, {
            type: 'line',
            data: {
                labels: data.discountData.map(item => item.rating.toFixed(1)),
                datasets: [{
                    label: 'Средняя скидка (%)',
                    data: data.discountData.map(item => item.discount),
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    fill: true,
                    tension: 0.3
                }]
            },
            options: {
                scales: {
                    y: {
                        title: { display: true, text: 'Скидка (%)' }
                    },
                    x: {
                        title: { display: true, text: 'Рейтинг' }
                    }
                }
            }
        });
    } else {
        document.getElementById('discountChart').closest('.chart').innerHTML =
            '<p>Нет данных для графика скидок</p>';
    }
}