# ShowMinder UI Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign ShowMinder from Bootstrap-standard to a modern dark theme with glassmorphism, responsive for iPhone 17 Pro, iPad Air M1, and desktop.

**Architecture:** Pure CSS redesign — replace `project.css` with a new dark theme using CSS custom properties. Update all Django templates to use new markup. Keep Bootstrap loaded for utilities/JS but override visual styling. Keep HTMX integration unchanged.

**Tech Stack:** Django templates, CSS custom properties, Bootstrap 5 (utilities only), Bootstrap Icons, HTMX

---

### Task 1: New CSS Theme File

**Files:**
- Rewrite: `showminder/static/css/project.css`

- [ ] **Step 1: Replace project.css with new dark theme**

```css
/* ShowMinder Dark Theme */

:root {
  --bg-primary: #0d1117;
  --bg-surface: #161b22;
  --bg-glass: rgba(255, 255, 255, 0.04);
  --border-default: rgba(255, 255, 255, 0.06);
  --border-input: rgba(255, 255, 255, 0.1);
  --border-hover: rgba(88, 166, 255, 0.3);
  --accent-blue: #58a6ff;
  --accent-green: #238636;
  --accent-green-hover: #2ea043;
  --accent-red: #f85149;
  --accent-red-bg: rgba(218, 54, 51, 0.1);
  --accent-red-border: rgba(218, 54, 51, 0.2);
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --text-muted: #484f58;
  --radius-card: 12px;
  --radius-button: 10px;
  --radius-badge: 8px;
  --radius-input: 14px;
  --radius-navbar: 14px;
  --shadow-card: 0 2px 8px rgba(0, 0, 0, 0.3);
  --shadow-card-hover: 0 12px 32px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(88, 166, 255, 0.15);
  --shadow-green-glow: 0 2px 10px rgba(35, 134, 54, 0.4);
  --transition-default: 0.2s ease;
}

html {
  position: relative;
  height: 100%;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  min-height: 100%;
  margin: 0;
}

/* --- Navbar --- */
.sm-navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  background: var(--bg-glass);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-default);
}

.sm-navbar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--text-primary);
}

.sm-navbar-brand img {
  width: 34px;
  height: 34px;
  border-radius: 9px;
}

.sm-navbar-brand span {
  font-weight: 700;
  font-size: 18px;
  letter-spacing: -0.3px;
}

.sm-navbar-actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

.sm-navbar-search {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid var(--border-input);
  border-radius: var(--radius-button);
  padding: 8px 16px;
  font-size: 13px;
  color: var(--text-primary);
  width: 240px;
  outline: none;
  transition: border-color var(--transition-default);
}

.sm-navbar-search::placeholder {
  color: var(--text-muted);
}

.sm-navbar-search:focus {
  border-color: var(--border-hover);
}

.sm-navbar-back {
  font-size: 13px;
  color: var(--accent-blue);
  text-decoration: none;
}

.sm-navbar-back:hover {
  text-decoration: underline;
  color: var(--accent-blue);
}

/* --- Buttons --- */
.sm-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 20px;
  border-radius: var(--radius-button);
  font-size: 14px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  text-decoration: none;
  transition: all var(--transition-default);
  line-height: 1;
}

.sm-btn-green {
  background: var(--accent-green);
  color: white;
  box-shadow: var(--shadow-green-glow);
}

.sm-btn-green:hover {
  background: var(--accent-green-hover);
  color: white;
}

.sm-btn-glass {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-input);
  color: var(--text-primary);
}

.sm-btn-glass:hover {
  background: rgba(255, 255, 255, 0.12);
  color: var(--text-primary);
}

.sm-btn-danger {
  background: var(--accent-red-bg);
  border: 1px solid var(--accent-red-border);
  color: var(--accent-red);
}

.sm-btn-danger:hover {
  background: rgba(218, 54, 51, 0.2);
  color: var(--accent-red);
}

.sm-btn-add-nav {
  background: linear-gradient(135deg, var(--accent-green), var(--accent-green-hover));
  width: 38px;
  height: 38px;
  border-radius: var(--radius-button);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  color: white;
  box-shadow: 0 0 16px rgba(35, 134, 54, 0.3);
  border: none;
  cursor: pointer;
  text-decoration: none;
  padding: 0;
}

.sm-btn-add-nav:hover {
  color: white;
}

/* --- Card Grid --- */
.sm-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
  padding: 24px;
}

/* --- Series Card --- */
.sm-card {
  border-radius: var(--radius-card);
  overflow: hidden;
  position: relative;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid var(--border-default);
  transition: transform var(--transition-default), box-shadow var(--transition-default), border-color var(--transition-default);
  cursor: pointer;
}

.sm-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card-hover);
  border-color: var(--border-hover);
}

.sm-card a {
  text-decoration: none;
  color: inherit;
}

.sm-card-poster {
  width: 100%;
  aspect-ratio: 2 / 3;
  object-fit: cover;
  display: block;
}

.sm-card-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  padding: 4px 10px;
  border-radius: var(--radius-badge);
  font-size: 11px;
  color: var(--accent-blue);
  font-weight: 600;
}

.sm-card-info {
  padding: 14px;
}

.sm-card-title {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sm-card-date {
  font-size: 11px;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 4px;
}

.sm-card-episode-btn {
  position: absolute;
  bottom: 14px;
  right: 14px;
  background: var(--accent-green);
  width: 32px;
  height: 32px;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: var(--shadow-green-glow);
  text-decoration: none;
  font-size: 14px;
  z-index: 2;
  border: none;
  cursor: pointer;
}

.sm-card-episode-btn:hover {
  background: var(--accent-green-hover);
  color: white;
}

/* --- Add Page --- */
.sm-add-hero {
  text-align: center;
  padding: 48px 24px 0;
}

.sm-add-hero h1 {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin: 0 0 8px;
}

.sm-add-hero p {
  font-size: 15px;
  color: var(--text-secondary);
  margin: 0;
}

.sm-add-search {
  max-width: 560px;
  margin: 32px auto 0;
  padding: 0 24px;
}

.sm-add-search input {
  width: 100%;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 16px 22px;
  font-size: 16px;
  color: var(--text-primary);
  outline: none;
  transition: border-color var(--transition-default);
  box-sizing: border-box;
}

.sm-add-search input::placeholder {
  color: var(--text-muted);
}

.sm-add-search input:focus {
  border-color: var(--border-hover);
}

/* --- Search Results (Add Page) --- */
.sm-search-results {
  max-width: 560px;
  margin: 16px auto 0;
  padding: 0 24px 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sm-search-result {
  display: flex;
  gap: 14px;
  align-items: center;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: var(--radius-card);
  padding: 12px 14px;
  cursor: pointer;
  transition: background var(--transition-default);
}

.sm-search-result:hover {
  background: rgba(255, 255, 255, 0.08);
}

.sm-search-result-poster {
  width: 52px;
  height: 74px;
  border-radius: var(--radius-badge);
  object-fit: cover;
  flex-shrink: 0;
}

.sm-search-result-info {
  flex: 1;
  min-width: 0;
}

.sm-search-result-title {
  font-size: 15px;
  font-weight: 600;
  margin: 0 0 2px;
  color: var(--text-primary);
}

.sm-search-result-meta {
  font-size: 12px;
  color: var(--text-secondary);
}

.sm-search-result-rating {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 4px;
  font-size: 12px;
}

.sm-search-result-rating .star {
  color: #f0b429;
}

.sm-search-result .sm-btn {
  flex-shrink: 0;
  padding: 8px 16px;
  font-size: 13px;
}

/* --- Detail Page --- */
.sm-detail-hero {
  position: relative;
  padding: 40px 32px 32px;
}

.sm-detail-hero-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(88, 166, 255, 0.15) 0%, var(--bg-primary) 100%);
  z-index: 0;
}

.sm-detail-hero-content {
  position: relative;
  z-index: 1;
  display: flex;
  gap: 28px;
}

.sm-detail-poster {
  width: 160px;
  height: 230px;
  border-radius: var(--radius-card);
  object-fit: cover;
  flex-shrink: 0;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
}

.sm-detail-info {
  flex: 1;
  padding-top: 8px;
}

.sm-detail-title {
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -0.5px;
  margin: 0 0 6px;
}

.sm-detail-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
  font-size: 14px;
  color: var(--text-secondary);
}

.sm-detail-meta .star {
  color: #f0b429;
}

.sm-detail-tagline {
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 24px;
  font-style: italic;
  max-width: 500px;
}

.sm-detail-actions {
  display: flex;
  gap: 10px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.sm-detail-cards {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}

.sm-detail-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-button);
  padding: 16px 20px;
  flex: 1;
  min-width: 140px;
}

.sm-detail-card-label {
  font-size: 11px;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.8px;
  margin-bottom: 6px;
}

.sm-detail-card-value {
  font-size: 22px;
  font-weight: 700;
}

.sm-detail-card-value .genre-tag {
  background: rgba(88, 166, 255, 0.12);
  color: var(--accent-blue);
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 12px;
  margin-right: 4px;
  display: inline-block;
  margin-bottom: 4px;
}

.sm-detail-danger {
  padding: 20px 32px;
  display: flex;
  gap: 10px;
}

/* Refresh search on detail page */
.sm-detail-refresh-search input {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--radius-button);
  padding: 8px 16px;
  font-size: 14px;
  color: var(--text-primary);
  outline: none;
  width: 300px;
  max-width: 100%;
}

.sm-detail-refresh-search input::placeholder {
  color: var(--text-muted);
}

/* --- Content container --- */
.sm-content {
  padding: 0;
}

/* --- Notifications --- */
.sm-notification {
  background: rgba(255, 166, 0, 0.1);
  border: 1px solid rgba(255, 166, 0, 0.2);
  border-radius: var(--radius-button);
  padding: 16px 20px;
  margin: 16px 24px;
}

.sm-notification h2 {
  font-size: 18px;
  font-weight: 700;
  margin: 0 0 8px;
  color: #ffa600;
}

.sm-notification p {
  font-size: 14px;
  color: var(--text-secondary);
  margin: 0 0 8px;
}

/* No search results */
.sm-no-results {
  text-align: center;
  color: var(--text-secondary);
  padding: 40px 24px;
  font-size: 15px;
}

/* --- Responsive --- */

/* Tablet portrait (iPad Air) */
@media (max-width: 820px) {
  .sm-grid {
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 14px;
    padding: 20px;
  }

  .sm-detail-poster {
    width: 120px;
    height: 170px;
  }

  .sm-detail-title {
    font-size: 26px;
  }

  .sm-detail-card-value {
    font-size: 18px;
  }

  .sm-detail-hero {
    padding: 28px 20px 24px;
  }

  .sm-detail-danger {
    padding: 16px 20px;
  }
}

/* Mobile (iPhone 17 Pro and similar) */
@media (max-width: 480px) {
  .sm-navbar {
    padding: 10px 14px;
  }

  .sm-navbar-brand span {
    display: none;
  }

  .sm-navbar-search {
    width: 140px;
    font-size: 12px;
    padding: 7px 12px;
  }

  .sm-btn-add-nav {
    width: 34px;
    height: 34px;
    font-size: 18px;
  }

  .sm-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    padding: 12px;
  }

  .sm-card-info {
    padding: 10px;
  }

  .sm-card-title {
    font-size: 13px;
  }

  .sm-card-badge {
    font-size: 10px;
    padding: 3px 7px;
  }

  .sm-card-episode-btn {
    width: 28px;
    height: 28px;
    font-size: 12px;
    bottom: 10px;
    right: 10px;
  }

  .sm-add-hero {
    padding: 32px 16px 0;
  }

  .sm-add-hero h1 {
    font-size: 24px;
  }

  .sm-add-search {
    padding: 0 16px;
    margin-top: 24px;
  }

  .sm-add-search input {
    padding: 14px 18px;
    font-size: 15px;
  }

  .sm-search-results {
    padding: 0 16px 16px;
  }

  .sm-search-result {
    padding: 10px;
    gap: 10px;
  }

  .sm-search-result-poster {
    width: 44px;
    height: 62px;
  }

  .sm-search-result-title {
    font-size: 14px;
  }

  .sm-detail-hero {
    padding: 24px 16px 20px;
  }

  .sm-detail-hero-content {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .sm-detail-poster {
    width: 140px;
    height: 200px;
  }

  .sm-detail-info {
    padding-top: 0;
  }

  .sm-detail-title {
    font-size: 24px;
  }

  .sm-detail-meta {
    justify-content: center;
    flex-wrap: wrap;
  }

  .sm-detail-tagline {
    max-width: 100%;
  }

  .sm-detail-actions {
    justify-content: center;
  }

  .sm-detail-cards {
    flex-direction: column;
  }

  .sm-detail-card {
    min-width: auto;
  }

  .sm-detail-danger {
    padding: 16px;
    flex-wrap: wrap;
  }

  .sm-detail-refresh-search input {
    width: 100%;
  }

  .sm-notification {
    margin: 12px;
  }
}
```

