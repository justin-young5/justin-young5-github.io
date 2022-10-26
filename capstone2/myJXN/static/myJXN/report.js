 
 
 let loc = document.getElementById("id_location");

 function update(x){
    loc.value = x;
};

//leaflet js
var map = L.map('map').setView([32.308, -90.194], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

var popup = L.popup();

function onMapClick(e) {
    popup
            .setLatLng(e.latlng)
            .setContent("You clicked the map at " + e.latlng.toString())
            .openOn(map)
            let coords = e.latlng
            a = `${coords.lat}, ${coords.lng}`
            update(a)
            console.log(loc.value);
        
    }

map.on('click', onMapClick);

