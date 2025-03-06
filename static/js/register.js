document.addEventListener("DOMContentLoaded", function () {
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");
    const passwordError = document.getElementById("passwordError");
    const passwordSuccess = document.getElementById("passwordSuccess");
    const submitButton = document.getElementById("submitButton");

    function validatePasswords() {
        if (password.value === "" || confirmPassword.value === "") {
            passwordError.classList.add("hidden");
            passwordSuccess.classList.add("hidden");
            confirmPassword.classList.remove("border-red-500", "border-green-500");
            submitButton.disabled = true;
        } else if (password.value !== confirmPassword.value) {
            passwordError.classList.remove("hidden");
            passwordSuccess.classList.add("hidden");
            confirmPassword.classList.add("border-red-500");
            confirmPassword.classList.remove("border-green-500");
            submitButton.disabled = true;
        } else {
            passwordError.classList.add("hidden");
            passwordSuccess.classList.remove("hidden");
            confirmPassword.classList.add("border-green-500");
            confirmPassword.classList.remove("border-red-500");
            submitButton.disabled = false;
        }
    }

    password.addEventListener("input", validatePasswords);
    confirmPassword.addEventListener("input", validatePasswords);
});
