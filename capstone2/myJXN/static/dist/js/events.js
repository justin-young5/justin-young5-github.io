
    let app = new Vue({
        el: '#app',
        delimiters: ['${','}'],
        data:{
            message: 'hello world!',
            djangoapi: [],
        },
        methods:{
            sayHello: function(){
                console.log(this.message)
            },
            loadAPI: function(){
                axios({
                    methods: 'get',
                    url: 'http://127.0.0.1:8000/myJXN/v1/',
                    headers: {
                    //   'Authorization': '48d0bddf-6f20-4781-8f62-b004b4095c87',
                    },
                }).then(response =>{
                    this.djangoapi = response.data
                    console.log(this.djangoapi[0])
                    for(let obj in this.djangoapi){
                        let objlat = this.djangoapi[obj].lat;
                        let objlon = this.djangoapi[obj].lon;
                        let title = this.djangoapi[obj].description;
                        let picture = this.djangoapi[obj].picture;
                        objlat = parseFloat(objlat)
                        objlon = parseFloat(objlon)                        
                        var markerOptions = {
                            title: this.djangoapi[obj].description,
                            clickable: true,
                        }
                        var marker = L.marker([objlat, objlon], markerOptions);
                        marker.addTo(map).bindPopup(title + "<br/><img src=" + picture + " height='300' width='auto'/>",{maxWidth: "auto"});
                        console.log(`${this.djangoapi[obj].id} ${this.djangoapi[obj].description}`);
                    }
                })
                    
            },
        },
            mapRefresh: function(){
                map.panTO([32.308, -90.194])
            },
        
        created: function(){
            this.loadAPI()
        },
    })
