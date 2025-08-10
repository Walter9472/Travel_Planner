document.addEventListener('DOMContentLoaded', function () {
    const dataEl = document.getElementById('route-data');
    if (!dataEl) {
        return;
    }
    const data = JSON.parse(dataEl.textContent);

    const map = L.map('map').setView([data.start.lat, data.start.lng], 13);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: '© OpenStreetMap contributors © Mapbox',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'your.mapbox.access.token'
    }).addTo(map);

    const points = [[data.start.lat, data.start.lng]];
    L.marker([data.start.lat, data.start.lng]).addTo(map).bindPopup('Start');

    data.waypoints.forEach(function (wp) {
        L.marker([wp.lat, wp.lng]).addTo(map).bindPopup(wp.name || 'Activity');
        points.push([wp.lat, wp.lng]);
    });

    L.marker([data.end.lat, data.end.lng]).addTo(map).bindPopup('End');
    points.push([data.end.lat, data.end.lng]);

    L.polyline(points, { color: 'blue' }).addTo(map);
    map.fitBounds(points);

    document.getElementById('start-point').textContent = data.start.lat + ', ' + data.start.lng;
    document.getElementById('end-point').textContent = data.end.lat + ', ' + data.end.lng;
    const wpList = document.getElementById('waypoints');
    data.waypoints.forEach(function (wp) {
        const li = document.createElement('li');
        li.textContent = (wp.name || '') + ' (' + wp.lat + ', ' + wp.lng + ')';
        wpList.appendChild(li);
    });
});
