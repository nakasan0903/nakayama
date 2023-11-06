$(document).ready(function() {
    loadMap();
});

function loadMap() {
    var map = L.map('map').setView([51.509865, -0.118092], 6);  // Set initial view to London, zoom level 6

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Simulating fetching England's location via Ajax
    $.ajax({
        url: 'https://jsonplaceholder.typicode.com/posts/1',  // Just a dummy endpoint, replace with your actual endpoint
        method: 'GET',
        success: function(response) {
            // Using London's coordinates as a mock response
            var englandLocation = [51.509865, -0.118092];
            L.marker(englandLocation).addTo(map)
                .bindPopup('This is England.').openPopup();
        },
        error: function(error) {
            console.error('Error fetching location:', error);
        }
    });
}

