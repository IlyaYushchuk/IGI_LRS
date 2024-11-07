function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

let newWindow;

document.getElementById('a1').addEventListener('click', async () => {
    // Получаем размеры окна браузера
    let w = window.innerWidth;
    let h = window.innerHeight;
    let password = prompt("Введите пароль");
    if(password==='finita la comedia')
    {// Открываем новое окно
    newWindow = window.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'newWindow', 'width=200,height=200');

    // Проверка, что новое окно открылось успешно
    if (newWindow) {
        // Перемещение нового окна в левый верхний угол

        let x = 0;
        let y = 0;
        let dx = 1;
        let dy = 1;
        let i = 0;
        while (i < 5000) 
        {
            newWindow.moveTo(x, y);
            x += dx;
            y += dy;
            if(x == (screen.width - 200) || x == 0)
            {
                dx = -dx;
            }
            if(y == (screen.height - 200) || y == 0)
            {
                dy = -dy;
            }
            i++;
        }
    }}
});
