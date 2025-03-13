/**
 * Script para el formulario de ventas
 * 
 * Maneja la interactividad y validación del formulario
 */



document.addEventListener("DOMContentLoaded", () => {
  // Inicializar elementos del formulario
  initDatePicker();
  initFormElements();
  setupEventListeners();
  setupFormValidation();
  addVisualFeedback();
});

/**
 * Inicializa el selector de fecha con Flatpickr
 */
function initDatePicker() {
  flatpickr("#sale_date", {
    dateFormat: "Y-m-d",
    defaultDate: "today",
    locale: {
      firstDayOfWeek: 1,
      weekdays: {
        shorthand: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"],
        longhand: [
          "Domingo",
          "Lunes",
          "Martes",
          "Miércoles",
          "Jueves",
          "Viernes",
          "Sábado",
        ],
      },
      months: {
        shorthand: [
          "Ene",
          "Feb",
          "Mar",
          "Abr",
          "May",
          "Jun",
          "Jul",
          "Ago",
          "Sep",
          "Oct",
          "Nov",
          "Dic",
        ],
        longhand: [
          "Enero",
          "Febrero",
          "Marzo",
          "Abril",
          "Mayo",
          "Junio",
          "Julio",
          "Agosto",
          "Septiembre",
          "Octubre",
          "Noviembre",
          "Diciembre",
        ],
      },
    },
  });
}

/**
 * Inicializa referencias a elementos del formulario
 */
function initFormElements() {
  window.formElements = {
    form: document.getElementById("salesForm"),
    productSelect: document.getElementById("product"),
    priceInput: document.getElementById("price"),
    quantityInput: document.getElementById("quantity"),
    discountInput: document.getElementById("discount"),
    totalInput: document.getElementById("total"),
    cancelButton: document.getElementById("cancelButton"),
    submitButton: document.querySelector('button[type="submit"]'),
    allInputs: document.querySelectorAll(
      ".form-input, .form-select, .form-textarea"
    ),
  };
}

/**
 * Configura los event listeners para la interactividad del formulario
 */
function setupEventListeners() {
  const {
    productSelect,
    priceInput,
    quantityInput,
    discountInput,
    cancelButton,
  } = window.formElements;

  // Actualizar precio cuando se selecciona un producto
  productSelect.addEventListener("change", function () {
    const selectedOption = this.options[this.selectedIndex];
    const price = selectedOption.getAttribute("data-price");
    if (price) {
      priceInput.value = price;
      calculateTotal();
    }
  });

  // Recalcular total cuando cambian los valores
  priceInput.addEventListener("input", calculateTotal);
  quantityInput.addEventListener("input", calculateTotal);
  discountInput.addEventListener("input", calculateTotal);

  // Botón cancelar
  cancelButton.addEventListener("click", () => {
    if (
      confirm(
        "¿Está seguro que desea cancelar? Se perderán los datos ingresados."
      )
    ) {
      resetForm();
    }
  });
}

/**
 * Calcula el total de la venta basado en precio, cantidad y descuento
 */
function calculateTotal() {
  const { priceInput, quantityInput, discountInput, totalInput } =
    window.formElements;

  const price = Number.parseFloat(priceInput.value) || 0;
  const quantity = Number.parseInt(quantityInput.value) || 0;
  const discount = Number.parseFloat(discountInput.value) || 0;

  const subtotal = price * quantity;
  const discountAmount = subtotal * (discount / 100);
  const total = subtotal - discountAmount;

  totalInput.value = total.toFixed(2);

  // Efecto visual para mostrar el cambio
  totalInput.classList.add("highlight");
  setTimeout(() => {
    totalInput.classList.remove("highlight");
  }, 300);
}

/**
 * Configura la validación del formulario
 */
function setupFormValidation() {
  const { form } = window.formElements;

  form.addEventListener("submit", (event) => {
    let isValid = true;
    const requiredFields = form.querySelectorAll("[required]");

    // Eliminar mensajes de error previos
    document.querySelectorAll(".error-message").forEach((el) => el.remove());

    // Validar campos requeridos
    requiredFields.forEach((field) => {
      field.classList.remove("error");

      if (!field.value.trim()) {
        isValid = false;
        field.classList.add("error");

        // Añadir mensaje de error
        const errorMessage = document.createElement("div");
        errorMessage.className = "error-message text-destructive text-sm mt-1";
        errorMessage.textContent = "Este campo es obligatorio";
        field.parentNode.appendChild(errorMessage);
      }
    });

    // Validar que el precio sea mayor que cero
    const price = Number.parseFloat(document.getElementById("price").value);
    if (price <= 0) {
      isValid = false;
      document.getElementById("price").classList.add("error");

      const errorMessage = document.createElement("div");
      errorMessage.className = "error-message text-destructive text-sm mt-1";
      errorMessage.textContent = "El precio debe ser mayor que cero";
      document.getElementById("price").parentNode.appendChild(errorMessage);
    }

    if (!isValid) {
      event.preventDefault();
      // Scroll al primer campo con error
      const firstError = document.querySelector(".error");
      if (firstError) {
        firstError.scrollIntoView({ behavior: "smooth", block: "center" });
        firstError.focus();
      }
    }
  });
}

/**
 * Añade feedback visual a los campos del formulario
 */
function addVisualFeedback() {
  const { allInputs } = window.formElements;

  allInputs.forEach((input) => {
    // Efecto al enfocar
    input.addEventListener("focus", function () {
      this.classList.add("ring-1", "ring-primary");
    });

    // Quitar efecto al perder foco
    input.addEventListener("blur", function () {
      this.classList.remove("ring-1", "ring-primary");

      // Validar campo al perder foco si es requerido
      if (this.hasAttribute("required") && !this.value.trim()) {
        this.classList.add("error");
      } else {
        this.classList.remove("error");
      }
    });

    // Quitar clase de error cuando el usuario comienza a escribir
    input.addEventListener("input", function () {
      if (this.classList.contains("error")) {
        this.classList.remove("error");
        const errorMessage = this.parentNode.querySelector(".error-message");
        if (errorMessage) {
          errorMessage.remove();
        }
      }
    });
  });
}

/**
 * Resetea el formulario a su estado inicial
 */
function resetForm() {
  const { form, totalInput } = window.formElements;

  // Limpiar todos los campos
  form.reset();

  // Restablecer el total
  totalInput.value = "";

  // Eliminar mensajes de error
  document.querySelectorAll(".error-message").forEach((el) => el.remove());

  // Eliminar clases de error
  document.querySelectorAll(".error").forEach((el) => {
    el.classList.remove("error");
  });
}
