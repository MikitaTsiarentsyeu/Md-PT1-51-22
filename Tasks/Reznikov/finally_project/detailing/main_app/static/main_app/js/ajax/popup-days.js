function popup_days(){
  var popupContainer = document.getElementById("day-name");
  var divs = popupContainer.getElementsByClassName("popup-day");

  let monthNames = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
  const formId = 'form#popup_form'

  for (var i = 0; i < divs.length; i++) {
      divs[i].addEventListener("click", function() {
      var current = document.getElementsByClassName("pressed");
      if (current.length != 0){
          current[0].className = current[0].className.replace(" pressed", "");
      }
      this.className += " pressed";

      var month_name = document.getElementById("calendar-month");
      let nowYear = new Date().getFullYear(),
          chosenMonth = monthNames.findIndex(i => i == month_name.textContent.trim()),
          strDate = nowYear + '-' + addZeroBefore(chosenMonth+1) + '-' + this.textContent.substring(3)
      
      // console.log(strDate)
      $(formId).find('input[type="hidden"][name="date"]').val(strDate)

      document.getElementById('select-time').style.display = 'block';


      $.ajax({                       
          type: "POST",
          url: '/popup_get/',
          data: {
              'date': strDate,       
              'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function (data) {   
              
              let time_data = ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00']
              let html_data = document.getElementById('select-time').getElementsByClassName('option-time')
              html_data.innerHTML = '<option class="option-time" value="">Выберите время</option>'
              for(var i=0; i<time_data.length;i++){
                html_data.innerHTML += '<option class="option-time" value="'+ time_data[i] + '">'+ time_data[i] +'</option>'
              }
              $("#select-time").html(html_data.innerHTML);

              var new_html_data = document.getElementById("select-time").getElementsByClassName("option-time");
              data['success'].forEach(function (data) {
                let unpack_date = new Date(data);
                let unpack_hours = addZeroBefore(unpack_date.getHours()) + ':' + addZeroBefore(unpack_date.getMinutes());  
                

                for (var i = 0; i < new_html_data.length; i++) {
                  if (unpack_hours == new_html_data[i].value){
                    new_html_data[i].setAttribute('disabled', true);
                  }
                  // new_html_data[i].addEventListener("click", function() {
                  //   var current = document.getElementsByClassName("pressed");
                  //   if (current.length != 0){
                  //       current[0].className = current[0].className.replace(" pressed", "");
                  //   }
                  // })
                }
                  // html_data.innerHTML += `<option value="">${data}</option>`
              });

              
          }
      });
    });
  }

  $('#select-time').change(function(){
      let get_time = $('form#popup_form').find('input[type="hidden"][name="date"]').val().substr(0,10)
      $(formId).find('input[type="hidden"][name="date"]').val(get_time + ' ' + $(this).val())
  })
}

function addZeroBefore(n) {
  return (n < 10 ? '0' : '') + n;
}

export {popup_days}