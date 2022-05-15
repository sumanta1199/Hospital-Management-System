function getRandomColor() {
    latters = '0123456789ABCDEF'
    color = '#'
    for (var i = 0; i < 6; i++) {
        r = Math.floor(Math.random(0, 1) * 16)
        color = color + latters[r]
    }
    return color
}

var h1=document.querySelector('h1')

function changeColor() {
    h1.style.color= getRandomColor()
}
setInterval(changeColor, 500)