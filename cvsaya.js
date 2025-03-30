// Anda bisa menambahkan JavaScript jika diperlukan untuk interaktivitas tambahan
// Contoh: Menambahkan efek hover pada list items
document.querySelectorAll("ul li").forEach((item) => {
  item.addEventListener("mouseover", () => {
    item.style.backgroundColor = "#77aaff";
    item.style.color = "#fff";
  });
  item.addEventListener("mouseout", () => {
    item.style.backgroundColor = "#e4e4e4";
    item.style.color = "#333";
  });
});