- [ ] **Step 2: Verify CSS loads without errors**

Run: open the app in a browser, check DevTools console for CSS errors.

- [ ] **Step 3: Commit**

```bash
git add showminder/static/css/project.css
git commit -m "style: replace project.css with dark theme using CSS custom properties"
```

---

### Task 2: Update Base Template and Navbar

**Files:**
- Modify: `showminder/templates/base.html`
- Modify: `showminder/templates/bootstrap.html`

- [ ] **Step 1: Update bootstrap.html — add dark background to body**

Replace the contents of `showminder/templates/bootstrap.html` with:

```html
<!DOCTYPE html>
{% load bootstrap5 %}
{% load static %}
<html{% if request.LANGUAGE_CODE %} lang="{{ request.LANGUAGE_CODE }}" {% endif %}>

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <title> ShowMinder </title>
        {% bootstrap_css %}
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css">

        <script src="https://unpkg.com/htmx.org@1.6.0"></script>

        {% block bootstrap_extra_head %}{% endblock %}
    </head>

    <body style="background-color: #0d1117;">
        {% block bootstrap_content %}
        content
        {% endblock %}

        {% bootstrap_javascript %}
        <script>
            document.body.addEventListener('htmx:configRequest', (event) => {
                event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
            })
        </script>

        {% block bootstrap_extra_script %}{% endblock %}
    </body>

    </html>
```

