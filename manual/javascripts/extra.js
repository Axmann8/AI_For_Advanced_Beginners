/* The Massive AI Manual · progress tracking, ELI5 mode, and a little confetti 🎉
   Everything is stored in this browser only (localStorage), and the page works fine without it. */
(() => {
  const KEY_DONE = "aiab:done:v1";
  const KEY_LAST = "aiab:last:v1";
  const KEY_ELI5 = "aiab:eli5mode:v1";

  const read = (key, fallback) => {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) {
      return fallback;
    }
  };
  const write = (key, value) => {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {
      /* private window or storage blocked: progress just isn't saved */
    }
  };

  const siteRoot = () => {
    const logo = document.querySelector("a.md-logo");
    return logo ? new URL(logo.getAttribute("href"), location.href) : new URL("/", location.href);
  };
  const keyFor = (rel) => new URL(rel, siteRoot()).pathname;
  const cleanTitle = (text) => (text || "").replace(/¶\s*$/, "").trim();

  function confetti() {
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const colors = ["#7c3aed", "#f59e0b", "#10b981", "#ec4899", "#0ea5e9", "#facc15"];
    for (let i = 0; i < 90; i++) {
      const piece = document.createElement("span");
      piece.className = "confetti-piece";
      piece.style.left = Math.random() * 100 + "vw";
      piece.style.background = colors[i % colors.length];
      piece.style.setProperty("--dx", Math.random() * 220 - 110 + "px");
      piece.style.setProperty("--rot", Math.random() * 900 - 450 + "deg");
      piece.style.animationDuration = 1.6 + Math.random() * 1.5 + "s";
      piece.style.animationDelay = Math.random() * 0.3 + "s";
      document.body.appendChild(piece);
      setTimeout(() => piece.remove(), 3800);
    }
  }

  function markNav(done) {
    document.querySelectorAll(".md-nav__link[href]").forEach((a) => {
      const path = new URL(a.getAttribute("href"), location.href).pathname;
      a.classList.toggle("is-done", Boolean(done[path]));
    });
  }

  function setupDoneButtons() {
    document.querySelectorAll(".chapter-done").forEach((box) => {
      const key = keyFor(box.dataset.chapter);
      const button = box.querySelector("button");
      const render = () => {
        const isDone = Boolean(read(KEY_DONE, {})[key]);
        box.classList.toggle("is-done", isDone);
        button.textContent = isDone ? "🎉 Chapter complete! (click to undo)" : "✅ Mark this chapter as done";
      };
      button.addEventListener("click", () => {
        const done = read(KEY_DONE, {});
        if (done[key]) delete done[key];
        else {
          done[key] = Date.now();
          confetti();
        }
        write(KEY_DONE, done);
        render();
        markNav(done);
      });
      render();
      const heading = document.querySelector(".md-content h1");
      write(KEY_LAST, { path: key, title: cleanTitle(heading && heading.textContent) || document.title });
    });
  }

  function setupProgress() {
    document.querySelectorAll(".progress-tracker").forEach((el) => {
      const total = parseInt(el.dataset.total || "0", 10);
      const count = Object.keys(read(KEY_DONE, {})).length;
      const pct = total ? Math.min(100, Math.round((count / total) * 100)) : 0;
      const last = read(KEY_LAST, null);
      el.innerHTML = "";
      const headline = document.createElement("p");
      headline.innerHTML = count
        ? `<strong>🏆 Your progress:</strong> ${count} of ${total} chapters done (${pct}%). Keep going, you're doing great!`
        : `<strong>🌱 Your progress:</strong> 0 of ${total} chapters. Tap ✅ at the end of any chapter to start your streak!`;
      const bar = document.createElement("div");
      bar.className = "bar";
      bar.appendChild(document.createElement("span"));
      el.append(headline, bar);
      if (last && last.path) {
        const resume = document.createElement("p");
        const link = document.createElement("a");
        link.href = last.path;
        link.textContent = last.title;
        resume.append("📖 Continue where you left off: ", link);
        el.append(resume);
      }
      requestAnimationFrame(() => {
        bar.firstChild.style.width = pct + "%";
      });
    });
  }

  function setupEli5Toggle() {
    document.querySelectorAll(".eli5-toggle").forEach((b) => b.remove());
    const boxes = document.querySelectorAll(".md-content details.eli5");
    if (!boxes.length) return;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "eli5-toggle";
    const apply = (on) => {
      button.setAttribute("aria-pressed", String(on));
      button.innerHTML = on ? '🧸<span class="label"> ELI5 mode: ON</span>' : '🧸<span class="label"> ELI5 mode</span>';
      button.title = on ? "Collapse the ELI5 explanations" : "Open every ELI5 explanation on this page";
      if (on) boxes.forEach((d) => d.setAttribute("open", ""));
    };
    button.addEventListener("click", () => {
      const on = !read(KEY_ELI5, false);
      write(KEY_ELI5, on);
      if (!on) boxes.forEach((d, i) => { if (i > 0) d.removeAttribute("open"); });
      apply(on);
    });
    apply(Boolean(read(KEY_ELI5, false)));
    document.body.appendChild(button);
  }

  // a bright "📄 PDF book" button in the header, on every page
  function setupPdfButton() {
    const header = document.querySelector(".md-header__inner");
    if (!header || header.querySelector(".aiab-pdf-btn")) return;
    const link = document.createElement("a");
    link.className = "aiab-pdf-btn";
    link.href = new URL("download/", siteRoot()).href;
    link.title = "Download the whole manual as a printable PDF book";
    link.innerHTML = '📄<span class="aiab-pdf-btn__label"> PDF book</span>';
    const search = header.querySelector(".md-search");
    header.insertBefore(link, search || null);
  }

  function setup() {
    setupPdfButton();
    setupDoneButtons();
    setupProgress();
    setupEli5Toggle();
    markNav(read(KEY_DONE, {}));
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(setup);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setup);
  } else {
    setup();
  }
})();
