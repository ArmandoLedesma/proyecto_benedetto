document.addEventListener("DOMContentLoaded", () => {
    const carousel = document.querySelector("#testimonial-carousel div");
    const prevButton = document.getElementById("prev-testimonial");
    const nextButton = document.getElementById("next-testimonial");

    let index = 0;

    function moveCarousel(direction) {
        const items = document.querySelectorAll("#testimonial-carousel div > div");
        const totalItems = items.length;
        index = (index + direction + totalItems) % totalItems;
        carousel.style.transform = `translateX(-${index * 100}%)`;
    }

    prevButton.addEventListener("click", () => moveCarousel(-1));
    nextButton.addEventListener("click", () => moveCarousel(1));
});
