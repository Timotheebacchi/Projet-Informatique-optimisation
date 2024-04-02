function redirectUser() {
    var password = document.getElementById('motdepasse').value;

    if (password == "7LcN8R3k84qceJ") {
        window.location.href = 'Teacher.html';
    } else {
        alert("Il y une erreur sur le mot de passe")
    }
}