# ShowMinder UI Redesign — Design Spec

## Overview

Redesign the ShowMinder UI from the current Bootstrap-standard look to a modern dark theme with glassmorphism effects, inspired by Netflix/Plex. The design must be responsive for iPhone 17 Pro (393pt), iPad Air M1 (820pt), and desktop.

## Design Direction

**Theme:** Modern & Dark with glassmorphism accents, glow effects, and poster-focused card layouts.

## Color Palette

| Token            | Value     | Usage                        |
|------------------|-----------|------------------------------|
| `--bg-primary`   | `#0d1117` | Page background              |
| `--bg-surface`   | `#161b22` | Card/surface backgrounds     |
| `--bg-glass`     | `rgba(255,255,255,0.04)` | Glassmorphism panels |
| `--border-default` | `rgba(255,255,255,0.06)` | Default borders      |
| `--border-input` | `rgba(255,255,255,0.1)` | Input borders         |
| `--border-hover` | `rgba(88,166,255,0.3)` | Hover glow borders    |
| `--accent-blue`  | `#58a6ff` | Links, badges, accents       |
| `--accent-green` | `#238636` | Primary actions (add, next)  |
| `--accent-red`   | `#f85149` | Danger actions (delete)      |
| `--text-primary` | `#e6edf3` | Primary text                 |
| `--text-secondary` | `#8b949e` | Secondary text, labels     |
| `--text-muted`   | `#484f58` | Placeholder text             |

## Typography

- Font family: `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- Headlines: font-weight 700-800, letter-spacing -0.3 to -0.5px
- Body text: font-weight 400-500, 13-15px
- Labels: 11px, uppercase, letter-spacing 0.8px

## Design Tokens

- **Border radius:** Cards 12px, Buttons 10px, Badges 8px, Inputs 14-16px
- **Shadows:** Glow-style `rgba(color, 0.3)` for buttons, `rgba(0,0,0,0.4)` for cards on hover
- **Glassmorphism:** `background: rgba(255,255,255,0.04)`, `backdrop-filter: blur(12px)`, subtle border
- **Transitions:** 0.2-0.3s ease for hover, transform, opacity

## Responsive Breakpoints

| Breakpoint | Device          | Grid Columns | Card Width | Notes                    |
|------------|-----------------|--------------|------------|--------------------------|
| < 480px    | iPhone 17 Pro   | 2            | ~170px     | Compact navbar, no text in logo, smaller padding |
| 480-820px  | iPad portrait   | 3            | ~230px     | Medium padding           |
| 820-1024px | iPad landscape  | 4            | ~200px     | Full navbar              |
| > 1024px   | Desktop         | 5+           | ~220px     | Full layout, auto-fill   |

Grid: `display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 16px;`

Mobile adjustments: gap 10px, padding 12px, font sizes reduced by ~2px.

## Pages

### 1. Navbar (all pages)

**Current:** Standard Bootstrap dark navbar with inline search and + button.

**New:**
- Glassmorphism bar: `rgba(255,255,255,0.04)` background, `backdrop-filter: blur(12px)`, subtle border, rounded corners (14px)
- Left: App icon (gradient blue-purple, 32x32, rounded 9px) + "ShowMinder" text
- Right: Search input (glass style, placeholder "Search shows...") + green "+" button (gradient green, glow shadow)
- **Mobile (< 480px):** Logo text hidden (`d-none`), search input shrinks, icon-only + button
- **Tablet:** Full navbar, slightly reduced padding

### 2. Homepage (index.html, series-list.html)

**Current:** Bootstrap cards with poster as `card-img-top`, overlay caption using `carousel-caption`, fixed 22rem width, green cloud-plus button.

**New:**
- CSS Grid layout (responsive auto-fill, see breakpoints)
- Cards: Dark surface background, subtle border, rounded 12px
  - Poster image on top (fills card width, `object-fit: cover`)
  - Season/Episode badge: top-right of poster, glassmorphism pill (`rgba(0,0,0,0.65)`, blur, blue text)
  - Below poster: Title (14px, 600 weight, ellipsis overflow) + date (11px, secondary color, calendar icon)
  - "Next Episode" button: green, 32x32, rounded 9px, bottom-right of card, glow shadow
- **Hover effect:** Card lifts (`translateY(-4px)`), blue glow border, deeper shadow
- **Mobile:** 2-column grid, smaller cards, badge and button scale down slightly
- Infinite scroll (existing HTMX) remains unchanged

### 3. Add Page (add.html, search-results.html)

**Current:** Plain "Import new TV Show" h1 heading, bare text input with fixed 20rem width, results appear below.

**New:**
- Centered layout with hero text: "Add a new show" (32px, 800 weight, gradient text), subtitle below
- "← Back to shows" link in navbar (accent blue)
- Large centered search input: glass style, 560px max-width, rounded 16px, search icon, larger padding
- Search results as vertical list (not card grid):
  - Each result: poster thumbnail (52x74px, rounded 8px) + title + year/genre + rating star + "+ Add" button (green, rounded 10px)
  - Results container: same max-width as search input
- **Mobile:** Search input full-width with horizontal padding, results stack naturally
- HTMX search trigger remains unchanged (keyup delay 500ms)

### 4. Detail Page (detail.html)

**Current:** Large poster image, buttons below, plain table with show metadata, admin/delete buttons at bottom.

**New:**
- "← Back to shows" link in navbar
- Hero section: gradient from poster's dominant color fading to background
  - Poster (160x230px, rounded 12px, deep shadow) on the left
  - Right side: Title (32px, 800 weight), rating/genre/year inline, tagline in italic
  - Action buttons row: "▶ Next Episode" (green, primary), "+ Season" (glass), "↻ Refresh" (glass)
  - Info cards row (3 cards): Progress (S/E), Last Seen (date), Genres (as blue tags)
- Danger zone at bottom: Admin button (glass, secondary), Delete button (red tinted background)
- **Mobile (< 480px):** Poster stacks above info (full width, centered), buttons wrap, info cards stack 1 column
- **Tablet:** Same layout as desktop but poster slightly smaller (120x170px)
- Refresh search input (for non-TMDB shows) styled same as add page search

### 5. Login Page (registration/login.html)

Not in scope — keep current Bootstrap styling.

## Technical Approach

- Replace `project.css` with new dark theme CSS using CSS custom properties for all colors
- Replace Bootstrap's `bg-dark` navbar with custom glassmorphism navbar in `base.html`
- Keep Bootstrap grid/utilities loaded but override with custom CSS where needed
- Keep Bootstrap JS for any toggler/collapse functionality
- Keep HTMX integration unchanged
- Keep `bootstrap-icons` for icons
- No additional JS frameworks or libraries needed

## Out of Scope

- Dark/light mode toggle (dark only)
- Login/registration page styling
- Admin pages
- 404/500 error pages
- Animation/micro-interaction library
