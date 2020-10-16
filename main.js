var mousePosition;
var offset = [0,0];
var div;
var isDown = false;
var ponztszam =0;
var click = 0

div = document.createElement("div");
div.style.position = "absolute";
div.style.left = "0px";
div.style.top = "0px";
div.style.width = "100px";
div.style.height = "100px";
div.style.background = "red";
div.style.color = "blue";

document.body.appendChild(div);


div.addEventListener("click",function(e){    
 //alert(e.target+" clicked"); 
 ponztszam++;
 document.getElementById("pontszam").innerHTML=ponztszam;

});

div.addEventListener('mousedown', function(e) {
    isDown = true;
    offset = [
        div.offsetLeft - e.clientX,
        div.offsetTop - e.clientY
    ];
}, true);

document.addEventListener('mouseup', function() {
    isDown = false;
    click++;
    document.getElementById("click").innerHTML=click;
}, true);

document.addEventListener('mousemove', function(event) {
    event.preventDefault();
    if (isDown) {
        mousePosition = {
            x : event.clientX,
            y : event.clientY
        };
      //  div.style.left = (mousePosition.x + offset[0]) + 'px';
      //  div.style.top  = (mousePosition.y + offset[1]) + 'px';
    }

}, true);

var h = setInterval(function () {
        div.style.top = Math.floor((Math.random() * 400) + 1)+"px"; //Math.floor((Math.random() * 100) + 1);  Generates random number between 1 and 100
        div.style.left = Math.floor((Math.random() * 400) + 1)+"px"; //Math.floor((Math.random() * 200) + 1);  Generates random number between 1 and 200
//console.log('top = '+div_elem.style.top);
//console.log('left = '+div_elem.style.left); 
}, 1000)
