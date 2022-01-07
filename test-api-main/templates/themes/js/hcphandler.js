url = "127.0.0.1:8000/api/"

$("#tenant-form").submit(function(event) {

    event.preventDefault();

    var posting = $.post(url + "create-tenant", {
        name: $('input[name*=tspace_name]').val(),
        name2: $('input[name*=tspace_uname]').val()
    });

    posting.done(function(data) {
        var n = noty({
            text: 'Your tenant created successfully!',
            layout: 'top',
            type: 'success'
        });
    }).fail(function(xhr, textStatus, errorThrown) {
        var n = noty({
            text: xhr.statusText,
            layout: 'top',
            type: 'error'
        });
    });

});

$("#namespace-form").submit(function(event) {

    event.preventDefault();

    var posting = $.post(url + "create-namespace", {
        name: $('input[name*=tspace_name]').val(),
        name2: $('input[name*=tspace_uname]').val()
    });

    posting.done(function(data) {
        var n = noty({
            text: 'Your namespace created successfully!',
            layout: 'top',
            type: 'success'
        });
    }).fail(function(xhr, textStatus, errorThrown) {
        var n = noty({
            text: xhr.statusText,
            layout: 'top',
            type: 'error'
        });
    });

});