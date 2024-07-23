

function get_geolocation(callback){
    var uiAddress = document.getElementById('address')
    var geocode_url = 'https://geocode.maps.co/search?q='+'\''+uiAddress.value+'\''+'&api_key=66992dafe112a189439452vcs987e60'
    var uiLat, uiLon;
    
    $.get(geocode_url,function(data,status){
        console.log("Getting co-ordinates")

        try {
            uiLat = parseFloat(data[0].lat)
            uiLon = parseFloat(data[0].lon)
            console.log(uiLat)
            console.log(uiLon)
            callback(uiLon, uiLat)
        } catch (error) {
            estimated_price.innerHTML = '<h2>' + error + '<h2>'
        }
        
    })
}

function onclickEstimatePrice(){
    
    var uiBedrooms = document.getElementById('bedrooms')
    var uiBathrooms = document.getElementById('bathrooms')
    var uiSq_feet = document.getElementById('sq_feet')
    var uiFurnishing = document.getElementById('furnishing_')
    var uiType = document.getElementById('type_')
    

    var prediction_url = 'http://127.0.0.1:5000/predict_home_price';
    //var prediction_url = '/api/predict_home_price';

    get_geolocation(function(uiLon, uiLat){

        $.post(prediction_url, {
            latitude: uiLat,
            longitude: uiLon,
            sq_feet: parseFloat(uiSq_feet.value),
            bedrooms: parseFloat(uiBedrooms.value),
            bathrooms: parseFloat(uiBathrooms.value),
            type: uiType.value,
            furnishing: uiFurnishing.value
    
        }, function(data,status){
            console.log(data['estimated_price']);
            estimated_price.innerHTML = '<h2>' + '$ ' + data['estimated_price'].toString() + '<h2>'
            console.log(status)
        })
        
    })

}

function onpageload(){
    console.log("Document loaded");
    var furnishing_url = 'http://127.0.0.1:5000/get_furnishing_names';
    var type_url = 'http://127.0.0.1:5000/get_type_names';
    //var furnishing_url = '/api/get_furnishing_names';
    //var type_url = '/api/get_type_names';

    $.get(furnishing_url, function(data,status){
        console.log("Got response for get_furnishing_names request");
        if(data){
            var furnishing_data = data['furnishing'];
            furnishing_data.push('other')
            var furnishing_ = document.getElementById('furnishing_');
            $('#furnishing_').empty();
            for(var i in furnishing_data){
                var opt = new Option(furnishing_data[i]);
                $('#furnishing_').append(opt);
            }
        }
    });

    $.get(type_url, function(data,status){
        console.log("Got response for get_type_names request");
        if(data){
            var type_data = data['type'];
            type_data.push('acreage')
            var type_ = document.getElementById('type_');
            $('#type_').empty();
            for(var i in type_data){
                var opt = new Option(type_data[i]);
                $('#type_').append(opt);
            }
        }
    });

}

window.onload = onpageload;