
function onlyNumberKey(evt) {
    // Only ASCII character in that range allowed
    var ASCIICode = (evt.which) ? evt.which : evt.keyCode
    if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57) && ASCIICode !== 46) {
        alert("You must enter numbers!");
        return false;
    }
    return true;
}

function Mes() {
    confirm("Are you sure you want to edit the studetn's data?");
}
function DelMes() {
    confirm("Are you sure you want to delete this student's data?");
}
window.onload = function () {
    document.getElementById("myBtn").addEventListener("click", Mes);
    document.getElementById("backBtn").addEventListener("click", DelMes);

}