const videoInput = document.getElementById("video-input");
const videoPreview = document.getElementById("video-preview");

videoInput.addEventListener("change", (event) => {
  const videoFile = event.target.files[0];
  if (videoFile) {
    const videoUrl = URL.createObjectURL(videoFile);

    // Afficher la vidéo directement
    videoPreview.innerHTML = `<video src="${videoUrl}" width="100%" height="100%" muted autoplay loop></video>`;

    // Libérer l'URL pour éviter les fuites mémoire (optionnel si la vidéo reste affichée)
    videoPreview.querySelector("video").addEventListener("ended", () => {
      URL.revokeObjectURL(videoUrl);
    });
  } else {
    videoPreview.innerHTML = "Aucune vidéo sélectionnée.";
  }
});


const imageInput = document.getElementById("image-input");
const imagePreview = document.getElementById("image-preview");

imageInput.addEventListener("change", (event) => {
  const file = event.target.files[0];

  if (file) {
    const imageURL = URL.createObjectURL(file);

    // Mettre à jour le contenu du div pour afficher l'image
    imagePreview.innerHTML = `<img src="${imageURL}" alt="Aperçu image">`;

    // Libérer l'URL après utilisation pour éviter les fuites mémoire
    URL.revokeObjectURL(imageURL);
  } else {
    imagePreview.innerHTML = "Aucun aperçu disponible";
  }
});
