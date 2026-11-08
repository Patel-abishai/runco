# run.co

Clickable, high-fidelity front-end prototype for **run.co**: a social app for Indian run clubs where people play real-world GPS games on foot across real streets. Launch city: Bengaluru.

Two games:

- **Chase**: hide and seek. Hunters vs Runners, pings every few minutes, shrinking zone, Classic and Infection modes.
- **Raid**: club vs club capture the flag. Hold 10 s on the enemy flag, carry it home, win turf on the Bengaluru hex map.

## Run it

No build step needed to view it. Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 5173
# then open http://localhost:5173
```

On desktop you get a 390 x 844 phone frame plus a list of every screen. On a phone it goes full screen. Every button links to the next screen, so you can tap through the whole flow.

Deploys as-is to GitHub Pages, Vercel or Netlify (static site, root folder).

## The flow (41 screens)

| Section | Screens |
| --- | --- |
| Onboarding | Splash, Chase / Raid / Turf cards, sign-in (email code or Google), location permission |
| Home and discovery | Home feed with stories, Join with code, Explore map, Play + sheet, demo round vs bots, club profile, club chat |
| Hosting | Hosting unlock (₹499), Club Pro (₹2,999), Host Chase setup, Host Raid setup, invite share sheet, lobby, report / block |
| Chase in game | Runner view, Ping flash, lock-screen alerts, out-of-zone warning, tag confirm, Hunter view, Team Radio, round menu, round over, story card |
| Raid and Turf | Flag hold timer, carrying the flag, flag dropped, Raid over, Bengaluru Turf |
| Ranks and you | Ranks (Players / Clubs / Cities), leaderboards-off state, profile, settings |

Three taps from a cold open to a live game: Splash → **Play a demo round now** → **Start demo**.

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

- Font: Satoshi (Fontshare), Medium for body, Bold / Black for headings and big numbers.
- Base `#0E0E10`, text `#F4F3EE`, accent lime `#C6FF3D` (primary actions, your team), hot `#FF4D2E` (opposing team, danger).
- 20 px cards, 44 px minimum targets, glow only on live elements.
- Rule of colour: lime is always *your* side. As a runner your teammates are lime; once you switch to hunter, hunters turn lime and runner pings turn hot.

## Not real yet

This is a front-end prototype. GPS, auth, payments, chat and push are mocked with sample data (Cubbon Crew, HSR Hustlers, @priya, @arjun.k, @meghna.runs). Sliders and toggles are visual.
