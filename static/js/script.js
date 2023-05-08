function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


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

let btns = document.querySelectorAll(".pizza_item button")

btns.forEach(btn=>{
    btn.addEventListener("click", addToCart)
})

function addToCart(e){
    let pizza_id = e.target.value
    let url = "cart/add_to_cart"

    let data = {id:pizza_id}

    fetch(url, {
        method: 'POST',
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
    })
    .catch(error=>{
        console.log(error)
    })
}