- [ ] **Step 2: Update base.html — replace Bootstrap navbar with custom dark navbar**

Replace the contents of `showminder/templates/base.html` with:

```html
{% extends 'bootstrap.html' %}

{% load static %}

{% block bootstrap_extra_head %}

<link href="{% static 'css/project.css' %}" rel="stylesheet">

<link rel="apple-touch-icon" sizes="57x57" href="{% static 'images/apple-icon-57x57.png' %}">
<link rel="apple-touch-icon" sizes="60x60" href="{% static 'images/apple-icon-60x60.png' %}">
<link rel="apple-touch-icon" sizes="72x72" href="{% static 'images/apple-icon-72x72.png' %}">
<link rel="apple-touch-icon" sizes="76x76" href="{% static 'images/apple-icon-76x76.png' %}">
<link rel="apple-touch-icon" sizes="114x114" href="{% static 'images/apple-icon-114x114.png' %}">
<link rel="apple-touch-icon" sizes="120x120" href="{% static 'images/apple-icon-120x120.png' %}">
<link rel="apple-touch-icon" sizes="144x144" href="{% static 'images/apple-icon-144x144.png' %}">
<link rel="apple-touch-icon" sizes="152x152" href="{% static 'images/apple-icon-152x152.png' %}">
<link rel="apple-touch-icon" sizes="180x180" href="{% static 'images/apple-icon-180x180.png' %}">
<link rel="mask-icon" href="{% static 'images/apple-icon-57x57.png' %}">
<link rel="icon" type="image/png" sizes="192x192" href="{% static 'images/android-icon-192x192.png' %}">
<link rel="icon" type="image/png" sizes="32x32" href="{% static 'images/favicon-32x32.png' %}">
<link rel="icon" type="image/png" sizes="96x96" href="{% static 'images/favicon-96x96.png' %}">
<link rel="icon" type="image/png" sizes="16x16" href="{% static 'images/favicon-16x16.png' %}">
<link rel="manifest" href="{% static 'images/manifest.json' %}">
<meta name="msapplication-TileColor" content="#0d1117">
<meta name="msapplication-TileImage" content="{% static 'images/ms-icon-144x144.png' %}">
<meta name="theme-color" content="#0d1117">
{% endblock %}

{% block bootstrap_content %}
{% if user.is_authenticated %}
<nav class="sm-navbar">
    <a class="sm-navbar-brand" href="{% url 'frontend:index' %}">
        <img src="{% static 'images/apple-icon-57x57.png' %}" alt="ShowMinder">
        <span>ShowMinder</span>
    </a>
    <div class="sm-navbar-actions">
        {% block navbar_right %}
        <form method="GET" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
            <input class="sm-navbar-search" type="search" name="search" placeholder="Search shows..." aria-label="Search">
        </form>
        <a class="sm-btn-add-nav" href="{% url 'frontend:add' %}" aria-label="Add show">
            <i class="bi bi-plus"></i>
        </a>
        {% endblock %}
    </div>
</nav>
{% endif %}

<div class="sm-content">
    {% if api_notifications %}
    {% for m in api_notifications %}
    <div class="sm-notification">
        <h2>{{ m.subject }}</h2>
        <p>{{ m.message }}</p>
        <a class="sm-btn sm-btn-danger" href="{% url 'api:delete-notification' pk=m.pk %}">
            <i class="bi bi-x-lg"></i> Dismiss
        </a>
    </div>
    {% endfor %}
    {% endif %}

    {% block content %}{% endblock %}
</div>
{% endblock %}
```

