const canvas = document.getElementById('canva-1');
const ctx1 = canvas.getContext('2d');

let square = {
    x: 50,
    y: 50,
    size: 30,
    dx: 2, // Начальная скорость по оси X
    dy: 2, // Начальная скорость по оси Y
    color: getRandomColor()
};

let isMoving = true; // Флаг, указывающий на движение
let changeColorEnabled = true; // Флаг, указывающий на возможность изменения цвета

// Функция для генерации случайного цвета
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Функция для анимации квадрата
function drawSquare() {
    ctx1.clearRect(0, 0, canvas.width, canvas.height); // Очистка канваса

    // Отрисовка квадрата
    ctx1.fillStyle = square.color;
    ctx1.fillRect(square.x, square.y, square.size, square.size);

    // Проверка столкновения со стенами
    if (square.x + square.size > canvas.width || square.x < 0) {
        square.dx = -square.dx; // Отскок по оси X
        if (changeColorEnabled) {
            square.color = getRandomColor(); // Изменение цвета
        }
    }
    if (square.y + square.size > canvas.height || square.y < 0) {
        square.dy = -square.dy; // Отскок по оси Y
        if (changeColorEnabled) {
            square.color = getRandomColor(); // Изменение цвета
        }
    }

    // Обновление позиции квадрата
    if (isMoving) {
        square.x += square.dx;
        square.y += square.dy;
    }

    requestAnimationFrame(drawSquare); // Запрос следующего кадра
}

// Запуск анимации
drawSquare();

// Управляющие кнопки
document.getElementById('start-stopButton').onclick = function() {
    isMoving = !isMoving; // Переключение состояния движения
    updateButtonState();
};

document.getElementById('toggleColorButton').onclick = function() {
    changeColorEnabled = !changeColorEnabled;
    this.textContent = changeColorEnabled ? 'Отключить изменение цвета' : 'Включить изменение цвета';
};

document.getElementById('speedUpButton').onclick = function() {
    square.dx *= 1.5; // Увеличение скорости по оси X
    square.dy *= 1.5; // Увеличение скорости по оси Y
};

document.getElementById('slowDownButton').onclick = function() {
    square.dx /= 1.5; // Уменьшение скорости по оси X
    square.dy /= 1.5; // Уменьшение скорости по оси Y
};

// Функция для обновления состояния кнопки
function updateButtonState() {
    const toggleButton = document.getElementById('start-stopButton');
    toggleButton.innerHTML = isMoving ? 'Остановить' : 'Запустить'; // Изменение символа на кнопку
}