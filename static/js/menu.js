document.addEventListener("DOMContentLoaded", function () {
    const categoryLinks = document.querySelectorAll(".category-link");
    const categoryTitle = document.getElementById("categoria-seleccionada");
    const contenedorProductos = document.getElementById("contenedor-productos");

    // 🔹 Definir ruta base para imágenes
    const BASE_URL_IMG = "/static/img/categorias_productos/";

    // 🔹 Base de datos simulada con múltiples categorías
    const menuCategorias = {
        "pizzas": [
            {   
                nombre: "Hawaiana", 
                imagen: "pizzas/tradicionales/hawaiana.jpg", 
                precio: "12.500",  
                descripcion: "Masa artesanal, pasta de tomate, queso mozzarella, jamón y piña." 
            },
            { 
                nombre: "Jamón queso", 
                imagen: "pizzas/tradicionales/jamon_queso.jpg", 
                precio: "12.500",  
                descripcion: "Masa artesanal, pasta de tomate, queso mozzarella y jamón." 
            },
            { 
                nombre: "Napolitana", 
                imagen: "pizzas/tradicionales/napolitana.jpg", 
                precio: "12.500", 
                descripcion: "Masa artesanal, pasta de tomate, queso mozzarella, rodajas de tomate y orégano." 
            },
            { 
                nombre: "Especial", 
                imagen: "pizzas/autor/especial.jpg", 
                precio: "15.500", 
                descripcion: "Pollo, salami, cábano, achampiñón, cebolla caramelizada y pimentón." 
            },
            { 
                nombre: "Americana", 
                imagen: "pizzas/autor/americana.jpg", 
                precio: "15.500",  
                descripcion: "Masa artesanal, panceta, jalapeños, cebolla roja, cilantro y salsa BBQ." 
            },
            { 
                nombre: "Stracciatella", 
                imagen: "pizzas/autor/stracciatella.webp", 
                precio: "18.500",  
                descripcion: "Pollo, salami, cábano, champiñón, cebolla caramelizada y pimentón." 
            },
        ],

        "hamburguesas": [
            {   nombre: "Clásica", 
                imagen: "hamburguesas/clasica.webp", 
                precio: "15.500",  
                descripcion: "Chedder, mozarella, lechuga, tomate, cebolla roja y salsa de la casa" 
            },
            { 
                nombre: "Bacon", 
                imagen: "hamburguesas/bacon.webp", 
                precio: "18.500",  
                descripcion: "Pan suave y dorado, tocineta, chedder, mozarella y salsa americana." 
            },
            { 
                nombre: "Gaucha", 
                imagen: "hamburguesas/gaucha.webp", 
                precio: "19.000",  
                descripcion: "Chorizo artesanal, chimichurri, chedder, mozarella y salsa de la casa." 
            },
            { 
                nombre: "Philadelphia", 
                imagen: "hamburguesas/philadelphia.webp", 
                precio: "19.000",  
                descripcion: "Tocineta, queso philadelphia, chedder, cebolla al vino tinto y salsa de la casa." 
            },
            { 
                nombre: "Costeña", 
                imagen: "hamburguesas/costena.webp", 
                precio: "19.500",  
                descripcion: "Queso costeño, chedder, mozarella, tocineta, piña y salsa de ajo." 
            },
            { 
                nombre: "Callejera", 
                imagen: "hamburguesas/callejera.webp", 
                precio: "19.500",  
                descripcion: "Carne mixta, queso doble crema, tocineta, salchicha ranchera, huevo frito, papa fosforito y pan suave." 
            },
        ],

        "lazanas": [
            { 
                nombre: "Pollo", 
                imagen: "lazanas/lazana_pollo.jpg", 
                precio: "14.000", 
                descripcion: "Capas de pasta, pollo desmenuzado, bechamel, salsa de tomate y queso gratinado." 
            },
            { 
                nombre: "Pollo champiñón", 
                imagen: "lazanas/lazana_pollo_champinon.jpeg", 
                precio: "15.500", 
                descripcion: "Capas de pasta, pollo desmenuzado, champiñones, bechamel, salsa de tomate y queso gratinado." 
            },
            { 
                nombre: "Mixta", 
                imagen: "lazanas/lazana_mixta.jpg", 
                precio: "15.500", 
                descripcion: "Capas de pasta, carne de res y cerdo, bechamel, salsa de tomate y queso gratinado."
            },
            { 
                nombre: "Carne", 
                imagen: "lazanas/lazana_carne.jpg", 
                precio: "16.000", 
                descripcion: "Capas de pasta, carne molida sazonada, bechamel, salsa de tomate y queso gratinado."
            },
            { 
                nombre: "Espinaca y queso", 
                imagen: "lazanas/lazana_espinaca_queso.jpg", 
                precio: "16.000", 
                descripcion: "Capas de pasta, espinaca salteada, ricotta, bechamel, salsa de tomate y queso gratinado."
            },
            { 
                nombre: "Tres quesos", 
                imagen: "lazanas/lazana_tres_queso.jpg", 
                precio: "17.000", 
                descripcion: "Capas de pasta, mezcla de mozzarella, ricotta y parmesano, bechamel y salsa de tomate."
            },
        ],

        "hotdog": [
            { 
                nombre: "Costeño", 
                imagen: "hotdog/costeno.jpeg", 
                precio: "14.500",  
                descripcion: "Panceta, queso costeño, piña caramelizada, cebolla, salsa americana y papa crocante." 
            },
            { 
                nombre: "Escoces", 
                imagen: "hotdog/escoces.jpeg", 
                precio: "14.500", 
                descripcion: "Panceta ahumada, maíz, queso costeño, salsa tartara y papa cabello de angel." 
            },
            { 
                nombre: "Americano", 
                imagen: "hotdog/americano.jpg", 
                precio: "14.500", 
                descripcion: "Picadillo de pepinillos, panceta de cerdo, cebolla y salsa chedder ahumada." 
            },
            { 
                nombre: "De la casa", 
                imagen: "hotdog/de_la_casa.jpg", 
                precio: "14.500", 
                descripcion: "Ensaladilla de repollo, salsa piña, mayo ajo y papa de cebolla de angel." 
            },
            { 
                nombre: "Choripan argentino", 
                imagen: "hotdog/choripan_argentino.jpg", 
                precio: "15.000", 
                descripcion: "Pan briocho, chorizo artesanal, queso costeño, pico de gallo, chimichurri y salsa de ajo." 
            },
            { 
                nombre: "Callejero", 
                imagen: "hotdog/callejero.jpg", 
                precio: "15.000", 
                descripcion: "Pan suave, queso costeño, salsa de la casa, romero, cebolla en rodajas." 
            }
        ]
    };

    // 🔹 Función para actualizar la categoría y mostrar los productos
    function actualizarCategoria(categoria) {
        const categoriaLower = categoria.toLowerCase();
        categoryTitle.textContent = categoria;

        // Limpiar contenedor antes de insertar nuevos elementos
        contenedorProductos.innerHTML = "";

        // Verificar si la categoría existe
        if (!menuCategorias[categoriaLower]) {
            console.error("Categoría no encontrada:", categoriaLower);
            return;
        }

        // Generar dinámicamente los productos
        menuCategorias[categoriaLower].forEach(producto => {
            const card = document.createElement("div");
            card.classList.add("relative", "bg-gray-100", "p-4", "rounded-lg", "shadow-lg", "text-center");

            // 🔹 Obtener la ruta de la imagen asegurando que tenga la base correcta
            const imagenSrc = `${BASE_URL_IMG}${producto.imagen}`;

            // 🔹 Badge de descuento
            const descuentoHTML = producto.descuento
                ? `<span class="absolute top-2 right-2 bg-red-600 text-white text-xs font-bold px-2 py-1 rounded-lg">
                        ${producto.descuento} OFF
                   </span>`
                : "";

            // 🔹 Badge de subcategoría (Solo para pizzas)
            const subcategoriaHTML = producto.subcategoria
                ? `<span class="absolute top-2 left-2 bg-gray-800 text-white text-xs font-bold px-2 py-1 rounded-lg">
                        ${producto.subcategoria}
                   </span>`
                : "";

            card.innerHTML = `
                ${descuentoHTML}
                ${subcategoriaHTML}
                <a href="#">
                    <img src="${imagenSrc}" 
                         alt="${producto.nombre}" 
                         class="w-full h-48 sm:h-56 md:h-64 object-cover rounded-md">
                </a>
                <h4 class="text-xl font-bold text-gray-900 mt-4">${producto.nombre}</h4>
                <p class="text-gray-600 text-sm">${producto.descripcion}</p>
                <p class="text-red-600 text-lg font-semibold mt-2">$${producto.precio}</p>
                <button class="mt-3 px-4 py-2 bg-lime-600 text-white rounded-lg shadow-md hover:bg-lime-700 transition">
                    Agregar al carrito
                </button>
            `;

            contenedorProductos.appendChild(card);
        });
    }

    // 🔹 Evento de clic en las categorías
    categoryLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            const selectedCategory = this.getAttribute("data-category");
            categoryLinks.forEach(l => l.classList.remove("border-red-600", "font-semibold"));
            this.classList.add("border-red-600", "font-semibold");

            actualizarCategoria(selectedCategory);
        });
    });

    // 🔹 Cargar la primera categoría al iniciar
    actualizarCategoria("pizzas");
});
