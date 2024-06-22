

function showCart() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
}

// Función para cerrar el modal
function closeModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

// Función para agregar un producto al carrito
function addToCart(name, price) {
    const cartItem = { name, price };
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(cartItem);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCart();
}

// Función para actualizar el contenido del carrito
function updateCart() {
    const cartContainer = document.getElementById('cart-items');
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    let total = 0;
    cartContainer.innerHTML = ''; // Limpiar contenido del carrito

    cart.forEach((item, index) => {
        const cartItem = document.createElement('div');
        cartItem.innerHTML = `<p>${item.name} - $${item.price} <button onclick="removeFromCart(${index})">Eliminar</button></p>`;
        cartContainer.appendChild(cartItem);
        total += item.price;
    });

    // Mostrar total
    cartContainer.innerHTML += `<hr><p>Total: $${total.toFixed(2)}</p>`;
}

// Función para limpiar el carrito
function clearCart() {
    localStorage.removeItem('cart');
    updateCart();
}

// Función para eliminar un producto del carrito
function removeFromCart(index) {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCart();
}

// Actualizar el carrito al cargar la página
window.onload = function() {
    updateCart();
}

css


    view-cart {
    position: fixed;
    top: 60px; /* Posición justo debajo del navbar */
    right: 20px;
    z-index: 9999; /* Para que esté por encima del resto del contenido */
}


.modal {
    display: none; /* Ocultar por defecto */
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0,0,0,0.4); /* Fondo oscuro semitransparente */
}


.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
}


.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}
nose si es este
.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}










/*====== Prueba-S ======*/

function myFunction() {
    document.getElementById("demo").innerHTML = "CÓMEME LAS BOLAS.";
}






function saludo() {
    alert("Hola Mundo");
}