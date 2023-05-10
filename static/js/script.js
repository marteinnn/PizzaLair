
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
                                    <a class="add-to-cart-btn" href="/cart/add-to-cart/${d.id}">Add to cart</a>
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
                                    <a class="add-to-cart-btn" href="/cart/add-to-cart/${d.id}">Add to cart</a>
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
                                    <a class="add-to-cart-btn" href="/cart/add-to-cart/${d.id}">Add to cart</a>
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
                                    <a class="add-to-cart-btn" href="/cart/add-to-cart/${d.id}">Add to cart</a>
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
                                    <a class="add-to-cart-btn" href="/cart/add-to-cart/${d.id}">Add to cart</a>
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


var form = document.getElementById('contact-form');

// Check if form data is stored in sessionStorage
if (sessionStorage.getItem('form_data')) {
  var data = JSON.parse(sessionStorage.getItem('form_data'));
  form.elements['full-name'].value = data.full_name;
  form.elements['street-name'].value = data.street_name;
  form.elements['house-number'].value = data.house_number;
  form.elements['city'].value = data.city;
  form.elements['country'].value = data.country;
  form.elements['postal-code'].value = data.postal_code;

  // Remove form data from sessionStorage
  sessionStorage.removeItem('form_data');
}

form.addEventListener('submit', function(event) {
  event.preventDefault();
  sessionStorage.setItem('form_data', JSON.stringify({
    'full_name': form.elements['full-name'].value,
    'street_name': form.elements['street-name'].value,
    'house_number': form.elements['house-number'].value,
    'city': form.elements['city'].value,
    'country': form.elements['country'].value,
    'postal_code': form.elements['postal-code'].value,
  }));
  window.location.href = "payment";
});



      var billingAddressSection = document.getElementById("billing-address-section");
      var billingAddressCheckbox = document.getElementById("billing-address-checkbox");

      // Hide the billing address section by default
      billingAddressSection.style.display = "none";

      // Show/hide the billing address section based on the checkbox state
      billingAddressCheckbox.addEventListener("change", function () {
        if (billingAddressCheckbox.checked) {
          billingAddressSection.style.display = "none";
        } else {
          billingAddressSection.style.display = "block";
        }
      });

      // Show the billing address section if the checkbox is unchecked by default
      if (!billingAddressCheckbox.checked) {
        billingAddressSection.style.display = "block";
      }

  var paymentForm = document.getElementById("payment-form");
  var payCheckbox = document.getElementById("pay-checkbox");
  var formElements = paymentForm.elements;

  // Hide form elements and associated labels except for the pay-checkbox and the submit button
  function hideFormElements() {
    for (var i = 0; i < formElements.length; i++) {
      var element = formElements[i];
      if (element.id !== "pay-checkbox" && element.type !== "submit") {
        // Hide the form element
        element.style.display = "none";

        // Hide the associated label if it exists
        var label = document.querySelector("label[for='" + element.id + "']");
        if (label) {
          label.style.display = "none";
        }
      }
    }
  }

  // Show all form elements and associated labels
  function showFormElements() {
    for (var i = 0; i < formElements.length; i++) {
      var element = formElements[i];
      element.style.display = "";

      // Show the associated label if it exists
      var label = document.querySelector("label[for='" + element.id + "']");
      if (label) {
        label.style.display = "";
      }
    }
  }

  // Initial setup: hide form elements and associated labels if pay-checkbox is checked
  if (payCheckbox.checked) {
    hideFormElements();
  }

  // Show/hide form elements and associated labels based on the pay-checkbox state
  payCheckbox.addEventListener("change", function() {
    if (payCheckbox.checked) {
      hideFormElements();
    } else {
      showFormElements();
    }
  });

