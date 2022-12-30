
console.log('hola fede')
// Obtiene los valores de los campos de inicio de sesión

const username = document.getElementById('username').value;
const password = document.getElementById('password').value;

// Envía la solicitud POST al servidor

fetch('/ingreso_usuario', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    username,
    password
  })
})
  .then(response => {
    // Si la solicitud fue exitosa, redirige al usuario a la página principal
    if (response.status === 200) {
      window.location.replace('/');
    } else {
      // Si la solicitud no fue exitosa, muestra un mensaje de error al usuario
      alert('Nombre de usuario o contraseña incorrectos');
    }
  })
  .catch(error => {
    console.error(error);
  });