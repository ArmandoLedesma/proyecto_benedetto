document.addEventListener("DOMContentLoaded", function () {
    const categoryLinks = document.querySelectorAll(".category-link");
    const categoryTitle = document.getElementById("categoria-seleccionada");
    const pizzaImages = document.querySelectorAll(".pizza-image"); // Imágenes dentro de las tarjetas

    // Definir las imágenes según la categoría
    const imagesByCategory = {
        "Sencillas": [
            "pizza-menu-1.png", "pizza-menu-2.png", "pizza-menu-3.png",
            "pizza-menu-4.png", "pizza-menu-5.png", "pizza-menu-6.png"
        ],
        "Especiales": [
            "especial-1.png", "especial-2.png", "especial-3.png",
            "especial-4.png", "especial-5.png", "especial-6.png"
        ],
        "Mexicanas": [
            "mexicana-1.png", "mexicana-2.png", "mexicana-3.png",
            "mexicana-4.png", "mexicana-5.png", "mexicana-6.png"
        ],
        "Sorpresa": [
            "sorpresa-1.png", "sorpresa-2.png", "sorpresa-3.png",
            "sorpresa-4.png", "sorpresa-5.png", "sorpresa-6.png"
        ]
    };

    categoryLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            const selectedCategory = this.getAttribute("data-category");

            // Actualizar el título de la categoría
            categoryTitle.textContent = selectedCategory;

            // Cambiar las imágenes de las pizzas
            if (imagesByCategory[selectedCategory]) {
                pizzaImages.forEach((img, index) => {
                    img.src = `/static/img/${imagesByCategory[selectedCategory][index]}`;
                });
            }
        });
    });
});
