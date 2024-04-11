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

