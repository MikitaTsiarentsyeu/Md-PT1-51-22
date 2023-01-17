function calendar(){
    let nowDate = new Date(),
        nowDateNumber = nowDate.getDate(),
        nowMonth = nowDate.getMonth(),
        nowYear = nowDate.getFullYear(),
        container = document.getElementById('popup-calendar'),
        appendContainer = document.getElementById('day-name'),
        monthContainer = document.getElementById('calendar-month'),
        daysContainer = '',
        // prev = container.getElementsByClassName('prev')[0],
        // next = container.getElementsByClassName('next')[0],
        monthName = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
        Days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun'];


    let curDate = nowDate.setMonth(nowDate.getMonth());

    let current_monthName = monthName[nowDate.getMonth()]

    function setMonthCalendar(year,month, nowDateNumber) {
        let monthDays = new Date(year, month + 1, 0).getDate(),
            monthPrefix = new Date(year, month, 0).getDay(),
            monthDaysText = '';

        for (let i = nowDateNumber; i < monthDays; i++){
            var dayPrefix = new Date(year, month, i).getDay()
            var numberday = i+1
            monthDaysText += '<div class="popup-day">' + '<li>' + '<p class="popup-day-week-name">' + Days[dayPrefix] + '</p>' + '<p class="popup-day-number">' + numberday + '</p>' + '</li>' + '</div>';
        }

        daysContainer = monthDaysText;
        appendContainer.innerHTML += daysContainer;

        monthContainer.innerHTML += '<p class="month-name">' + monthName[month] + '</p>'
        // if (month == nowMonth && year == nowYear){
        //     days = daysContainer.getElementsByTagName('li');
        //     days[monthPrefix + nowDateNumber - 1].classList.add('date-now');
        // }
    }

    setMonthCalendar(nowYear,nowMonth, nowDateNumber-1);
}

export {calendar}

// prev.onclick = function () {
//     let curDate = new Date(yearContainer.textContent,monthName.indexOf(monthContainer.textContent));

//     curDate.setMonth(curDate.getMonth() - 1);

//     let curYear = curDate.getFullYear(),
//         curMonth = curDate.getMonth();

//     setMonthCalendar(curYear,curMonth);
// }

// next.onclick = function () {
//     let curDate = new Date(yearContainer.textContent,monthName.indexOf(monthContainer.textContent));

//     curDate.setMonth(curDate.getMonth() + 1);

//     let curYear = curDate.getFullYear(),
//         curMonth = curDate.getMonth();

//     setMonthCalendar(curYear,curMonth);
// }








// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler

// let nowDate = new Date(),
//     nowDateNumber = nowDate.getDate(),
//     nowMonth = nowDate.getMonth(),
//     nowYear = nowDate.getFullYear(),
//     monthName = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь'];



// let curDate = nowDate.setMonth(nowDate.getMonth());
// console.log(nowDate.getFullYear());

// let current_monthName = monthName[nowDate.getMonth()]

// year = 2023;
// month = 0;
// let monthDays = new Date(year, month + 1, 0).getDate(),
//     dayPrefix = new Date(year, month, 0).getDay(),
//     monthDaysText = '';

// Days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ','ВС'];
// console.log(monthDays);
// console.log(dayPrefix);
// console.log(Days[dayPrefix]);

// for (let i = 0; i < monthDays; i++){
//     dayPrefix = new Date(year, month, i).getDay()
//     console.log(i+1 + '-' + Days[dayPrefix]);
// }
