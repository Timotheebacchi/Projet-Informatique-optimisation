document.addEventListener("DOMContentLoaded", (event) => {
  let dragged;

  // Événements pour les éléments draggables
  document.querySelectorAll(".draggable").forEach((elem) => {
    elem.addEventListener("dragstart", (e) => {
      dragged = e.target; // l'élément en cours de déplacement
      e.target.style.opacity = 0.5;
    });

    elem.addEventListener("dragend", (e) => {
      e.target.style.opacity = ""; // réinitialise l'opacité
    });
  });

  // Événements pour les cibles de dépôt
  document.querySelectorAll(".droppable").forEach((elem) => {
    elem.addEventListener("dragover", (e) => {
      e.preventDefault(); // permet de déposer
    });

    elem.addEventListener("dragenter", (e) => {
      e.target.classList.add("over"); // style quand un élément est survolé
    });

    elem.addEventListener("dragleave", (e) => {
      e.target.classList.remove("over"); // réinitialise le style
    });

    elem.addEventListener("drop", (e) => {
      e.preventDefault(); // évite l'ouverture du contenu déplaçable
      if (e.target.className.includes("droppable")) {
        e.target.textContent = ""; // retire le texte initial
        e.target.append(dragged); // ajoute l'élément déplacé
      }
    });
  });
});

function send_choice() {
  if (document.getElementById("hole1").childElementCount*document.getElementById("hole2").childElementCount*document.getElementById("hole3").childElementCount*document.getElementById("hole4").childElementCount*document.getElementById("hole5").childElementCount == 0)
    {
      alert("remplissez tout les choix");
      return;
    }
  let choice1 = document.getElementById("hole1").children[0].value;
  let choice2 = document.getElementById("hole2").children[0].value;
  let choice3 = document.getElementById("hole3").children[0].value;
  let choice4 = document.getElementById("hole4").children[0].value;
  let choice5 = document.getElementById("hole5").children[0].value;

  let choices = {1:choice1,2:choice2,3:choice3,4:choice4,5:choice5}

  fetch("/save_choice", {
    method: "POST",
    body: JSON.stringify(choices),
    headers: { "Content-type": "application/json; charset=UTF-8" }
  }).then(response => {
    window.location.href = response.url;
  });
}