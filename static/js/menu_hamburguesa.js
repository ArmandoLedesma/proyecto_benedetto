document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menu-toggle");
    const menu = document.getElementById("menu");
    const closeMenu = document.getElementById("close-menu");

    if (menuToggle && menu) {
        menuToggle.addEventListener("click", function () {
            const isHidden = menu.classList.contains("hidden");

            if (isHidden) {
                menu.classList.remove("hidden");
                menu.classList.add("opacity-100", "translate-y-0");
                document.body.classList.add("overflow-hidden"); // Evita desplazamiento cuando el menú está abierto
            } else {
                menu.classList.add("opacity-0", "-translate-y-5");
                setTimeout(() => menu.classList.add("hidden"), 300);
                document.body.classList.remove("overflow-hidden");
            }
        });

        // Botón para cerrar menú (opcional)
        if (closeMenu) {
            closeMenu.addEventListener("click", function () {
                menu.classList.add("opacity-0", "-translate-y-5");
                setTimeout(() => menu.classList.add("hidden"), 300);
                document.body.classList.remove("overflow-hidden");
            });
        }

        // Opción: Cerrar menú al hacer clic en un enlace
        document.querySelectorAll("#menu a").forEach(link => {
            link.addEventListener("click", function () {
                menu.classList.add("opacity-0", "-translate-y-5");
                setTimeout(() => menu.classList.add("hidden"), 300);
                document.body.classList.remove("overflow-hidden");
            });
        });
    } else {
        console.warn("El menú hamburguesa no se encontró en esta página.");
    }
});
