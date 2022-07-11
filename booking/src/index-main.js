import datepicker from 'js-datepicker'

document.getElementById("id_fecha").setAttribute("readonly", "true");

var opt = document.createElement('option');
opt.innerHTML = "---- Elije el Horario ----";
opt.setAttribute("selected", "selected");
opt.setAttribute("disabled", "disabled");
opt.value = "";
id_horario.appendChild(opt);

var valuefecha="";
const picker = datepicker('#id_fecha', {
    position: 'c', // Top right.
    alwaysShow: true,
    minDate: new Date(),
    startDay: 1,
    customDays: ['D', 'L', 'M', 'M', 'J', 'V', 'S'],
    customMonths: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    formatter: (input, date, instance) => {
        const dd = date.getDate();
        const mm = date.getMonth() + 1;
        const yyyy = date.getFullYear();
        input.value = dd + '/' + mm + '/' + yyyy;
      },
    events: fechas,
    disabledDates: [
        new Date(2022,5,23), 
        new Date(2022,5,22)
    ], // Specific disabled dates.
    onSelect: instance => {
        valuefecha = id_fecha.value
        let str = id_horario.value.replace(/\s/g, '');
        str = str.split("-");     
        id_fecha.value = valuefecha + " " + str[0];    
      },
});

id_horario.addEventListener("change", function() {
    let str = id_horario.value.replace(/\s/g, '');
    str = str.split("-");
    id_fecha.value = valuefecha + " " + str[0];
});


// console.log(id_horario.childNodes);


// console.log(a);

// id_horario.option.forEach(element => {
//     console.log(element);
// });

// id_horario.forEach(element => {
//     console.log(element);
// });

