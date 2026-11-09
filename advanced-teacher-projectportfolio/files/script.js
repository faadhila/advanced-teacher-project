// 1. Dark mode toggle
const toggleBtn = document.getElementById("theme-toggle");
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  toggleBtn.textContent = document.body.classList.contains("dark") ? "Light" : "Dark";
});

// 2. Filter projects by category
const filterButtons = document.querySelectorAll(".filter");
const cards = document.querySelectorAll(".card");

filterButtons.forEach((button) => {
  button.addEventListener("click", () => {
    filterButtons.forEach((b) => b.classList.remove("active"));
    button.classList.add("active");

    const category = button.dataset.filter;
    cards.forEach((card) => {
      const match = category === "all" || card.dataset.category === category;
      card.style.display = match ? "block" : "none";
    });
  });
});

// 3. Reveal sections when scrolled into view
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) entry.target.classList.add("show");
    });
  },
  { threshold: 0.15 },
);

document.querySelectorAll(".reveal").forEach((section) => observer.observe(section));
