$(document).ready(function () {
    // Функция для получения CSRF-токена из куков
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Устанавливаем обработчик события на кнопку лайка
    $('.like-button').click(function () {
        const button = $(this);
        const taskId = button.data('task-id');
        const csrftoken = getCookie('csrftoken');  // Получаем CSRF-токен

        // Включаем CSRF-токен в заголовках запроса
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        });

        // Делаем AJAX-запрос
        $.ajax({
            type: 'POST',
            url: '/toggle_like/' + taskId + '/',
            data: {task_id: taskId},
            success: function (response) {
                button.siblings('.likes-count').text(response.likes_count);
            }
        });
    });

    // Устанавливаем обработчик события на кнопку дизлайка
    $('.dislike-button').click(function () {
        const button = $(this);
        const taskId = button.data('task-id');
        const csrftoken = getCookie('csrftoken');  // Получаем CSRF-токен

        // Включаем CSRF-токен в заголовках запроса
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                }
            }
        });

        // Делаем AJAX-запрос
        $.ajax({
            type: 'POST',
            url: '/toggle_dislike/' + taskId + '/',
            data: {task_id: taskId},
            success: function (response) {
                button.siblings('.dislikes-count').text(response.dislikes_count);
            }
        });
    });

// Полноэкранный режим для изображений
function toggleFullscreenImage() {
    const fullscreenImage = $('.fullscreen-image img');
    const isVisible = fullscreenImage.is(':visible');

    if (isVisible) {
        fullscreenImage.hide();
    } else {
        const imageUrl = fullscreenImage.attr('src');
        if (imageUrl) {
            fullscreenImage.attr('src', imageUrl);
            fullscreenImage.show();
        }
    }
}
});



