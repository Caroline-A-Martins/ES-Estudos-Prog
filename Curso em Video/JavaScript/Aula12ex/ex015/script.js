function verificar() {
    var data = new Date();
    var ano = data.getFullYear();
    var fano = document.getElementById('txtano');
    var res = document.querySelector('div#res');

    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente!');
    } else {
        var fsex = document.getElementsByName('radsex');
        var idade = ano - Number(fano.value);
        var genero = '';
        var img = document.createElement('img');
        img.setAttribute('id', 'foto');

        if (fsex[0].checked) {
            genero = 'Homem';
            if (idade >= 0 && idade < 6) {
                // bebe
                img.setAttribute('src', 'img/M/homem-bebe.png');
            } else if (idade < 13) {
                // criança
                img.setAttribute('src', 'img/M/menino-crianca.png');
            } else if (idade < 18) {
                // Adolescente
                img.setAttribute('src', 'img/M/adolescente-homem.png');
            } else if (idade < 25) {
                // jovem
                img.setAttribute('src', 'img/M/jovem-homem.png');
            } else if (idade < 50) {
                // adulto
                img.setAttribute('src', 'img/M/adulto-homem.png');
            } else {
                // idoso
                img.setAttribute('src', 'img/M/idoso-homem.png');
            }

        } else if (fsex[1].checked) {
            genero = 'Mulher';
            if (idade >= 0 && idade < 6) {
                // bebe
                img.setAttribute('src', 'img/F/mulher-bebe.png');
            } else if (idade < 13) {
                // criança
                img.setAttribute('src', 'img/F/mulher-crianca.png');
            } else if (idade < 18) {
                // Adolescente
                img.setAttribute('src', 'img/F/adolescente-mulher.png');
            } else if (idade < 25) {
                // jovem
                img.setAttribute('src', 'img/F/jovem-mulher.png');
            } else if (idade < 50) {
                // adulta
                img.setAttribute('src', 'img/F/adulta-mulher.png');
            } else {
                // idoso
                img.setAttribute('src', 'img/F/idosa-mulher.png');
            }
        }

        res.style.textAlign = 'center';
        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`;
        res.appendChild(img); // Add the image to the 'res' div
    }
}
