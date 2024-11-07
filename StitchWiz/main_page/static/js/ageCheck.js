const btn = document.getElementById('age-btn');

function checkAge()
{
    const birthDateInput = document.getElementById("birth-date").value;
    
    if (!birthDateInput)
    {
        alert("Вы не ввели свой возраст");
        return;
    }
    
    const birthDate = new Date(birthDateInput);
    const today = new Date();
    
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate()))
    {
        age--;
    }

    const daysOfWeek = ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятницу", "субботу"];
    const dayOfWeek = daysOfWeek[birthDate.getDay()];

    const message = document.getElementById("message");
    
    if (age >= 18)
    {
        message.innerHTML = `Возраст: ${age} лет. День недели, когда вы родились: ${dayOfWeek}. Добро пожаловать!`;
    }
    else
    {
        message.innerHTML = `Возраст: ${age} лет. День недели, когда вы родились: ${dayOfWeek}. Пожалуйста, получите разрешение от родителей для использования сайта.`;
        alert("Вы несовершеннолетний. Необходимо разрешение родителей для использования сайта.");
    }
}

btn.addEventListener('click', () => {
    checkAge();
});