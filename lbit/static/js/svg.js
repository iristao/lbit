var pic = document.getElementById("pic");
var pic2 = document.getElementById("pic2");
var workButt = document.getElementById("working");
var stopButt = document.getElementById("stopped");
var brokeButt = document.getElementById("broken");
var down_stat = document.getElementById("down_stat");
var up_stat = document.getElementById("up_stat");

var b1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var b2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var b3 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var b4 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var esc = document.createElementNS("http://www.w3.org/2000/svg", "path");

var up_status = up_stat.innerHTML;
var down_status = down_stat.innerHTML;

b1.setAttribute("x1", 10); 
b1.setAttribute("y1", 10); 
b1.setAttribute("x2", 390); 
b1.setAttribute("y2", 10);
b1.setAttribute("stroke", "black");
b1.setAttribute("stroke-width", 20);
b1.setAttribute("stroke-linecap", "round");
pic.appendChild(b1); 


b2.setAttribute("x1", 390); 
b2.setAttribute("y1", 10); 
b2.setAttribute("x2", 390); 
b2.setAttribute("y2", 390);
b2.setAttribute("stroke", "black");
b2.setAttribute("stroke-width", 20);
b2.setAttribute("stroke-linecap", "round");
pic.appendChild(b2); 


b3.setAttribute("x1", 390); 
b3.setAttribute("y1", 390); 
b3.setAttribute("x2", 10); 
b3.setAttribute("y2", 390);
b3.setAttribute("stroke", "black");
b3.setAttribute("stroke-width", 20);
b3.setAttribute("stroke-linecap", "round");
pic.appendChild(b3); 


b4.setAttribute("x1", 10); 
b4.setAttribute("y1", 390); 
b4.setAttribute("x2", 10); 
b4.setAttribute("y2", 10);
b4.setAttribute("stroke", "black");
b4.setAttribute("stroke-width", 20);
b4.setAttribute("stroke-linecap", "round");
pic.appendChild(b4); 


esc.setAttribute("d", "M50 300 C10 300 10 360 50 360 L100 360 L325 200 L350 200 C390 200 390 140 350 140 L300 140 L75 300 Z");
esc.setAttribute("stroke-width", 10);
esc.setAttribute("stroke", "black");
esc.setAttribute("fill", "none");
pic.appendChild(esc);


var c1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var c2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var c3 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var c4 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var esc2 = document.createElementNS("http://www.w3.org/2000/svg", "path");

c1.setAttribute("x1", 10); 
c1.setAttribute("y1", 10); 
c1.setAttribute("x2", 390); 
c1.setAttribute("y2", 10);
c1.setAttribute("stroke", "black");
c1.setAttribute("stroke-width", 20);
c1.setAttribute("stroke-linecap", "round");
pic2.appendChild(c1); 


c2.setAttribute("x1", 390); 
c2.setAttribute("y1", 10); 
c2.setAttribute("x2", 390); 
c2.setAttribute("y2", 390);
c2.setAttribute("stroke", "black");
c2.setAttribute("stroke-width", 20);
c2.setAttribute("stroke-linecap", "round");
pic2.appendChild(c2); 


c3.setAttribute("x1", 390); 
c3.setAttribute("y1", 390); 
c3.setAttribute("x2", 10); 
c3.setAttribute("y2", 390);
c3.setAttribute("stroke", "black");
c3.setAttribute("stroke-width", 20);
c3.setAttribute("stroke-linecap", "round");
pic2.appendChild(c3); 


c4.setAttribute("x1", 10); 
c4.setAttribute("y1", 390); 
c4.setAttribute("x2", 10); 
c4.setAttribute("y2", 10);
c4.setAttribute("stroke", "black");
c4.setAttribute("stroke-width", 20);
c4.setAttribute("stroke-linecap", "round");
pic2.appendChild(c4); 


esc2.setAttribute("d", "M50 300 C10 300 10 360 50 360 L100 360 L325 200 L350 200 C390 200 390 140 350 140 L300 140 L75 300 Z");
esc2.setAttribute("stroke-width", 10);
esc2.setAttribute("stroke", "black");
esc2.setAttribute("fill", "none");
pic2.appendChild(esc2);

var working = function(e){
    esc.setAttribute("fill", "green");
    pic.appendChild(esc);
};

workButt.addEventListener("click", working);

var stopped = function(e){
    esc.setAttribute("fill", "yellow");
    pic.appendChild(esc);
};

stopButt.addEventListener("click", stopped);

var broken = function(e){
    esc.setAttribute("fill", "red");
    pic.appendChild(esc);
};

brokeButt.addEventListener("click", broken);

console.log(up_status);

if(up_status == 0){
    esc.setAttribute("fill", "green");
    pic.appendChild(esc);
}
else if(up_status == 1){
    esc.setAttribute("fill", "yellow");
    pic.appendChild(esc);
}
else{
    esc.setAttribute("fill", "red");
    pic.appendChild(esc);
}

if(down_status == 0){
    esc2.setAttribute("fill", "green");
    pic2.appendChild(esc2);
}
else if(down_status == 1){
    esc2.setAttribute("fill", "yellow");
    pic2.appendChild(esc2);
}
else{
    esc2.setAttribute("fill", "red");
    pic2.appendChild(esc2);
}