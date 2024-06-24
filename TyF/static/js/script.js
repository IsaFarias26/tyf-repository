

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




/*====== Prueba-S ======*/

function myFunction() {
    document.getElementById("demo").innerHTML = "CÓMEME LAS BOLAS.";
}






function saludo() {
    alert("Hola Mundo");
}