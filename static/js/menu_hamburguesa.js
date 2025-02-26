document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.getElementById("menu-toggle");
    const menu = document.getElementById("menu");

    menuToggle.addEventListener("click", function () {
        if (menu.classList.contains("hidden")) {
            menu.classList.remove("hidden");
            menu.classList.remove("opacity-0", "-translate-y-5");
            menu.classList.add("opacity-100", "translate-y-0");
        } else {
            menu.classList.add("opacity-0", "-translate-y-5");
            setTimeout(() => menu.classList.add("hidden"), 300); // Se oculta después de la animación
        }
    });

    window.addEventListener("scroll", function () {
        if (!menu.classList.contains("hidden")) {
            menu.classList.add("opacity-0", "-translate-y-5");
            setTimeout(() => menu.classList.add("hidden"), 300);
        }
    });
});
