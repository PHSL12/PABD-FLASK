function validateYear() {
    var year = document.getElementById("year").value;
    if (isNaN(year)) {
        alert("O ano deve ser um número.");
        return false;
    }
    return true;}