document.addEventListener("DOMContentLoaded", function () {
    console.log("🔍 Dropdown con transición JS iniciado");

    function setupDropdowns() {
        const headers = document.querySelectorAll("header"); // Detectar todos los headers

        headers.forEach(header => {
            const menuButton = header.querySelector(".user-btn");
            const userMenu = header.querySelector(".popup-window");

            if (!menuButton || !userMenu) return;

            // Establecer estilos iniciales
            userMenu.style.opacity = "0";
            userMenu.style.transform = "translateY(-10px)";
            userMenu.style.transition = "opacity 0.3s ease-out, transform 0.3s ease-out";
            userMenu.classList.add("hidden");

            menuButton.addEventListener("click", function (event) {
                event.preventDefault();
                event.stopPropagation();

                if (userMenu.classList.contains("hidden")) {
                    userMenu.classList.remove("hidden");

                    // Permitir que el navegador registre el cambio de display antes de animar
                    setTimeout(() => {
                        userMenu.style.opacity = "1";
                        userMenu.style.transform = "translateY(0)";
                    }, 10);
                } else {
                    userMenu.style.opacity = "0";
                    userMenu.style.transform = "translateY(-10px)";

                    setTimeout(() => {
                        userMenu.classList.add("hidden");
                    }, 300); // Ocultar después de la animación
                }
            });

            // Cierre global
            document.addEventListener("click", function (event) {
                if (!header.contains(event.target)) {
                    userMenu.style.opacity = "0";
                    userMenu.style.transform = "translateY(-10px)";

                    setTimeout(() => {
                        userMenu.classList.add("hidden");
                    }, 300);
                }
            });
        });
    }

    setupDropdowns();
    console.log("✅ Dropdown con transición JS completado");
});
