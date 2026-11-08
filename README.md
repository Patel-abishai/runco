# run.co

Clickable, high-fidelity front-end prototype for **run.co**: a social app for Indian run clubs where people play real-world GPS games on foot across real streets. Launch city: Bengaluru.

Two modes:

- **Chase**: hide and seek with friends. 1 to 2 seekers, everyone else hides. Seekers only see pings of where hiders were, every few minutes.
- **Turf**: async territory capture. Club members' normal runs paint Bengaluru's hex map. Rivals can steal hexes; your club gets a 5-day window to reclaim them.

## Run it

No build step needed to view it. Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 5173
# then open http://localhost:5173
```

On desktop you get a 390 x 844 phone frame plus a list of every screen. On a phone it goes full screen. Every button links to the next screen, so you can tap through the whole flow.

Deploys as-is to GitHub Pages, Vercel or Netlify (static site, root folder).

## The flow (38 screens)

| Section | Screens |
| --- | --- |
| Onboarding | Cobalt splash, Chase and Turf cards, sign-in (email code or Google), location permission |
| Home and clubs | Home feed with stories, Play sheet, Join with code, demo vs bots, club page, club chat |
| Hosting Chase | Hosting unlock (₹499), setup with presets, More options, invite, lobby with seeker picks, report / block |
| Chase in game | Hider view, Mango ping flash, lock-screen alerts, out-of-zone warning, tag confirm, seeker view, team chat, game menu, Cobalt round over, story card |
| Turf | Club Pro (₹2,999), Bengaluru Turf map, club run in progress, run summary, solo run |
| Ranks and you | Ranks (Players / Clubs), leaderboards-off state, profile dashboard, badges, settings |

Two taps from a cold open to a live game: Splash → **Play a demo now** → **Start demo**.

## Structure

```
index.html          generated: every screen as a <section>, hash routes (#Home, #Lobby ...)
app.js              tiny router
styles/runco.css    design system (generated from design/runco.css)
styles/shell.css    phone frame + screen list
assets/             Bengaluru night map, turf hex overlay
design/             source of truth: one .dc.html per screen + canvas.json (screen order)
tools/build.py      regenerates index.html and styles/runco.css from design/
```

Edit a screen in `design/`, then run `python3 tools/build.py`.

## Design system

- Font: Satoshi (Fontshare). Black for headings and big numbers, Medium for body.
- Light mode. Paper `#F7F5F0` background, White cards, Midnight `#0B1026` text, in-game bars and map.
- Cobalt `#2B3BFF`: brand, primary buttons, your team, your club's turf. Used full-bleed on splash, round over and turf captured.
- Mango `#FFB020`: seekers, pings, rival turf, alerts. Full-bleed on the ping flash.
- Mint `#2EE59D`: success (reclaimed, never caught).
- Flat colour, 20 px cards, no gradients, no heavy shadows, one primary action per screen.

## Not real yet

This is a front-end prototype. GPS, auth, payments, chat and push are mocked with sample data (Cubbon Crew, HSR Hustlers, Indiranagar Night Runners, @priya, @arjun.k, @meghna.runs). Sliders and toggles are visual.
