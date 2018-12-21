var theList = document.getElementById('thelist').children;
var header = document.getElementById('h');
var fibind = 1;




var elemfxn = (e) =>{
    e.addEventListener("mouseover", function () {
      header.innerHTML = e.innerHTML;
    });

    e.addEventListener("mouseout", function(){
      header.innerHTML = "Hello World!"
    });

    e.addEventListener("click" , function(){
      e.remove();
    });
}

document.getElementById('b').addEventListener("click" , function(){
     var element = document.createElement("LI");
     var text = document.createTextNode("Blah");
     element.appendChild(text);
     elemfxn(element);
     document.getElementById("thelist").appendChild(element);
})


for(var i =0; i < theList.length; i++){
  let e = theList[i];
  elemfxn(e);
}

document.getElementById("fb").addEventListener("click", function(){
    var element = document.createElement("LI");
    var text = document.createTextNode(fibonacci(fibind));
    element.appendChild(text);
    document.getElementById("fiblist").appendChild(element);
    fibind++;
})


var fibonacci = (n) => {
    var first = 0;
    var second = 1;
    for (i = 0; i < n; i++) {
      	var temp = second;
      	second += first;
      	first = temp;
    }
    return first;
}
