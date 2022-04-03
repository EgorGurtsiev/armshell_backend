const form = document.getElementById('search_form')
form.addEventListener('submit', () => {
    form.preventDefault();
    const search = document.getElementById('search')
    fetch('/call/busy/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
            'X-CSRFToken': CSRF_TOKEN
        },
        body: `search: '${search.value}'`
    })
});