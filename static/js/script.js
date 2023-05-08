$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
       e.preventDefault();
       let searchText = $('#search-box').val();
       $.ajax({
           url: '/order?search_filter='+ searchText,
           type: 'GET',
           success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="pizza-item">
                            <img class="pizza-image" src="../static/images/${d.image}"/>
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                            <h2>${d.price} $</h2>
                            <button>Add to cart!</button>
                            </div>`
                });
                $('.order-items').html(newHtml.join(''));
                $('#search-box').val('')

           },
           error: function(xhr, status, error) {
               console.error(error);
           }
       })
    });
});

$(document).ready(function() {
    $('#vegan-btn').on('click', function(e) {
       e.preventDefault();
       let searchText = $('#search-box').val();
       $.ajax({
           url: '/order?check_filter=vegan',
           type: 'GET',
           success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="pizza-item">
                            <img class="pizza-image" src="../static/images/${d.image}"/>
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                            <h2>${d.price} $</h2>
                            <button>Add to cart!</button>
                            </div>`
                });
                $('.order-items').html(newHtml.join(''));
                $('#search-box').val('')

           },
           error: function(xhr, status, error) {
               console.error(error);
           }
       })
    });
});

$(document).ready(function() {
    $('#spicy-btn').on('click', function(e) {
       e.preventDefault();
       $.ajax({
           url: '/order?check_filter=spicy',
           type: 'GET',
           success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="pizza-item">
                            <img class="pizza-image" src="../static/images/${d.image}"/>
                            <h4>${d.name}</h4>
                            <p>${d.description}</p>
                            <h2>${d.price} $</h2>
                            <button>Add to cart!</button>
                            </div>`
                });
                $('.order-items').html(newHtml.join(''));
                $('#search-box').val('')

           },
           error: function(xhr, status, error) {
               console.error(error);
           }
       })
    });
});