- [ ] **Step 3: Verify navbar renders correctly**

Run the app, check that the dark navbar with glassmorphism appears, search and + button work.

- [ ] **Step 4: Commit**

```bash
git add showminder/templates/base.html showminder/templates/bootstrap.html
git commit -m "style: update base templates with dark glassmorphism navbar"
```

---

### Task 3: Update Homepage and Series Card

**Files:**
- Modify: `showminder/frontend/templates/index.html`
- Modify: `showminder/frontend/templates/partials/series-list.html`

- [ ] **Step 1: Update index.html**

Replace the contents of `showminder/frontend/templates/index.html` with:

```html
{% extends "base.html" %}

{% load static %}
{% load bootstrap5 %}

{% block content %}
<div class="sm-grid">
    {% include "partials/series-list.html" %}
</div>
{% endblock %}
```

- [ ] **Step 2: Update series-list.html with new card markup**

Replace the contents of `showminder/frontend/templates/partials/series-list.html` with:

```html
{% for t in object_list %}
<div class="sm-card" {% if forloop.last and page_obj.has_next %}
    hx-get="{% url 'frontend:index' %}?page={{ page_obj.number|add:1 }}" hx-trigger="revealed" hx-swap="afterend"
    hx-target="this" {% endif %}>
    <a href="{% url 'frontend:detail' tvshow=t.pk %}">
        <img src="{{ t.cover_url }}" class="sm-card-poster" alt="{{ t.title }}">
        <div class="sm-card-badge">S{{ t.season }} / E{{ t.episode }}</div>
        <div class="sm-card-info">
            <h3 class="sm-card-title">{{ t.title }}</h3>
            <div class="sm-card-date">
                <i class="bi bi-calendar-date"></i> {{ t.last_seen|date:"DATE_FORMAT" }}
            </div>
        </div>
    </a>
    <a class="sm-card-episode-btn" href="{% url 'frontend:inc-episode' tvshow=t.pk %}">
        <i class="bi bi-skip-forward-fill"></i>
    </a>
</div>
{% endfor %}
```

