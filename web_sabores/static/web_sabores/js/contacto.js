// Validaciones del formulario

document.addEventListener('DOMContentLoaded', function () {

    const form     = document.getElementById('contacto-form');
    const nombre   = document.getElementById('nombre');
    const email    = document.getElementById('email');
    const asunto   = document.getElementById('asunto');
    const mensaje  = document.getElementById('mensaje');
    const charCount = document.getElementById('char-count');

    // ── CONTADOR DE CARACTERES ─────────────────────────
    if (mensaje && charCount) {
        mensaje.addEventListener('input', function () {
            const len = this.value.length;
            charCount.textContent = `${len} / 500`;
            charCount.style.color = len > 450 ? '#FF7F11' : '';
            if (len > 500) {
                this.value = this.value.substring(0, 500);
            }
        });
    }

    // ── VALIDACIÓN EN TIEMPO REAL ──────────────────────
    function mostrarError(input, msg) {
        const group = input.closest('.form-group');
        const error = group.querySelector('.form-error-msg');
        if (error) error.textContent = msg;
        input.style.borderColor = '#ef4444';
    }

    function limpiarError(input) {
        const group = input.closest('.form-group');
        const error = group.querySelector('.form-error-msg');
        if (error) error.textContent = '';
        input.style.borderColor = '';
    }

    function validarEmail(value) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    }

    if (nombre) {
        nombre.addEventListener('blur', function () {
            if (!this.value.trim()) {
                mostrarError(this, 'El nombre es obligatorio.');
            } else if (this.value.trim().length < 2) {
                mostrarError(this, 'El nombre debe tener al menos 2 caracteres.');
            } else {
                limpiarError(this);
            }
        });
    }

    if (email) {
        email.addEventListener('blur', function () {
            if (!this.value.trim()) {
                mostrarError(this, 'El correo es obligatorio.');
            } else if (!validarEmail(this.value.trim())) {
                mostrarError(this, 'Ingresá un correo válido con @.');
            } else {
                limpiarError(this);
            }
        });
    }

    if (asunto) {
        asunto.addEventListener('change', function () {
            if (!this.value) {
                mostrarError(this, 'Seleccioná un motivo.');
            } else {
                limpiarError(this);
            }
        });
    }

    if (mensaje) {
        mensaje.addEventListener('blur', function () {
            if (!this.value.trim()) {
                mostrarError(this, 'El mensaje es obligatorio.');
            } else if (this.value.trim().length < 10) {
                mostrarError(this, 'El mensaje debe tener al menos 10 caracteres.');
            } else {
                limpiarError(this);
            }
        });
    }

    // ── VALIDACIÓN AL ENVIAR ───────────────────────────
    if (form) {
        form.addEventListener('submit', function (e) {
            let valido = true;

            if (!nombre.value.trim()) {
                mostrarError(nombre, 'El nombre es obligatorio.');
                valido = false;
            }
            if (!email.value.trim() || !validarEmail(email.value.trim())) {
                mostrarError(email, 'Ingresá un correo válido con @.');
                valido = false;
            }
            if (!asunto.value) {
                mostrarError(asunto, 'Seleccioná un motivo.');
                valido = false;
            }
            if (!mensaje.value.trim() || mensaje.value.trim().length < 10) {
                mostrarError(mensaje, 'El mensaje debe tener al menos 10 caracteres.');
                valido = false;
            }

            if (!valido) {
                e.preventDefault();
                const primerError = form.querySelector('input[style*="border-color"], select[style*="border-color"], textarea[style*="border-color"]');
                if (primerError) primerError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    }
});