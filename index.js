// JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    console.log("working")
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                console.log("working")
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                    const error_messages = Array.from(document.querySelectorAll('.invalid-input'))
                    error_messages.forEach((error_message) => {
                        error_message.hidden = false;
                    });

                }

                form.classList.add('was-validated')
            }, false)
        })

})()

