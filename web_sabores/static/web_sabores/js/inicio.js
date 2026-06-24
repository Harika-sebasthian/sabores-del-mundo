document.addEventListener('DOMContentLoaded', function () {
    const scrollHint = document.querySelector('.hero__scroll-hint');
    if (scrollHint) {
        scrollHint.addEventListener('click', function () {
            const concepto = document.querySelector('.concepto');
            if (concepto) {
                concepto.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
});