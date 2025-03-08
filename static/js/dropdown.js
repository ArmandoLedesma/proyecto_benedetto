document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.getElementById("user-menu-button");
    const userMenu = document.getElementById("user-menu");

    if (menuButton && userMenu) {
        // Estilos iniciales para la animación
        userMenu.classList.add("opacity-0", "scale-95", "hidden", "transition-all", "duration-300", "ease-out");

        // Toggle del menú de usuario al hacer clic en el botón
        menuButton.addEventListener("click", function (event) {
            event.stopPropagation();

            const isHidden = userMenu.classList.contains("hidden");

            if (isHidden) {
                userMenu.classList.remove("hidden");
                setTimeout(() => {
                    userMenu.classList.remove("opacity-0", "scale-95");
                    userMenu.classList.add("opacity-100", "scale-100");
                }, 10);
            } else {
                userMenu.classList.remove("opacity-100", "scale-100");
                userMenu.classList.add("opacity-0", "scale-95");
                setTimeout(() => userMenu.classList.add("hidden"), 300);
            }
        });

        // Cierra el menú si se hace clic fuera de él
        document.addEventListener("click", function (event) {
            if (!menuButton.contains(event.target) && !userMenu.contains(event.target)) {
                userMenu.classList.remove("opacity-100", "scale-100");
                userMenu.classList.add("opacity-0", "scale-95");
                setTimeout(() => userMenu.classList.add("hidden"), 300);
            }
        });
    } else {
        console.warn("Dropdown de usuario no encontrado en esta página.");
    }
});
