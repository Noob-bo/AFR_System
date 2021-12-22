const Cientonoventaisete = [{
        img: 'static/Persones/3_PAU PALMERO ARANS/rostro_0.jpg',
        desc: ' PAU PALMERO ARANS '
    }]

    let Cincuentatres = document.querySelector('#persones3')

    function dinamico(src, desc) {
        let colm = document.createElement("div");
        let img = document.createElement("img");
        img.src = src;
        let a = document.createElement("a");
        a.innerHTML = desc;
        colm.appendChild(img);
        colm.appendChild(a);
        Cincuentatres.appendChild(colm);
    }

    Cientonoventaisete.forEach(({img, desc}) => dinamico(img, desc));