const Cientosetentaseis = [{
        img: 'static/Persones/2_POL RUIZ TORRAS/rostro_0.jpg',
        desc: ' POL RUIZ TORRAS '
    }]

    let Sesentados = document.querySelector('#persones2')

    function dinamico(src, desc) {
        let colm = document.createElement("div");
        let img = document.createElement("img");
        img.src = src;
        let a = document.createElement("a");
        a.innerHTML = desc;
        colm.appendChild(img);
        colm.appendChild(a);
        Sesentados.appendChild(colm);
    }

    Cientosetentaseis.forEach(({img, desc}) => dinamico(img, desc));