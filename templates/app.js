document.getElementById('teamForm').addEventListener('submit', function(event) {
    event.preventDefault(); // prevent the default form submission

    const teamName = document.getElementById('teamName').value;
    
    switch(teamName.toLowerCase()) {
        case 'arsenal':
            window.location.href = 'arsenal.html';
            break;
        case 'chelsea':
            window.location.href = 'chelsea.html';
            break;
        case 'liverpool':
            window.location.href = 'chelsea.html';
            break;
        case 'city':
            window.location.href = 'chelsea.html';
            break;
        case 'united':
            window.location.href = 'chelsea.html';
            break;
        case 'spurs':
            window.location.href = 'chelsea.html';
            break;
        // ... Add more teams as needed
        default:
            alert('Team not found or not supported.');
            break;
    }
});
