const smContainer = document.querySelectorAll('.machines-container');
const sm1 = document.getElementById('Image1');
const sm2 = document.getElementById('Image2');
const sm3 = document.getElementById('Image3');
const sm4 = document.getElementById('Image4');


        // Добавляем обработчик для события прокрутки
window.addEventListener('scroll', function() {
    // Получаем значение прокрутки
    
    //this.alert(this.window.outerHeight + ' ' + scrollPosition);
    //  alert();
    //console.log(scrollPosition);
    // Рассчитываем смещение бутылки на основе прокрутки
    const scrollPosition = window.scrollY;
    let cadr = 100;
    let angle = 10;
    let anglePerCadr = cadr/2;

    if( Math.floor(scrollPosition / anglePerCadr) % 4 === 0)
    {
        sm1.style.transform = `rotate(${angle}deg)`;   
    }
    if( Math.floor(scrollPosition / anglePerCadr) % 4 === 1)
    {
        sm1.style.transform = `rotate(${-angle}deg)`;   
    }
    if( Math.floor(scrollPosition / anglePerCadr) % 4 === 2)
    {
        sm1.style.transform = `rotate(${-angle}deg)`;   
    }
    if( Math.floor(scrollPosition / anglePerCadr) % 4 === 3)
    {
        sm1.style.transform = `rotate(${angle}deg)`;   
    }


   

    // if( Math.floor(scrollPosition / anglePerCadr) % 4 === 0)
    // {
    //     sm2.style.transform = `rotate(${angle}deg)`;   
    // }
    // if( Math.floor(scrollPosition / anglePerCadr) % 4 === 1)
    // {
    //     sm2.style.transform = `rotate(${-angle}deg)`;   
    // }
    // if( Math.floor(scrollPosition / anglePerCadr) % 4 === 2)
    // {
    //     sm2.style.transform = `rotate(${-angle}deg)`;   
    // }
    // if( Math.floor(scrollPosition / anglePerCadr) % 4 === 3)
    // {
    //     sm2.style.transform = `rotate(${angle}deg)`;   
    // }

    if( Math.floor(scrollPosition / anglePerCadr) % 4 === 0)
        {
            sm3.style.transform = `rotate(${angle}deg)`;   
        }
        if( Math.floor(scrollPosition / anglePerCadr) % 4 === 1)
        {
            sm3.style.transform = `rotate(${-angle}deg)`;   
        }
        if( Math.floor(scrollPosition / anglePerCadr) % 4 === 2)
        {
            sm3.style.transform = `rotate(${-angle}deg)`;   
        }
        if( Math.floor(scrollPosition / anglePerCadr) % 4 === 3)
        {
            sm3.style.transform = `rotate(${angle}deg)`;   
        }

        // if( Math.floor(scrollPosition / anglePerCadr) % 4 === 0)
        //     {
        //         sm4.style.transform = `rotate(${angle}deg)`;   
        //     }
        //     if( Math.floor(scrollPosition / anglePerCadr) % 4 === 1)
        //     {
        //         sm4.style.transform = `rotate(${-angle}deg)`;   
        //     }
        //     if( Math.floor(scrollPosition / anglePerCadr) % 4 === 2)
        //     {
        //         sm4.style.transform = `rotate(${-angle}deg)`;   
        //     }
        //     if( Math.floor(scrollPosition / anglePerCadr) % 4 === 3)
        //     {
        //         sm4.style.transform = `rotate(${angle}deg)`;   
        //     }



    if( Math.floor(scrollPosition / cadr) % 2 === 0)
    {
        sm1.style.display = 'none';    
    }
    else{
        sm1.style.display = 'block'
    }

    if( Math.floor(scrollPosition / cadr) % 2 === 0)
        {
        sm2.style.display = 'block';
    }
    else{
        sm2.style.display = 'none'
    }
    
    if( Math.floor(scrollPosition / cadr) % 2 === 0)
        {
        sm3.style.display = 'none';
    }
    else{
        sm3.style.display = 'block'
    } 
    
    if( Math.floor(scrollPosition / cadr) % 2 === 0)
        {
        sm4.style.display = 'block';
    }
    else{
        sm4.style.display = 'none'
    }

    // smContainer.forEach(sm => {
    //     const scrollPosition = window.scrollY;
    //     let moveY = scrollPosition * 3; // Коэффициент 0.5 для уменьшения скорости перемещения
    //     while (moveY > this.window.innerHeight - this.getComputedStyle(sm).top.slice(0, -2))
    //     {
    //         //console.log(moveY);
    //         moveY = moveY - this.window.innerHeight - 300;
            
    //     }
    //     if( Math.floor(scrollPosition / 50) % 2 === 0)
    //         {
    //         sm.style.visibility = 'hidden';
    //     }
    //     else{
    //         sm.style.visibility = 'visible'
    //     }
    // });
    
});