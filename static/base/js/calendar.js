document.addEventListener('DOMContentLoaded', function() {
    //capturamos las citas desde el contexto
    const citas = JSON.parse(document.getElementById('citas').textContent);
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const eventos = citas 
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        //zona horaria
        
        timeZone: 'America/Caracas',
        locale: 'es',
        selectable: true,
        headerToolbar: {
            left: 'prev,next',
            center: 'title',
            right: 'dayGridMonth, timeGridWeek, listDay',
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

       
        buttonText: {
            month: 'Mes',
            week: 'Semana',
            day: 'Dia',
            prev: '<',
            next: '>',
        },
        /* slotMinTime: '08:00:00',
        slotMaxTime: '18:00:00', */
        dateClick: function(info) {            
            let selectedDate = info.dateStr;
            abrirModal(selectedDate);
        },


        
    });
    
    
    function abrirModal(selectedDate) {
        $("#citaModal").modal('show');
        // asiganmos la fecha seleccionada al input de fecha
        $("#dates_date").val(selectedDate);
       
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

 

    calendar.render();
});