- [ ] **Step 3: Test homepage rendering**

Open the app in browser. Verify:
1. Cards display in responsive grid
2. Poster fills card width with correct aspect ratio
3. Season/Episode badge appears top-right
4. Hover effect works (card lifts, blue glow)
5. Green episode button is in bottom-right
6. Infinite scroll still works (scroll to bottom, next page loads)

- [ ] **Step 4: Test responsive — resize to 393px width (iPhone 17 Pro)**

Verify: 2-column grid, smaller cards, badge and button scale down, text doesn't overflow.

- [ ] **Step 5: Test responsive — resize to 820px width (iPad Air)**

Verify: ~3-4 column grid, appropriate spacing.

- [ ] **Step 6: Commit**

```bash
git add showminder/frontend/templates/index.html showminder/frontend/templates/partials/series-list.html
git commit -m "style: redesign homepage with dark cards grid and responsive layout"
```

---

### Task 4: Update Add Page and Search Results

**Files:**
- Modify: `showminder/frontend/templates/add.html`
- Modify: `showminder/frontend/templates/partials/search-results.html`

- [ ] **Step 1: Update add.html with centered search layout**

Replace the contents of `showminder/frontend/templates/add.html` with:

```html
{% extends "base.html" %}

{% load bootstrap5 %}

{% block navbar_right %}
<a class="sm-navbar-back" href="{% url 'frontend:index' %}">
    <i class="bi bi-arrow-left"></i> Back to shows
</a>
{% endblock %}

{% block content %}
<div class="sm-add-hero">
    <h1>Add a new show</h1>
    <p>Search TMDB to find and import a TV show</p>
</div>
<div class="sm-add-search">
    <input type="text"
        hx-post="{% url 'frontend:htmx-search-tmdb-for-add' %}" hx-target="#results"
        hx-trigger="keyup changed delay:500ms" name="search"
        placeholder="Search for a TV show..." autocomplete="off" autocorrect="off" autocapitalize="off"
        spellcheck="false" />
</div>
<div id="results"></div>
{% endblock %}
```

