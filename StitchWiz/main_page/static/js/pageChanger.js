const toggleCheckbox = document.getElementById('toggleStyleOptions');
const styleOptionsContainer = document.getElementById('styleOptionsContainer');

// Восстановление настроек из localStorage
function applyStoredStyles() {
    const storedFontSize = localStorage.getItem('fontSize');
    const storedTextColor = localStorage.getItem('textColor');
    const storedBgColor = localStorage.getItem('bgColor');

    if (storedFontSize) {
        document.body.style.fontSize = storedFontSize;
    }
    if (storedTextColor) {
        document.body.style.color = storedTextColor;
    }
    if (storedBgColor) {
        document.body.style.backgroundColor = storedBgColor;
    }
}

function createStyleOptions() {
    const form = document.createElement('div');
    form.className = 'style-form';

    const fontSizeLabel = document.createElement('label');
    fontSizeLabel.textContent = 'Размер шрифта:';
    const fontSizeInput = document.createElement('input');
    fontSizeInput.type = 'text';
    fontSizeInput.placeholder = 'Введите размер шрифта';
    fontSizeInput.value = localStorage.getItem('fontSize') || ''; // Устанавливаем значение из localStorage

    const textColorLabel = document.createElement('label');
    textColorLabel.textContent = 'Цвет текста:';
    const textColorInput = document.createElement('input');
    textColorInput.type = 'color';
    textColorInput.value = localStorage.getItem('textColor') || '#000000'; // Устанавливаем значение из localStorage

    const bgColorLabel = document.createElement('label');
    bgColorLabel.textContent = 'Цвет фона страницы:';
    const bgColorInput = document.createElement('input');
    bgColorInput.type = 'color';
    bgColorInput.value = localStorage.getItem('bgColor') || '#ffffff'; // Устанавливаем значение из localStorage

    form.appendChild(fontSizeLabel);
    form.appendChild(fontSizeInput);
    form.appendChild(textColorLabel);
    form.appendChild(textColorInput);
    form.appendChild(bgColorLabel);
    form.appendChild(bgColorInput);

    fontSizeInput.addEventListener('input', function () {
        document.body.style.fontSize = fontSizeInput.value;
        localStorage.setItem('fontSize', fontSizeInput.value); // Сохраняем в localStorage
    });

    textColorInput.addEventListener('input', function () {
        document.body.style.color = textColorInput.value;
        localStorage.setItem('textColor', textColorInput.value); // Сохраняем в localStorage
    });

    bgColorInput.addEventListener('input', function () {
        document.body.style.backgroundColor = bgColorInput.value;
        localStorage.setItem('bgColor', bgColorInput.value); // Сохраняем в localStorage
    });

    return form;
}

toggleCheckbox.addEventListener('change', function () {
    if (toggleCheckbox.checked) {
        const form = createStyleOptions();
        styleOptionsContainer.appendChild(form);
    } else {
        styleOptionsContainer.innerHTML = '';
    }
});

// Применяем сохраненные стили при загрузке страницы
applyStoredStyles();
