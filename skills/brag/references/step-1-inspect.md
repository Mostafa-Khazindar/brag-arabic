# Step 1: Inspect the project

Read the project directory to understand what you're bragging about.

This step is language-independent — you're reading the source code and extracting meaning. The project may be in English, Arabic, or any language. Your job is to understand it deeply so you can produce compelling Arabic output in Step 2.

## What to look for

Read these in priority order:

1. **`index.html`** — the primary source. Read the full file. Extract: page title, hero headline, tagline, all section headings, CTA text, testimonial copy, nav items. This is the voice and story of the app.

2. **`styles.css`** or equivalent — extract: primary color palette (look for CSS custom properties / `:root` vars), font families, background colors, accent colors. These become the visual identity of the brag video.

3. **`README.md`** — if present, extract: project name, one-line description, any listed features.

4. **`package.json`** — if present, extract: `name`, `description`.

5. **Subdirectory files** — if this is a multi-page app, scan route files, component files, or page files. Extract key feature names and screen descriptions.

6. **The user flow / happy path** — scan beyond marketing pages. The brag's strongest material is usually the product *in use*, not the product's marketing of itself. Look at:
   - **Routes** (`app/`, `pages/`, route files) — the screens beyond the landing page.
   - **Key feature components** — the upload form, the editor, the result view, the dashboard.
   - **State machines, stores, or step components** — how a session progresses.
   - **README "how it works" or "usage" sections** — the project's own description of the flow.
   - **Example or demo folders** — sample inputs and outputs the team tested with.

   Identify the 2–3 beats of *using* the product: **entry → key action → result.**

7. **`public/` or `assets/`** — note any images, logos, icons. These can be referenced in the composition.

## The 9-question rubric

After reading, answer all nine. Write these down before moving to Step 2. Keep answers in English (this is internal agent reasoning).

```
1. What is the app?
   One sentence. What does it actually do (or claim to do)?

2. What is the funniest or most impressive claim?
   The one line from the site that earns a reaction.

3. What is the visual hook?
   The strongest CSS visual: a color palette moment, a UI element, a diagram, a card.

4. What should be shown from the actual UI?
   Which section of the site has the most video-worthy content?
   (Hero? Feature section? Testimonial? The UI mockup?)

5. What is the shortest satisfying video?
   Would 15 seconds work? 20? What's the minimum to land the joke/claim?

6. What tone fits best?
   If the user specified a preset, use it.
   If the user gave freeform direction, preserve it and map it to the nearest preset.
   If the user did not specify, infer both:
   - Tone preset: one of the known presets
   - Creative direction: a short custom phrase for this project
   Examples:
   - Absurd product → preset: yc-parody; direction: fake startup launch
   - Earnest product → preset: polished; direction: quiet confidence

7. What is the product's strongest claim, rewritten in Arabic?
   Take the answer to question 2 and craft a compelling Arabic version.
   This is NOT a translation — it's a reimagining in Arabic that preserves the
   punch while sounding natural. Consider the selected dialect.

8. What is the Arabic hook line?
   The opening 2-3 words or phrase in Arabic that earns the next 20 seconds.
   This is the most important piece of Arabic copy in the entire video.

9. What is the user flow worth showing?
   The 2–3 beats of *using* the product: entry → key action → result.
   If the project is landing-page-only, write "none — landing-page only."
```

Questions 7 and 8 are specific to the Arabic version — they ensure you're not just translating but creating original Arabic copy that hits as hard as (or harder than) English.