- [ ] **Step 2: Update search-results.html with list-style results**

Replace the contents of `showminder/frontend/templates/partials/search-results.html` with:

```html
{% if results %}
<div class="sm-search-results">
    {% for tv in results %}
    <div class="sm-search-result" hx-post="{% url 'frontend:htmx-add-tv' tmdb_id=tv.tmdb_id %}">
        <img src="{{ tv.cover_url }}" class="sm-search-result-poster" alt="{{ tv.title }}">
        <div class="sm-search-result-info">
            <h4 class="sm-search-result-title">{{ tv.title }}</h4>
            <div class="sm-search-result-meta">
                {% if tv.release_date %}{{ tv.release_date|date:"Y" }} · {% endif %}{{ tv.genres|default:"" }}
            </div>
            <div class="sm-search-result-rating">
                <span class="star">★</span>
                <span>{{ tv.rating }}</span>
            </div>
        </div>
        <button class="sm-btn sm-btn-green" type="button">+ Add</button>
    </div>
    {% endfor %}
</div>
{% else %}
<p class="sm-no-results">No search results</p>
{% endif %}
```

- [ ] **Step 3: Test add page**

Verify:
1. Centered hero text and search input display correctly
2. "Back to shows" link in navbar works
3. Search HTMX trigger works (type, wait 500ms, results appear)
4. Results show with poster thumbnail, title, year, rating, and "+ Add" button
5. Clicking a result adds the show and redirects to homepage

- [ ] **Step 4: Test responsive (393px and 820px)**

Verify: search input goes full-width on mobile, results stack cleanly.

- [ ] **Step 5: Commit**

```bash
git add showminder/frontend/templates/add.html showminder/frontend/templates/partials/search-results.html
git commit -m "style: redesign add page with centered search and list-style results"
```

---

### Task 5: Update Detail Page

**Files:**
- Modify: `showminder/frontend/templates/detail.html`

- [ ] **Step 1: Update detail.html with hero layout**

Replace the contents of `showminder/frontend/templates/detail.html` with:

