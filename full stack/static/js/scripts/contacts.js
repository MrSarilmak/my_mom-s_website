function request_ajax(url_str, request_method, data_json) {
    fetch(url_str, {
        headers : {
            'Content-Type' : '<type of json>'
        },
        method : request_method, 
        body : JSON.stringify(data_json)
    })
    .then(function (response){ 
    
        if(response.ok) {  
    
            response.json()
            .then(function(response) {
                var response_string = JSON.stringify(response);
                pars_responce(response_string, '.test');
            });
        }
        else {
            throw Error('Something went wrong');
        }
})
.catch(function(error) {
    console.log(error);
});
}

function http_block() {
    var http_shablon = ``
    return http_shablon;
}


function pars_responce(response_string_w, element) {
    var response_json= JSON.parse(response_string_w);
    var response_obj = response_json["response"]
    var response_type = response_obj["type"]
    var response_data = response_obj["data"]
    if(response_type == "get_all_application"){
        //pass
    }else if(response_type == "delete_application"){
        //pass
    }else{
        console.log("не обрабатываемый тип сообщения");
    }
}

function view_all_application(){
    var request_view_all_application_data = {
        "fragment": "0:10" // $("#redirect_ap_url").val()
    }
    var request_view_all_application = {
        "request": {
            "type": "get_all_application",
            "data": request_view_all_application_data
        }
    };
    request_ajax("/contacts", "POST", request_view_all_application);
}

function delete_application(){
    var request_delete_application_data = {
        "application_id": "-1" // $("#redirect_ap_url").val()
    }
    var request_delete_application = {
        "request": {
            "type": "delete_application",
            "data": request_delete_application_data
        }
    };
    request_ajax("/contacts", "POST", request_delete_application);
}

