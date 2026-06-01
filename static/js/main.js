(function () {
  const avatarInput = document.getElementById("id_avatar");
  const deleteAvatarBtn = document.getElementById("delete-avatar-btn");
  const avatarPreview = document.getElementById("avatar-preview");
  if (avatarInput) {
    avatarInput.addEventListener("change", function (event) {
      const file = event.target.files[0];
      if (!file) return;
      avatarPreview.src = URL.createObjectURL(file);
      document.getElementById("avatar-deleted").value = "0";
    });
  }

  if (deleteAvatarBtn) {
    deleteAvatarBtn.addEventListener("click", function () {
      if (avatarPreview.dataset.hasAvatar !== "true") {
        return;
      }

      avatarPreview.src = avatarPreview.dataset.defaultAvatar;
      avatarPreview.dataset.hasAvatar = "false";
      document.getElementById("avatar-deleted").value = "1";
      avatarInput.value = "";
    });
  }
})();
