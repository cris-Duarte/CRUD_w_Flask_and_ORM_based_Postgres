var form1 = function() {
    const request = new XMLHttpRequest();
    const data = new FormData();
    data.append('nombre', document.getElementById('fnombre').value);
    data.append('apellido', document.getElementById('fapellido').value);
    data.append('ci', document.getElementById('fci').value);
    data.append('email', document.getElementById('femail').value);
    data.append('con', document.getElementById('fc').value);

    let e = document.getElementById('ftipo');

    data.append('tipo', e.options[e.selectedIndex].value);
    data.append('alta',true);

    request.open('POST', '/');

    request.onload = () => {
      document.getElementById('mensaje').innerHTML = request.response;
    };
    request.send(data);

    return false;

};
var eliminar = function(id) {
  const request = new XMLHttpRequest();
  const data = new FormData();
  data.append('baja', true);
  data.append('id',id);
  request.open('POST', '/');

  request.onload = () => {
    document.getElementById('mensaje').innerHTML = request.response;
  };
  request.send(data);

  return false;

};
