// Базовый класс для деталей
class Part {
    constructor(name, cost, quantity) {
        this.name = name;
        this.cost = cost;
        this.quantity = quantity;
    }

    // Геттеры
    getName() {
        return this.name;
    }

    getCost() {
        return this.cost;
    }

    getQuantity() {
        return this.quantity;
    }

    // Сеттеры
    setName(name) {
        this.name = name;
    }

    setCost(cost) {
        this.cost = cost;
    }

    setQuantity(quantity) {
        this.quantity = quantity;
    }

    // Метод для добавления объекта на страницу
    static displayParts(parts) {
        const partsList = document.getElementById('partsList');
        partsList.innerHTML = '<h2>Список деталей на складе:</h2>';
        parts.forEach(part => {
            partsList.innerHTML += `
                <p>${part.getName()} - ${part.getCost()} руб., ${part.getQuantity()} шт.</p>
            `;
        });
    }
}

// Класс-наследник для обработки заказов
class Order extends Part {
    static processOrder(orderItems, parts) {
        let totalCost = 0;
        const orderResult = document.getElementById('orderResult');
        orderResult.innerHTML = '';

        for (const item of orderItems) {
            const part = parts.find(p => p.getName() === item.name);
            if (!part) {
                orderResult.innerHTML += `<p>Деталь "${item.name}" не найдена на складе.</p>`;
                continue;
            }

            if (part.getQuantity() < item.quantity) {
                orderResult.innerHTML += `<p>Недостаточное количество деталей "${item.name}" на складе.</p>`;
                continue;
            }

            totalCost += item.quantity * part.getCost();
        }

        if (orderResult.innerHTML === '') {
            orderResult.innerHTML = `Заказ может быть выполнен. Полная стоимость: ${totalCost} руб.`;
        }
    }
}

// Массив деталей на складе
const parts = [];

// Массив для хранения заказа
const orderItems = [];

// Функция для добавления детали
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
        orderItems.push({ name, quantity });
        displayOrderItems();
        document.getElementById('orderForm').reset();
    } else {
        alert('Введите корректные данные для заказа!');
    }
}

// Функция для отображения списка позиций в заказе
function displayOrderItems() {
    const orderList = document.getElementById('orderList');
    orderList.innerHTML = '<h3>Позиции в заказе:</h3>';
    orderItems.forEach(item => {
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
