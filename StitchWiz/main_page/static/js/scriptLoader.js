function loadScriptAndReload() {
    // Получаем выбранный скрипт
    const selectedScript = document.querySelector('input[name="scriptOption"]:checked').value;
    
    // Сохраняем имя скрипта в localStorage, чтобы использовать его после перезагрузки
    localStorage.setItem('selectedScript', selectedScript);

    // Перезагружаем страницу
    location.reload();
}

// При загрузке страницы проверяем, был ли выбран скрипт
window.onload = function() {
    const selectedScript = localStorage.getItem('selectedScript');
    console.log(selectedScript)
    if (selectedScript) {
        // Создаем элемент <script> и добавляем его в <head> для подключения выбранного скрипта
        const scriptElement = document.createElement('script');
        scriptElement.src = selectedScript;
        document.head.appendChild(scriptElement);
        
        // Устанавливаем выбранное радио значение
        const radioButton = document.querySelector(`input[value="${selectedScript}"]`);
        if (radioButton) {
            radioButton.checked = true;
        }
    }
};