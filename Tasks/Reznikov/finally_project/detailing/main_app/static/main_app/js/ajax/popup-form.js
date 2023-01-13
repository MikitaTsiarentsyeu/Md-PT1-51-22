import {close_success} from "../close-success-form.js"

function popupForm(){
    const formId = 'form#popup_form'

    $(formId).on('submit', (e) => {
        e.preventDefault()

        $.ajax({
            url:'/popup/',
            type: 'POST',
            dataType: 'json',
            data: {
                date:   $(formId + ' #id_date').val(),
                name:   $(formId + ' #id_name').val(),
                phone:  $(formId + ' #id_phone').val(),
            },
            success: (data) => {

                if('errors' in data){
                    $(formId + ' input[type="text"], ' + formId + ' textarea').each((index,el) => {
                        $(el).removeClass('is-invalid').addClass('is-valid')
                    })

                    $('form#popup_form .invalid-feedback').each((index, el) => {
                        $(el).remove()
                    })

                    for (let key in data['errors']){

                        if (key == 'date'){
                            $(formId).find('input[type="hidden"][name="' + key + '"]').removeClass('is-valid').addClass('is-invalid')
                            $(formId).find('input[type="hidden"][name="' + key+ '"]').after(() => {
                                return '<div class="invalid-feedback">' + data['errors'][key] + '</div>'
                            })
                        }

                        $(formId).find('input[type="text"][name="' + key + '"]').removeClass('is-valid').addClass('is-invalid')

                        // $(formId).find('input[type="text"][name="' + key+ '"]').after(() => {
                        //     let result = ''
                        //     for(let k in data['errors'][key]){
                        //         result += data['errors'][key][k] + '<br>'
                        //     }
                        //     return '<div class="invalid-feedback"' + result + '</div>'
                        // })
                        $(formId).find('input[type="text"][name="' + key+ '"]').after(() => {
                            return '<div class="invalid-feedback">' + data['errors'][key] + '</div>'
                        })
                    }
                }
                if('success' in data){
                    document.getElementById('select-time').style.display = 'none';
                    document.getElementsByClassName("pressed")[0].className = document.getElementsByClassName("pressed")[0].className.replace(" pressed", "")
                    $('.popup-bg').hide()
                    $('#success-form').fadeIn(800);
                    $("#success-form .success-content").html(data.html_form);
                    close_success()
                }
            }
        })
    });
}

export {popupForm}