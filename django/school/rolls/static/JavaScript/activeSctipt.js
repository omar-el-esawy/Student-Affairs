function onCbChange(cb) {
    var b = document.getElementById(cb).checked;

    var Confirm = confirm('Are you sure to change it?');
    if (Confirm == true) {
        if (b) {
            alert('Action Succesfully');
            document.getElementById(cb).checked = true;
        }
        else {
            document.getElementById(cb).checked = false;
        }
    }
    else {
        alert('Action cancelled');
        document.getElementById(cb).checked = !b;
    }
}
function submit() {
    alert('Submitted Successfully');
}