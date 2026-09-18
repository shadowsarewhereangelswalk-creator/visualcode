document.querySelectorAll(".controls").forEach((controls) => {
  const media = document.getElementById(controls.dataset.for);
  const toggle = controls.querySelector('[data-action="toggle"]');
  const mute = controls.querySelector('[data-action="mute"]');
  const volume = controls.querySelector('[data-action="volume"]');

  toggle.addEventListener("click", async () => {
    if (media.paused) {
      try {
        await media.play();
      } catch (error) {
        console.error("No se pudo iniciar la reproducción:", error);
      }
    } else {
      media.pause();
    }
  });

  mute.addEventListener("click", () => {
    media.muted = !media.muted;
    mute.textContent = media.muted ? "Activar sonido" : "Silenciar";
  });

  volume.addEventListener("input", () => {
    media.volume = Number(volume.value);
    media.muted = false;
    mute.textContent = "Silenciar";
  });
});
