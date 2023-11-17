function carregar() {
    var msg = window.document.getElementById('msg');
    var img = window.document.getElementById('imagem');
    var data = new Date();
    var hora = data.getHours();
    //var hora = 23; // Use this line for testing
    msg.innerHTML = `Agora são ${hora} horas.`;
    if (hora >= 0 && hora < 12) {
        // BOM DIA
        img.src = 'img/Dia.png';
        document.body.style.background = '#F2DC99'
    } else if (hora >= 12 && hora < 18) {
        // BOA TARDE
        img.src = 'img/Tarde.png';
        document.body.style.background = '#874735'

    } else {
        // BOA NOITE
        img.src = 'img/Noite.png';
        document.body.style.background = '#314F53'
    }
}
