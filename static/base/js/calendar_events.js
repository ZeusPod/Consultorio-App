document.addEventListener('DOMContentLoaded', function() {

    const citas = JSON.parse(document.getElementById('citas').textContent);
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    let selectedDate; 
    const eventos = citas 
    var CalendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(CalendarEl, {
        timeZone: 'America/Caracas',
        locale: 'es',
        initialView : 'dayGridMonth',
        selectable: true,
        headerToolbar: {
            left: 'prev,next',
            center: 'title',
            right: 'dayGridMonth, timeGridWeek, listDay',
        },
        buttonText: {
            month: 'Mes',
            week: 'Semana',
            day: 'Dia',
            prev: '<',
            next: '>',
        },
        

        dateClick: function(info) {
            selectedDate = info.dateStr;
            abrirModal(selectedDate);
            
        }, 

        events: function(info, successCallback, failureCallback) {
            let events = eventos.map(evento => ({
                title: evento.description,
                start: new Date(evento.dates_date),
                timeStart: moment(evento.hour_date, 'HH:mm:ss').format('hh:mm A'),
                id: evento.id,
                medic: evento.medic,
                patient: evento.patient,
                status: evento.status,
            }))
            successCallback(events);
        },

        eventContent: function(info) {
            return{
                html:`
                    <div style="overflow:hidden; font-size: 12px; position: relative; cursor: pointer">
                    <strong>${info.event.title}</strong>
                    <div>Fecha : ${info.event._instance.range.start.toLocaleDateString(
                        'es-ES',
                        {
                            month: "long",
                            day: "numeric",
                            year: "numeric",
                        }
                    )}</div>
                    <div>Hora:${info.event.extendedProps.timeStart}</div>
                    </div>
                    `
            }
        },

        eventMouseEnter: function(mouseEnterInfo) {
            let el = mouseEnterInfo.el;
            el.classList.add("relative");

            let newEl = document.createElement("div");
            let newElTitle = mouseEnterInfo.event.title;
            let newElHour = mouseEnterInfo.event.extendedProps.timeStart;
            newEl.innerHTML = `
                <div
                    class="fc-hoverable-event"
                    style="position: absolute; bottom: 100%; left: 0; width: 300px; height: auto; background-color: #4A6FDC; color:white; 
                    z-index: 50; border: 1px solid #e2e8f0; border-radius: 0.375rem; padding: 0.75rem; font-size: 14px; 
                    font-family: 'Inter', sans-serif; cursor: pointer;"
                >
                    <strong>${newElTitle}</strong>
                    <div>Hora:${newElHour}</div>
                   

                </div>
            `
            el.after(newEl)
        
        },

        eventMouseLeave: function() {
            document.querySelector(".fc-hoverable-event").remove()
        },
        
    });

    calendar.render(); 

    $('#citaModal').on('hidden.bs.modal', function() {
        limpiarSeleccionesModal();
    });

    function abrirModal(params) {
        $("#citaModal").modal('show');

        $("#guardarCitaBtn").on('click', function() {
            var paciente = $("#pacienteSelect").val();
            var doctor = $("#doctorSelect").val();
            var description = $("#description").val();
            var hora_cita = $("#horaCita").val();
            
            // Formatea la fecha y hora en un formato adecuado para Django
            var formattedDate = moment(selectedDate).format('YYYY-MM-DDTHH:mm:ss');
            
            console.log(paciente, doctor, description, formattedDate, hora_cita);
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
                    }, 2000);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    };

    function limpiarSeleccionesModal() {
        $("#pacienteSelect").val('');
        $("#doctorSelect").val('');
        $("#description").val('');
        $("#horaCita").val('');
    };

    $('#horaCita').timepicker({
        timeFormat: 'H:i',
        interval: 60,
        minTime: '8:00am',
        maxTime: '6:00pm',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });



})