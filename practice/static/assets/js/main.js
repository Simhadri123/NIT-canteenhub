

document.addEventListener('DOMContentLoaded', () => {
    // Client UI
    ClientDataFlow();
    filtering();

});
// Menu Section -
const menuItems = document.querySelectorAll('.menu-item');

function filtering() {
    const menuFilterBtns = document.querySelectorAll('.filter-btn');
    menuFilterBtns.forEach(function (button) {
        button.addEventListener('click', function () {
            const category = button.dataset.filter;
            filterItems(category);
        });
    });
}

function filterItems(category) {
    menuItems.forEach(function (item) {
        if (category === 'all' || item.querySelector('.item-category').textContent === category) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

filtering();

function ClientDataFlow() {
    // Your ClientDataFlow function remains the same
    const cartBtn = document.querySelector('#cart-btn');
    cartBtn.addEventListener('click', () => {
        displayCartItems();
    });

    const clearCart = document.querySelector('.clear-cart');

    // Clear Cart Btn
    const checkOutBtn = document.querySelector('.check-out');

    

        // Cart Buttons -



    // Remove all items from Cart -
    clearCart.addEventListener('click', () => {
        clearCartItems();
    });

    // User Check Out's -
    checkOutBtn.addEventListener('click', () => {
        placeOrder();
    });
}

function checkCartStatus() {
    fetch('/get_cart_status/')  // Assuming you have a view to get the cart status
        .then(response => response.json())
        .then(data => {
            $('.add-to-cart-btn').each(function() {
                var itemId = $(this).data('id');
                var added = data[itemId] ? true : false;
                $(this).data('added', added);
                if (added) {
                    $(this).text('In Cart').prop('disabled', true);
                } else {
                    $(this).text('Add to Cart').prop('disabled', false);
                }
            });
        })
        .catch(error => console.error('Error:', error));
}
function displayCartItems() {
    fetch('/get_cart_items/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const cartItemsContainer = document.querySelector('.cart-items-container');
            cartItemsContainer.innerHTML = ''; // Clear previous items
            const total_sum = data.total_sum;
            const carttotal = document.querySelector('.cart-total-sum');
            carttotal.innerHTML = `${total_sum}`
            if (data.cart_items.length === 0) {
                const emptyCartMessage = document.createElement('p');
                emptyCartMessage.textContent = 'Your cart is empty.';
                cartItemsContainer.appendChild(emptyCartMessage);
            } else {
                data.cart_items.forEach(cartItem => {
                    const cartItemElement = document.createElement('div');
                    cartItemElement.classList.add('cart-item');
                    cartItemElement.innerHTML = `
                    <article class="menu-item">
                        <img src="/static/${cartItem.imageurl}" loading="lazy" alt="Product image">
                        <div class="item-info">
                            <figure>
                                <h2>${cartItem.title}</h2>
                                <div class="item-category">${cartItem.category}</div>
                            </figure>
                            <hr>
                            <div class="item-quantity" data-id="${cartItem.item_id}">
                                Quantity: 
                                <button class="quantity-btn decrease-btn"><i class="fas fa-minus"></i></button>
                                <span>${cartItem.quantity}</span>
                                <button class="quantity-btn increase-btn"><i class="fas fa-plus"></i></button>
                            </div>
                            <div class="menu-cart-functionality">
                                <div class="price">&#8377;${cartItem.price}</div>
                            </div>
                        </div>
                    </article>
                `;
                    cartItemsContainer.appendChild(cartItemElement);
                });
            }
                const decreaseButtons = document.querySelectorAll('.decrease-btn');
                const increaseButtons = document.querySelectorAll('.increase-btn');

                decreaseButtons.forEach(button => {
                    button.addEventListener('click', function() {
                        const itemId = this.closest('.item-quantity').getAttribute('data-id');
                        decreaseQuantity(itemId);
                    });
                });

                increaseButtons.forEach(button => {
                    button.addEventListener('click', function() {
                        const itemId = this.closest('.item-quantity').getAttribute('data-id');
                        console.log(itemId);
                        increaseQuantity(itemId);
                    });
                });   

        })
        .catch(error => console.error('Error fetching cart items:', error));     
}

if (typeof window !== 'undefined') {
document.addEventListener('DOMContentLoaded', () => {
    // Call the function initially
    checkCartStatus();

    $('.add-to-cart-btn').click(function() {
        var itemId = $(this).data('id');
        var added = $(this).data('added');
        if (!added) {
            addToCart(itemId);
        }
    });
});
}

function addToCart(itemId) {
    fetch('/add_to_cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Ensure to include CSRF token
        },
        body: JSON.stringify({
            itemId: itemId,
        }),
    })
        .then(response => response.json())
        .then(data => {
            // Handle response as needed (e.g., display a message)
            checkCartStatus(); // Update button status after adding to cart
        })
        .catch(error => console.error('Error:', error));
}


function decreaseQuantity(itemId) {
    fetch('/decrease_quantity/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Ensure to include CSRF token
        },
        body: JSON.stringify({
            itemId: itemId,
        }),
    })
        .then(response => response.json())
        .then(data => {
            // Update the quantity display on the page
            if (data.quantity===0){
                displayCartItems();
                checkCartStatus();
            }
            else{
            const quantityElement = document.querySelector(`.item-quantity[data-id="${itemId}"] span`);
            quantityElement.textContent = data.quantity;
            displayCartItems();
            checkCartStatus();
            }
        })
        .catch(error => console.error('Error:', error));
}

function increaseQuantity(itemId) {
    fetch('/increase_quantity/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Ensure to include CSRF token
        },
        body: JSON.stringify({
            itemid: itemId,
        }),
    })
        .then(response => response.json())
        .then(data => {

            const selector = `.item-quantity[data-id="${itemId}"] span`;

            const quantityElement = document.querySelector(selector);
            
            // Check if quantityElement is not null before updating textContent

            if (quantityElement) {
                console.log(data.quantity);
                quantityElement.textContent = data.quantity;
                displayCartItems();
            } else {
                console.error('Quantity element not found');
            }
        })        
        .catch(error => console.error('Error:', error));
}




function clearCartItems() {
    fetch('/clear_cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Ensure to include CSRF token
        },
    })
        .then(response => response.json())
        .then(data => {
            // Handle response as needed (e.g., refresh cart display)
            displayCartItems();
            checkCartStatus();
        })
        .catch(error => console.error('Error:', error));
}

function placeOrder() {
    fetch('/place_order/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Ensure to include CSRF token
        },
    })
        .then(response => {
            if (response.ok) {
                window.location.href = '/user-orders/';  // Redirect to the URL returned by the server
            }
        })
        .then(data => {
        })
        .catch(error => console.error('Error placing order :', error));
}

// Function to get CSRF cookie
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
