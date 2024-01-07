document.addEventListener('DOMContentLoaded', function() {
    //capturamos las citas desde el contexto
    const citas = JSON.parse(document.getElementById('citas').textContent);
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const eventos = citas.map(cita => ({
       
        title: cita.description,
        start: new Date(cita.dates_date),
        timeStart: moment(cita.hour_date, 'HH:mm:ss').format('hh:mm A'),
        id: cita.id,
        medic: cita.medic,
        patient: cita.patient,
        status: cita.status,
    }));

    console.log(eventos);
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        //zona horaria
        timeZone: 'America/Caracas',
        locale: 'es',
        selectable: true,
        headerToolbar: {
            left: 'prev,next',
            center: 'title',
            right: 'dayGridMonth, timeGridWeek, timeGridDay',
        },
        events: eventos,


        buttonText: {
            month: 'Mes',
            week: 'Semana',
            day: 'Dia',
            prev: '<',
            next: '>',
        },
        slotMinTime: '08:00:00',
        slotMaxTime: '18:00:00',
        dateClick: function(info) {
            // Utiliza una función anónima para pasar la fecha a abrirModal
            
            var selectedDate = info.dateStr;
            abrirModal(selectedDate);
        },
    });

    function abrirModal(selectedDate) {
        $("#citaModal").modal('show');
        // Muestra la fecha seleccionada en el cuerpo del modal
        

        $("#guardarCitaBtn").on('click', function() {
            var paciente = $("#pacienteSelect").val();
            var doctor = $("#doctorSelect").val();
            var description = $("#description").val();
            var hora_cita = $("#horaCita").val();
            
            // Formatea la fecha y hora en un formato adecuado para Django
            var formattedDate = moment(selectedDate).format('YYYY-MM-DDTHH:mm:ss');
            
            fetch('/citas/create_date/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrfToken
                },
                body: new URLSearchParams({
                    'paciente': paciente,
                    'doctor': doctor,
                    'description': description,
                    'dates_date': formattedDate,
                    'hora_cita': hora_cita
                }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    $("#citaModal").modal('hide');
                    // Mensaje de éxito para SweetAlert
                    Swal.fire({
                        "title": "Cita Agendada",
                        "text": data.message,
                        "icon": "success",
                    });
                    calendar.addEventSource(citas);
                    // Limpia los campos del formulario
                    $("#pacienteSelect").val('').trigger('change');
                    $("#doctorSelect").val('').trigger('change');
                    $("#description").val('');
                    $("#horaCita").val('');

                    // esperamos 5 segundos antes de redireccionar
                    setTimeout(() => {

                        // redirecionar a la vista de index
                        window.location.href = '/';
                    }, 5000);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }

    $('#horaCita').timepicker({
        timeFormat: 'H:i',
        interval: 60,
        minTime: '8:00am',
        maxTime: '6:00pm',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });

    calendar.render();
});
