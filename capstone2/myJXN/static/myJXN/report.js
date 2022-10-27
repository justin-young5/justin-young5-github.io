 
 
 let loclat = document.getElementById("id_lat");
 let loclon = document.getElementById("id_lon");


function update_lat(x){
    loclat.value = x;
};
function update_lon(x){
    loclon.value = x;
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
            let a = coords.lat
            let b = coords.lng
            update_lat(a)
            update_lon(b);
        
    }

map.on('click', onMapClick);

