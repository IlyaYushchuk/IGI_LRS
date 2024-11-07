document.getElementById('speakButton').addEventListener('click', () => {
    const textInput = document.getElementById('textInput').value;
   
    if (textInput) {
        generateSpeech(textInput);
    } else {
        alert('Пожалуйста, введите текст.');
    }
});

function generateSpeech(text) {
    const speech = new SpeechSynthesisUtterance(text); // Создаем объект для синтеза речи
    speech.lang = 'ru-RU'; // Указываем язык (в данном случае русский)

    // Опционально: можете задать дополнительные параметры
    speech.volume = 1; // Громкость (от 0 до 1)
    speech.rate = 1;   // Скорость (от 0.1 до 10)
    speech.pitch = 1;  // Высота тона (от 0 до 2)

    window.speechSynthesis.speak(speech); // Проигрываем синтезированную речь
}

document.getElementById('jokeButton').addEventListener('click', () => {
    fetch('https://v2.jokeapi.dev/joke/Any') // Запрос к JokeAPI
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Получаем данные в формате JSON
        })
        .then(data => {
            // Проверяем тип шутки и отображаем её
            let jokeText = '';
            if (data.type === 'single') {
                jokeText = data.joke; // Если шутка одиночная
            } else {
                jokeText = `${data.setup} - ${data.delivery}`; // Если шутка с установкой и развязкой
            }
            document.getElementById('jokeLabel').textContent = jokeText; // Вставляем шутку в label
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
            document.getElementById('jokeLabel').textContent = 'Не удалось получить шутку. Попробуйте позже.'; // Сообщение об ошибке
        });
});
