function redirectUser() {
    var surname = document.getElementById('nom').value;
    var firstname = document.getElementById('prenom').value;

    if ((surname == "Roy")&&(firstname == "Valerie")) {
        window.location.href = 'Pass.html';
    } else {
        window.location.href = 'Choice_Page.html';
    }
}