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