```html
{% extends "base.html" %}

{% load bootstrap5 %}

{% block navbar_right %}
<a class="sm-navbar-back" href="{% url 'frontend:index' %}">
    <i class="bi bi-arrow-left"></i> Back to shows
</a>
{% endblock %}

{% block content %}
<div class="sm-detail-hero">
    <div class="sm-detail-hero-bg"></div>
    <div class="sm-detail-hero-content">
        <img src="{{ tvshow.cover_url }}" class="sm-detail-poster" alt="{{ tvshow.title }}">
        <div class="sm-detail-info">
            <h1 class="sm-detail-title">{{ tvshow.title }}</h1>
            <div class="sm-detail-meta">
                <span class="star">★ {{ tvshow.rating }}</span>
                <span>·</span>
                <span>{{ tvshow.genres|default:"" }}</span>
                {% if tvshow.release_date %}
                <span>·</span>
                <span>{{ tvshow.release_date|date:"Y" }}</span>
                {% endif %}
            </div>

            {% if tvshow.tagline %}
            <p class="sm-detail-tagline">"{{ tvshow.tagline }}"</p>
            {% endif %}

            <div class="sm-detail-actions">
                <a class="sm-btn sm-btn-green" href="{% url 'frontend:inc-episode' tvshow=tvshow.pk %}">
                    <i class="bi bi-skip-forward-fill"></i> Next Episode
                </a>
                <a class="sm-btn sm-btn-glass" href="{% url 'frontend:inc-season' tvshow=tvshow.pk %}">
                    <i class="bi bi-plus-square"></i> Season
                </a>

                {% if tvshow.movie_db == 'tmdb' %}
                <button class="sm-btn sm-btn-glass"
                    hx-post="{% url 'frontend:htmx-refresh-tv' tmdb_id=tvshow.tmdb_id tvshow=tvshow.pk %}">
                    <i class="bi bi-arrow-clockwise"></i> Refresh
                </button>
                {% else %}
                <div class="sm-detail-refresh-search">
                    <input type="text"
                        hx-post="{% url 'frontend:htmx-search-tmdb-for-refresh' tvshow=tvshow.pk %}" hx-target="#results"
                        hx-trigger="keyup changed delay:500ms" name="search"
                        placeholder="Search to refresh from..." autocomplete="off" autocorrect="off" autocapitalize="off"
                        spellcheck="false" />
                </div>
                {% endif %}
            </div>

            <div id="results"></div>

            <div class="sm-detail-cards">
                <div class="sm-detail-card">
                    <div class="sm-detail-card-label">Progress</div>
                    <div class="sm-detail-card-value">S{{ tvshow.season }} / E{{ tvshow.episode }}</div>
                </div>
                <div class="sm-detail-card">
                    <div class="sm-detail-card-label">Last Seen</div>
                    <div class="sm-detail-card-value">{{ tvshow.last_seen|date:"DATE_FORMAT" }}</div>
                </div>
                <div class="sm-detail-card">
                    <div class="sm-detail-card-label">Genres</div>
                    <div class="sm-detail-card-value">
                        {% for genre in tvshow.genres.split:", " %}
                        <span class="genre-tag">{{ genre }}</span>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="sm-detail-danger">
    <a class="sm-btn sm-btn-glass" href="{% url 'admin:frontend_tvshow_change' tvshow.pk %}">
        <i class="bi bi-pencil-square"></i> Admin
    </a>
    <a class="sm-btn sm-btn-danger" href="{% url 'frontend:delete' tvshow=tvshow.pk %}">
        <i class="bi bi-trash"></i> Delete
    </a>
</div>
{% endblock %}
```

- [ ] **Step 2: Test detail page**

Verify:
1. Hero gradient background renders
2. Poster displays on left, info on right
3. Title, rating, genres, tagline display correctly
4. "Next Episode", "Season", "Refresh" buttons work
5. Info cards (Progress, Last Seen, Genres with tags) display
6. Admin and Delete buttons at bottom
7. For non-TMDB shows: refresh search input appears and HTMX works

- [ ] **Step 3: Test the genre split template tag**

The `{{ tvshow.genres.split:", " }}` Django template syntax may not work directly. If genres don't render as tags, we need a template filter. Test with a show that has genres.

If the split doesn't work, add a simple template filter. Create `showminder/frontend/templatetags/__init__.py` and `showminder/frontend/templatetags/show_tags.py`:

