document.addEventListener("DOMContentLoaded", function () {
    // Lista de inputs de contraseña con sus respectivos iconos
    const passwordFields = [
        { inputId: "password", toggleId: "toggle-password" },
        { inputId: "confirmPassword", toggleId: "toggle-confirmPassword" }
    ];

    passwordFields.forEach(({ inputId, toggleId }) => {
        let passwordInput = document.getElementById(inputId);
        let toggleIcon = document.querySelector(`#${toggleId} i`);

        // Evento para cambiar la visibilidad de la contraseña
        document.getElementById(toggleId).addEventListener("click", function () {
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                toggleIcon.classList.replace("fa-eye", "fa-eye-slash");
            } else {
                passwordInput.type = "password";
                toggleIcon.classList.replace("fa-eye-slash", "fa-eye");
            }
        });

        // Asegurar que el icono refleje correctamente el estado al cargar la página
        syncPasswordVisibility(passwordInput, toggleIcon);
    });

    function syncPasswordVisibility(passwordInput, toggleIcon) {
        if (passwordInput.type === "password") {
            toggleIcon.classList.add("fa-eye");
            toggleIcon.classList.remove("fa-eye-slash");
        } else {
            toggleIcon.classList.add("fa-eye-slash");
            toggleIcon.classList.remove("fa-eye");
        }
    }
});
