function initCharts(data) {
    // Гистограмма цен
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
        }
    });

    // График скидок
    const discountCtx = document.getElementById('discountChart').getContext('2d');
    new Chart(discountCtx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Скидка vs Рейтинг',
                data: data.discountData.map(item => ({
                    x: item.rating,
                    y: item.discount
                })),
                backgroundColor: 'rgba(255, 99, 132, 0.6)'
            }]
        },
        options: {
            scales: {
                x: {
                    title: { display: true, text: 'Рейтинг' }
                },
                y: {
                    title: { display: true, text: 'Скидка (%)' }
                }
            }
        }
    });
}