```python
from django import template

register = template.Library()


@register.filter
def split(value: str, sep: str = ",") -> list[str]:
    """Split a string by separator and strip whitespace."""
    if not value:
        return []
    return [item.strip() for item in value.split(sep)]
```

Then in the template, replace the genres section with:

```html
{% load show_tags %}
...
{% for genre in tvshow.genres|split:"," %}
<span class="genre-tag">{{ genre }}</span>
{% endfor %}
```

- [ ] **Step 4: Test responsive (393px — iPhone 17 Pro)**

Verify: Poster stacks above info (centered), buttons wrap, info cards stack vertically.

- [ ] **Step 5: Test responsive (820px — iPad Air)**

Verify: Side-by-side layout, smaller poster, adjusted font sizes.

- [ ] **Step 6: Commit**

```bash
git add showminder/frontend/templates/detail.html
# if template filter was needed:
git add showminder/frontend/templatetags/
git commit -m "style: redesign detail page with hero layout and info cards"
```

---

### Task 6: Update Refresh Results Partial

**Files:**
- Modify: `showminder/frontend/templates/partials/refresh-results.html`

- [ ] **Step 1: Update refresh-results.html to match new search result style**

Replace the contents of `showminder/frontend/templates/partials/refresh-results.html` with:

```html
{% if results %}
<div class="sm-search-results" style="padding-top: 8px;">
    {% for tv in results %}
    <div class="sm-search-result"
        hx-post="{% url 'frontend:htmx-refresh-tv' tmdb_id=tv.tmdb_id tvshow=tvshow %}">
        <img src="{{ tv.cover_url }}" class="sm-search-result-poster" alt="{{ tv.title }}">
        <div class="sm-search-result-info">
            <h4 class="sm-search-result-title">{{ tv.title }}</h4>
            <div class="sm-search-result-meta">
                {% if tv.release_date %}{{ tv.release_date|date:"Y" }}{% endif %}
            </div>
            <div class="sm-search-result-rating">
                <span class="star">★</span>
                <span>{{ tv.rating }}</span>
            </div>
        </div>
        <button class="sm-btn sm-btn-glass" type="button">
            <i class="bi bi-arrow-clockwise"></i> Use
        </button>
    </div>
    {% endfor %}
</div>
{% else %}
<p class="sm-no-results">No search results</p>
{% endif %}
```

- [ ] **Step 2: Verify on detail page for non-TMDB show**

Test: open a show without TMDB data, search for a show to refresh from, verify results display with new styling.

- [ ] **Step 3: Commit**

```bash
git add showminder/frontend/templates/partials/refresh-results.html
git commit -m "style: update refresh results partial to match new dark theme"
```

---

### Task 7: Clean Up site.css

**Files:**
- Modify: `site.css`

- [ ] **Step 1: Update site.css for new navbar class**

Replace the contents of `site.css` with:

```css
/* header is draggable... */
.sm-navbar {
    -webkit-app-region: drag;
}

/* but any buttons or anything else inside the header shouldn't be draggable */
.sm-navbar button, .sm-navbar a, .sm-navbar input {
    -webkit-app-region: no-drag;
}
```

- [ ] **Step 2: Commit**

```bash
git add site.css
git commit -m "style: update site.css selectors for new navbar class"
```

---

### Task 8: Final Visual QA

- [ ] **Step 1: Full QA on desktop (> 1024px)**

Check all pages: homepage grid, add page, detail page, search functionality, infinite scroll.

- [ ] **Step 2: QA on iPad Air M1 (820px viewport)**

Use Chrome DevTools device toolbar: "iPad Air" preset. Check all pages.

- [ ] **Step 3: QA on iPhone 17 Pro (393px viewport)**

Use Chrome DevTools: set viewport to 393x852. Check all pages.

- [ ] **Step 4: Fix any visual issues found**

Address any spacing, overflow, or layout issues found during QA.

- [ ] **Step 5: Final commit if fixes were needed**

```bash
git add -u
git commit -m "fix: visual QA fixes for responsive layout"
```
