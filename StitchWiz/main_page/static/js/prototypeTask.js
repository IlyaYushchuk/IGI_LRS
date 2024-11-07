// Базовый класс для деталей
function Part(name, cost, quantity) {
    this.name = name;
    this.cost = cost;
    this.quantity = quantity;
}

// Методы базового класса
Part.prototype.getName = function () {
    return this.name;
};

Part.prototype.getCost = function () {
    return this.cost;
};

Part.prototype.getQuantity = function () {
    return this.quantity;
};

Part.prototype.setName = function (name) {
    this.name = name;
};

Part.prototype.setCost = function (cost) {
    this.cost = cost;
};

Part.prototype.setQuantity = function (quantity) {
    this.quantity = quantity;
};

// Метод для отображения деталей на странице
Part.displayParts = function (parts) {
    const partsList = document.getElementById('partsList');
    partsList.innerHTML = '<h2>Список деталей на складе:</h2>';
    parts.forEach(function (part) {
        partsList.innerHTML += `
            <p>${part.getName()} - ${part.getCost()} руб., ${part.getQuantity()} шт.</p>
        `;
    });
};

// Класс-наследник для обработки заказов
function Order() {}

// Наследование от Part
Order.prototype = Object.create(Part.prototype);
Order.prototype.constructor = Order;

// Метод для обработки заказа
Order.processOrder = function (orderItems, parts) {
    let totalCost = 0;
    const orderResult = document.getElementById('orderResult');
    orderResult.innerHTML = '';

    orderItems.forEach(function (item) {
        const part = parts.find(function (p) {
            return p.getName() === item.name;
        });

        if (!part) {
            orderResult.innerHTML += `<p>Деталь "${item.name}" не найдена на складе.</p>`;
            return;
        }

        if (part.getQuantity() < item.quantity) {
            orderResult.innerHTML += `<p>Недостаточное количество деталей "${item.name}" на складе.</p>`;
            return;
        }

        totalCost += item.quantity * part.getCost();
    });

    if (orderResult.innerHTML === '') {
        orderResult.innerHTML = `Заказ может быть выполнен. Полная стоимость: ${totalCost} руб.`;
    }
};

// Массив для хранения деталей на складе
const parts = [];

// Массив для хранения позиций заказа
const orderItems = [];

// Функция для добавления детали на склад
function addPart() {
    const name = document.getElementById('partName').value;
    const cost = parseFloat(document.getElementById('partCost').value);
    const quantity = parseInt(document.getElementById('partQuantity').value);

    if (name && cost > 0 && quantity > 0) {
        const newPart = new Part(name, cost, quantity);
        parts.push(newPart);
        Part.displayParts(parts);
        document.getElementById('partForm').reset();
    } else {
        alert('Введите корректные данные!');
    }
}

// Функция для добавления позиции в заказ
function addToOrder() {
    const name = document.getElementById('orderName').value;
    const quantity = parseInt(document.getElementById('orderQuantity').value);

    if (name && quantity > 0) {
        orderItems.push({ name: name, quantity: quantity });
        displayOrderItems();
        document.getElementById('orderForm').reset();
    } else {
        alert('Введите корректные данные для заказа!');
    }
}

// Функция для отображения позиций заказа
function displayOrderItems() {
    const orderList = document.getElementById('orderList');
    orderList.innerHTML = '<h3>Позиции в заказе:</h3>';
    orderItems.forEach(function (item) {
        orderList.innerHTML += `<p>${item.name} - ${item.quantity} шт.</p>`;
    });
}

// Функция для обработки заказа
function processOrder() {
    Order.processOrder(orderItems, parts);
}

// Функция для очистки склада
function clearParts() {
    parts.length = 0; // Очистка массива деталей
    document.getElementById('partsList').innerHTML = '';
}

// Функция для очистки заказа
function clearOrder() {
    orderItems.length = 0; // Очистка массива заказа
    document.getElementById('orderList').innerHTML = '';
    document.getElementById('orderResult').innerHTML = '';
}
