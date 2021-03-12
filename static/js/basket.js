$(document).ready(function(){
    $('.basket-list').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        // console.log('Basket ID: ' + t_href.name, '   ', 'Basket Quantity: ' + t_href.value);

        $.ajax({
            url: "/basket-elements/basket-edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
              $('.basket-list').html(data.result);
            },
        });

        event.preventDefault();
    });
});