function validateForm(){
    var name = document.getElementById("name").value;

    if(name == ""){
        alert("Name required");
        return false;
    }

    return true;
}