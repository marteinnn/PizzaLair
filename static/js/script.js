
const TOKEN = '{% csrf_token %}'
$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
       e.preventDefault();
       let searchText = $('#search-box').val();
       $.ajax({
           url: '/order?search_filter='+ searchText,
           type: 'GET',
           success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<a href="/order/${d.id}">
                                <div class="pizza_item">
                                    <img class="pizza-image" src="../static/images/${d.image}"/>
                                    <h4>${d.name}</h4>
                                    <p>
                                    ${d.toppings}
                                    </p>
                                    <h2>${d.price} $</h2>
                                        <form method="POST" action="/cart/add-to-cart/${d.id}">
                                            {{ csrf_token }}
                                            <button type="submit">Add to cart</button>
                                        </form>
                                </div>
                            </a>`
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
                    return `<a href="/order/${d.id}">
                                <div class="pizza_item">
                                    <img class="pizza-image" src="../static/images/${d.image}"/>
                                    <h4>${d.name}</h4>
                                    <p>
                                    ${d.toppings}
                                    </p>
                                    <h2>${d.price} $</h2>
                                        <form method="POST" action="/cart/add-to-cart/${d.id}">
                                            {{ csrf_token }}
                                            <button type="submit">Add to cart</button>
                                        </form>
                                </div>
                            </a>`
                });
                $(".order-items").html(newHtml.join(''));
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
                    return `<a href="/order/${d.id}">
                                <div class="pizza_item">
                                    <img class="pizza-image" src="../static/images/${d.image}"/>
                                    <h4>${d.name}</h4>
                                    <p>
                                    ${d.toppings}
                                    </p>
                                    <h2>${d.price} $</h2>
                                        <form method="POST" action="/cart/add-to-cart/${d.id}">
                                            {{ csrf_token }}
                                            <button type="submit">Add to cart</button>
                                        </form>
                                </div>
                            </a>`
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
    $('#name-btn').on('click', function(e) {
       e.preventDefault();
       $.ajax({
           url: '/order?check_filter=sortbyname',
           type: 'GET',
           success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<a href="/order/${d.id}">
                                <div class="pizza_item">
                                    <img class="pizza-image" src="../static/images/${d.image}"/>
                                    <h4>${d.name}</h4>
                                    <p>
                                    ${d.toppings}
                                    </p>
                                    <h2>${d.price} $</h2>
                                        <form method="POST" action="/cart/add-to-cart/${d.id}">
                                            {{ csrf_token }}
                                            <button type="submit">Add to cart</button>
                                        </form>
                                </div>
                            </a>`
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
    $('#price-btn').on('click', function(e) {
       e.preventDefault();
       $.ajax({
           url: '/order?check_filter=sortbyprice',
           type: 'GET',
           success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<a href="/order/${d.id}">
                                <div class="pizza_item">
                                    <img class="pizza-image" src="../static/images/${d.image}"/>
                                    <h4>${d.name}</h4>
                                    <p>
                                    ${d.toppings}
                                    </p>
                                    <h2>${d.price} $</h2>
                                        <form method="POST" action="/cart/add-to-cart/${d.id}">
                                            {{ csrf_token }}
                                            <button type="submit">Add to cart</button>
                                        </form>
                                </div>
                            </a>`
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

let btns = document.querySelectorAll(".pizza_item button")
