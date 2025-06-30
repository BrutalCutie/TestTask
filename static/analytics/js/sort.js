document.addEventListener('DOMContentLoaded', function() {
    const tableHeaders = document.querySelectorAll('th[data-sort]');

    tableHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const sortBy = this.dataset.sort;
            const currentSort = new URLSearchParams(window.location.search).get('sort_by');
            const currentOrder = new URLSearchParams(window.location.search).get('sort_order');

            let newOrder = 'asc';
            if (currentSort === sortBy && currentOrder === 'asc') {
                newOrder = 'desc';
            }

            const params = new URLSearchParams(window.location.search);
            params.set('sort_by', sortBy);
            params.set('sort_order', newOrder);

            window.location.search = params.toString();
        });
    });
});