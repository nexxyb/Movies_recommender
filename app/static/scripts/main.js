let getMovie = ()=>{
    search = document.getElementById("search").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("search_result").innerHTML= xhttp.responseText;
        }
    };
    xhttp.open("GET", "getmovie?search"+"="+search, true);
    xhttp.send;
}