$(document).ready(function() {
    $('.delete-btn').click(function(e){
        e.preventDefault();
        if (confirm("Are you sure you want to delete this user ?")) {
            var userId = $(this).data('user-id');
            let csrftoken = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                type:'POST',
                url: '/delete/' + userId + '/',
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('X-CSRFToken',csrftoken);
                },
                success: function(response) {
                    window.location.href = "/employees/";
                },
                error: function(xhr, status, error) {
                    console.error(xhr.responseText);
                }
            });
        }
    });
});

$(document).ready(function() {
    $('.delete-btn1').click(function(e) {
        e.preventDefault();
        if (confirm('Are you sure you want to delete this ticket?')) {
            var ticketId = $(this).data('ticket-id');
            let csrftoken = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                type:'POST',
                url: '/delete_ticket/' + ticketId + '/',
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                },
                success: function(response) {
                    window.location.href = "/";
                },
                error: function(xhr, status, error) {
                    console.error(xhr.responseText);
                }
            });
        }
    });
});

$(document).ready(function() {
    $('.edit-btn').click(function(e){
        e.preventDefault();

        var ticketId = $(this).data('ticket-id');
        let csrftoken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method:'POST',
            url: '/edit_ticket/' + ticketId + '/',
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken)
            },
            success: function(response) {
                window.location.href = "/edit_ticket/" + ticketId + "/";
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });
});