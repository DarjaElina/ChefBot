const theme = localStorage.theme;

const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

document.documentElement.classList.toggle(
  "dark",
  theme === "dark" || (!("theme" in localStorage) && prefersDark),
);

// 1) Get saved theme from localStorage

// 2) Check if the user’s system prefers dark mode

// 3 Toggle the 'dark' class on the <html> element
// - If user has set theme to 'dark'
// - Or if there is no user-set theme and system prefers dark
