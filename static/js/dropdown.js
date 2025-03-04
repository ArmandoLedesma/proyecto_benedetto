document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.getElementById("user-menu-button");
    const userMenu = document.getElementById("user-menu");

    menuButton.addEventListener("click", function (event) {
        userMenu.classList.toggle("hidden");
        event.stopPropagation();
    });

    document.addEventListener("click", function (event) {
        if (!menuButton.contains(event.target) && !userMenu.contains(event.target)) {
            userMenu.classList.add("hidden");
        }
    });
});