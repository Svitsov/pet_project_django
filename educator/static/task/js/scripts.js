// scripts.js

// Функция для увеличенных изображений
function toggleFullscreenImage(imageUrl) {
    const fullscreenImage = document.querySelector('.fullscreen-image');
    const imageElement = fullscreenImage.querySelector('img');

    if (fullscreenImage.style.display === 'flex') {
        fullscreenImage.style.display = 'none';
        imageElement.src = '';
    } else {
        fullscreenImage.style.display = 'flex';
        imageElement.src = imageUrl;
    }
}

// Активация карусели
$(document).ready(function() {
    // Используйте класс carousel для активации всех каруселей на странице
    $('.carousel').carousel();
});

// scripts.js
$(document).ready(function () {
    $('.card').hover(
        function () {
            $(this).addClass('shadow-lg').css('cursor', 'pointer');
        },
        function () {
            $(this).removeClass('shadow-lg');
        }
    );
});


