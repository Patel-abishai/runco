# run.co

Clickable, high-fidelity front-end prototype for **run.co**: a social app for Indian run clubs where people play real-world GPS games on foot across real streets. Launch city: Bengaluru.

Two modes:

- **Chase**: hide and seek with friends. 1 to 2 hunters, everyone else runs and hides. Hunters only see pings of where runners were, every few minutes.
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
| Onboarding | Volt splash, Chase and Turf cards, sign-in (email code or Google), location permission |
| Home and clubs | Home feed with stories, Play sheet, Join with code, demo vs bots, club page, club chat |
| Hosting Chase | Hosting unlock (₹499), setup with presets, More options, invite, lobby with hunter picks, report / block |
| Chase in game | Runner view, Hunter-pink ping flash, lock-screen alerts, out-of-zone warning, tag confirm, hunter view, team chat, game menu, Volt round over, story card |
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
- Volt `#C8FF1A`: brand, runners, your club's turf. Full-bleed on splash, round over, turf captured and the profile header.
- Ink `#101210`: base and text, primary buttons (Ink with Volt label), in-game bars.
- Hunter `#FF2E7E`: hunters, tags, pings, rival turf, alerts. Full-bleed on the ping flash.
- Paper `#F3F4EC`: light-mode background, white cards on top.
- Night map `#1C201B`: map base.
- Flat colour, 20 px cards, no gradients, one primary action per screen.

## Not real yet

This is a front-end prototype. GPS, auth, payments, chat and push are mocked with sample data (Cubbon Crew, HSR Hustlers, Indiranagar Night Runners, @priya, @arjun.k, @meghna.runs). Sliders and toggles are visual.
