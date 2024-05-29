

(() => {
    'use strict'
    
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
    const inputEmail = document.querySelector('#validationCustom02')
    const inputName = document.querySelector('#validationCustom01')
    const toastLiveExample = document.getElementById('liveToast')
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample)
    const mensaje = document.querySelector("#mensajeToast")
    
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
          event.preventDefault()
        if (!form.checkValidity()) {
          event.stopPropagation()
        }
        form.classList.add('was-validated')

        /*const obj={
            Hola:1,
            "Hola-Mundo":1
        }*/

        const formEntries = new FormData(form)
        const formData = Object.fromEntries(formEntries)
        if (!formData["soy-terminos"]) formData["soy-terminos"] = "off"                   
        const keysOfForm = Object.keys(formData)
        const validations = keysOfForm.map((key) => validateInput(key,formData[key],inputEmail,inputName))
        const isValid = validations.every((validation) => validation === true)
        console.log(validations)
        console.log(formData)

        toastBootstrap.show()
        if (isValid){
            mensaje.innerHTML= "Se ha ingresado su solicitud con exito"
        }
        else{
            mensaje.innerHTML= "Formulario no completado correctamente"
        }

      }, false)
    })
  })()


function validateInput(name,value,inputEmail,inputName){
    const regexEmail = /^[^\s@]+@[^\s@]+.[^\s@]+$/;
    let isValid = false;
    switch (name) {
        case "soy-correo":
            isValid = regexEmail.test(value);
            inputEmail.setCustomValidity(isValid?"":"invalidField");
            /*!isValid?inputRef.setCustomValidity("invalidField"):inputRef.setCustomValidity("");*/
            /*if(!isValid){
                inputRef.setCustomValidity("invalidField");
            }
            else{
                inputRef.setCustomValidity("");
            }*/
            return isValid;
            
        case "soy-nombre":
            isValid = (value.length >= 2 && value.length <= 50);
            inputName.setCustomValidity(isValid?"":"invalidField");
            return isValid;

        case "soy-mensaje":
            isValid = (value.length > 0);
            return isValid;

        case "soy-terminos":
            isValid = value==="on";
            return isValid;

           
    }
}


