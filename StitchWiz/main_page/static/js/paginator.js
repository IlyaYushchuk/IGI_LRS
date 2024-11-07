// Получаем данные о товарах из JSON
let goodsData = JSON.parse(document.getElementById('goods-data').textContent.replace(/<.+>/, ''));

console.log("aaaaaaaaaaaaaaaaaaaa")
const itemsPerPage = 3; // Количество товаров на странице
let currentPage = 1;
function animation()
{
    let shopItems = document.querySelectorAll('.product-card');
    shopItems.forEach(item => {
        item.addEventListener('mousemove', (e) => {
            const rect = item.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
    
            const rotateX = ((y / rect.height) - 0.5) * 45;
            const rotateY = ((x / rect.width) - 0.5) * -45;
    
            item.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
        });
    
        item.addEventListener('mouseleave', () => {
            item.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
        });
    });
}


// Функция для отображения товаров на текущей странице
function displayGoods(page) {
    const productGrid = document.querySelector('.product-grid');
    productGrid.innerHTML = ''; // Очищаем текущий контент

    const start = (page - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const goodsToDisplay = goodsData.slice(start, end); // Получаем нужные товары

    goodsToDisplay.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';

        const img = document.createElement('img');
        img.className = 'product-img';
        img.src = product.image ? product.image : '/media/deps/images/Not found image.png';
        productCard.appendChild(img);

        productCard.innerHTML += `<p class="product-id">id: ${product.display_id}</p>`;
        productCard.innerHTML += `<p class="product-text">Цена: <strong>${product.sell_price} $</strong></p>`;
        productCard.innerHTML += `<p class="product-title">${product.name}</p>`;
        productCard.innerHTML += `<p class="product-text">${product.description}</p>`;
        productCard.innerHTML += `<div class="center-btn"><a class="product-reference" href="/catalog/product/${product.slug}">Подробнее</a></div>`;

        productGrid.appendChild(productCard);
    });

    // Обновляем информацию о текущей странице
    document.getElementById('pageInfo').textContent = `Страница ${currentPage}`;
    document.getElementById('prevBtn').disabled = currentPage === 1;
    document.getElementById('nextBtn').disabled = currentPage * itemsPerPage >= goodsData.length;
}

// Обработчики событий для кнопок
document.getElementById('prevBtn').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        displayGoods(currentPage);
        
    }animation();
});

document.getElementById('nextBtn').addEventListener('click', () => {
    if (currentPage * itemsPerPage < goodsData.length) {
        currentPage++;
        displayGoods(currentPage);
        
    }animation();
});

// Инициализация пагинатора
displayGoods(currentPage);
animation();