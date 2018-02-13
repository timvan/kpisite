$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});


// function edit_activity(endpoint) {
//     console.log("edit_activity!")
//     console.log(endpoint)
// }


function activity_edit(endpoint, elements){
    // console.log("activity_edit is working") // sanity check
    $.ajax({
        url : endpoint, //url endpoint
        type : "POST", // http method
        data : { 
            datetime_logged : $(elements[0]).val(),
            activity_value : $(elements[1]).val()
            }, // data sent with the request

        // handle a succesful response
        success : function(json){
            // $(elements[0]).val('put json data into here'); // put this into the elemenet
            //console.log(json); // log the returned json to the console to check
            //console.log('ajax success'); // sanity check
            lock_in_activity_form_elements(elements)
        },

        // handle a unsuccessful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Error: "
             + errmsg + " <a href='#' class='close'>&times;</a></div>") // add error to the DOM
            console.log(xhr.status + ": " + xhr,responseText); // provide a bit more info about the error to the console
        }


    })
}

function lock_in_activity_form_elements(elements){

    var id_row = elements[0].split("_")[0]
    var element_parent  = ""
    var element_content = ""
    
    var edit_button = '<button class="' + id_row.substring(1) + ' activity_edit btn btn-success">Edit</button>'
    var submit_button = $(elements[0]).parent().parent().find(".edit_submit")
    
    $(submit_button).replaceWith(edit_button)

    element_parent = $(elements[0]).parent()
    element_content = $(elements[0]).val()
    $(elements[0]).remove()
    $(element_parent).append(element_content)


    element_parent = $(elements[1]).parent()
    element_content = $(elements[1]).val()
    $(elements[1]).remove()
    $(element_parent).append(element_content)


 



    // <td id="row{{ forloop.counter }}_datetime_logged" class="row{{ forloop.counter }}_form">{{ activity.datetime_logged|date:"Y-m-d" }} {{ activity.datetime_logged|time:"H:i:s" }}</td>
    // <td id="row{{ forloop.counter }}_activity_value" class="row{{ forloop.counter }}">{{ activity.activity_value }}</td>
}



