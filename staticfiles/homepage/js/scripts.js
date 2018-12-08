
$(document).ready(function () {
    $('.rmFriend').hide();
})



$('.acceptbtn').click(function () {
    $.ajax({
        url: 'ajax/acceptFriend/',
        data: {
            friend: $(this).data('name')
        },
        dataType: 'json',
        success: function (data) {
            if (data.done) {
                var id = 'friendRequest' + data.friend;
                var div = $('#' + id);
                div.empty();
                div.prepend('<p class="list-group-item">Friend request accepted');
            }
        }
    });
})

$('.declinebtn').click(function () {
    $.ajax({
        url: 'ajax/declineFriend/',
        data: {
            friend: $(this).data('name')
        },
        dataType: 'json',
        success: function (data) {
            if (data.done) {
                var id = 'friendRequest' + data.friend;
                var div = $('#' + id);
                div.empty();
                div.prepend('<p class="list-group-item">Friend request declined');
            }
        }
    });
})

$('.cancelbtn').click(function () {
    $.ajax({
        url: 'ajax/cancelFriend/',
        data: {
            friend: $(this).data('name')
        },
        dataType: 'json',
        success: function (data) {
            if (data.done) {
                var id = 'cancelRequest' + data.friend;
                var div = $('#' + id);
                div.empty();
                div.prepend('<p class="list-group-item">Friend request canceled');
            }
        }
    });
})

$('#showrmbtn').click(function() {

    $(this).text(function(i, text){
        return text === "Cancel" ? "Remove friends" : "Cancel";
    });

    $('.rmFriend').each(function () {
        $(this).toggle();
    })
})

$('.rmFriend').click(function () {
    $.ajax({
        url: 'ajax/rmFriend/',
        data: {
            friend: $(this).data('name')
        },
        dataType: 'json',
        success: function (data) {
            if (data.done) {
                var id = 'rmdiv' + data.friend;
                var div = $('#' + id);
                div.empty();
                div.prepend('<p class="list-group-item">User removed from your friends');
            }
        }
    });
})