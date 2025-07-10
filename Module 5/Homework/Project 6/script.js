function myFunction() {
    document.getElementById("result").innerHTML = 
    document.getElementById("demo").firstChild.nodeValue;
    document.getElementById("result").innerHTML = 
    document.getElementById("demo").childNodes[0].nodeValue;
}