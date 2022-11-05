 
 
 let loclat = document.getElementById("id_lat");
 let loclon = document.getElementById("id_lon");
 let des = document.getElementById("id_address");
 let name = document.getElementById("id_name");
 let pid = document.getElementsByClassName("leaflet-popup-content");


function update_lat(x){
    loclat.value = x;
};
function update_lon(x){
    loclon.value = x;
};
function update_des(x){
    des.value = x;
}

function update_name(x){
    name.value=x;
}

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
            // .setContent("You clicked the map at " + e.latlng.toString())
            .openOn(map)
            let coords = e.latlng            
            let a = coords.lat
            let b = coords.lng
            update_lat(a)
            update_lon(b)
            axios.get(`https://geocode.maps.co/reverse?lat=${a}&lon=${b}`).then(response =>{
                            let clickobj = response.data
                            let c = clickobj['display_name']
                            update_des(c)
                            popup.setContent(c.toString())
                            if(clickobj['address']['building'] != undefined){
                                let a = clickobj['address']['building']
                               
                                update_name(a)
                            }
                            else if(clickobj['address']['shop'] != undefined){
                                let a = clickobj['address']['shop']
                                
                                update_name(a)
                            }
                            else if(clickobj['address']['amenity'] != undefined){
                                let a = clickobj['address']['amenity']
                                
                                update_name(a)
                            } 
                            else if(clickobj['address']['tourism'] != undefined){
                                let a = clickobj['address']['tourism']
                                
                                update_name(a)
                            }
                            else if(clickobj['address']['leisure'] != undefined){
                                let a = clickobj['address']['leisure']
                                
                                update_name(a)
                            }                             
                            else{update_name('')}                            
                            
                            
                            
                        })
            
                
        
    }

map.on('click', onMapClick);

