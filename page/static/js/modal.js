document.addEventListener('DOMContentLoaded', function() {
    var openModalBtn = document.getElementById("openModalBtn");
    var closeModalBtn = document.getElementById("closeModalBtn");
    var modal = document.getElementById('myModal');
    var categoryLinks = document.querySelectorAll('.category');
    var subcategoryModals = document.querySelectorAll('.subcategory');

    openModalBtn.onclick = function() {
        modal.style.display = "block";
    }

    closeModalBtn.onclick = function() {
        modal.style.display = "none";
        subcategoryModals.forEach(function(modal) {
            modal.classList.remove('show');
        });

        // Удаляем класс активного состояния у всех категорий при закрытии модального окна
        categoryLinks.forEach(function(link) {
            link.classList.remove('active');
        });
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            subcategoryModals.forEach(function(modal) {
                modal.classList.remove('show');
            });

            // Удаляем класс активного состояния у всех категорий при закрытии модального окна
            categoryLinks.forEach(function(link) {
                link.classList.remove('active');
            });
        }
    }

    categoryLinks.forEach(function(link) {
        link.onclick = function(event) {
            event.preventDefault();

            // Скрыть все подкатегории
            subcategoryModals.forEach(function(modal) {
                modal.classList.remove('show');
            });

            // Показать выбранную подкатегорию
            var categoryId = this.getAttribute('data-category');
            document.getElementById(categoryId).classList.add('show');

            // Удаляем класс активного состояния у всех категорий
            categoryLinks.forEach(function(link) {
                link.classList.remove('active');
            });

            // Добавляем класс активного состояния к текущей категории
            this.classList.add('active');
        };
    });
});
