import "js-datepicker/dist/datepicker.min.css";
import datepicker from 'js-datepicker'

document.getElementById("id_fecha").setAttribute("readonly", "true");

var opt = document.createElement('option');
opt.innerHTML = "---- Elije el Horario ----";
opt.setAttribute("selected", "selected");
opt.setAttribute("disabled", "disabled");
opt.value = "";
id_horario.appendChild(opt);
var valuefecha = "";

const picker = datepicker('#id_fecha', {
  position: 'tr', 
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
  if (id_fecha.value.length>10) { 
    let fecha = id_fecha.value.split(" ");
    id_fecha.value = fecha[0] + " " + str[0];
  } else {
    id_fecha.value = id_fecha.value + " " + str[0];
  }

});

