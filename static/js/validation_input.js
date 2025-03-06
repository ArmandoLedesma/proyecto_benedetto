document.getElementById('email').addEventListener('input', function() {
    const emailError = document.getElementById('email-error');
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Expresión regular para validar emails

    if (this.value.trim() === '') {
        emailError.classList.add('hidden'); // Ocultar el mensaje de error
        this.classList.remove('border-red-500', 'border-green-500'); // Restaurar el borde normal
    } else if (!emailPattern.test(this.value)) {
        emailError.classList.remove('hidden'); // Mostrar mensaje de error
        this.classList.add('border-red-500');  // Borde rojo
        this.classList.remove('border-green-500'); // Quitar borde verde si lo tenía
    } else {
        emailError.classList.add('hidden'); // Ocultar mensaje de error
        this.classList.remove('border-red-500'); // Quitar borde rojo si lo tenía
        this.classList.add('border-green-500'); // Borde verde para indicar éxito
    }
});
