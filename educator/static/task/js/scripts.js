// scripts.js

// Функция для увеличенных изображений
let fullscreenImageUrl = '';

function toggleFullscreenImage(imageUrl) {
    const fullscreenImage = document.querySelector('.fullscreen-image');
    const imageElement = fullscreenImage.querySelector('img');

    if (fullscreenImage.style.display === 'none' || fullscreenImageUrl !== imageUrl) {
        fullscreenImageUrl = imageUrl;
        fullscreenImage.style.display = 'flex';
        imageElement.src = imageUrl;
    } else {
        fullscreenImageUrl = '';
        fullscreenImage.style.display = 'none';
        imageElement.src = '';
    }
}

// Активация карусели
$(document).ready(function() {
    $('#imageCarousel').carousel();
});
