document.addEventListener('DOMContentLoaded', function() {
    const filterForm = document.getElementById('filter-form');

    filterForm.addEventListener('submit', function(e) {
        e.preventDefault();
        applyFilters();
    });

    function applyFilters() {
        const formData = new FormData(filterForm);
        const params = new URLSearchParams();

        for (const [key, value] of formData.entries()) {
            if (value) params.append(key, value);
        }

        window.location.search = params.toString();
    }
});