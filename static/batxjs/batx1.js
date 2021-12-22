const Sesentanueve = [{
        img: 'static/Persones/1_DAVID CORTE CRUZ/rostro_0.jpg',
        desc: ' DAVID CORTE CRUZ '
    }]

    let Ochentaocho = document.querySelector('#persones1')

    function dinamico(src, desc) {
        let colm = document.createElement("div");
        let img = document.createElement("img");
        img.src = src;
        let a = document.createElement("a");
        a.innerHTML = desc;
        colm.appendChild(img);
        colm.appendChild(a);
        Ochentaocho.appendChild(colm);
    }

    Sesentanueve.forEach(({img, desc}) => dinamico(img, desc));