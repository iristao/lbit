var pic = document.getElementById("pic");
var workButt = document.getElementById("working");
var stopButt = document.getElementById("stopped");
var brokeButt = document.getElementById("broken");

var b1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var b2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var b3 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var b4 = document.createElementNS("http://www.w3.org/2000/svg", "line");
var esc = document.createElementNS("http://www.w3.org/2000/svg", "path");



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