# Challenge 7: Agent command center

Create a command center for a small team of AI agents: a planner, a researcher, a writer, and a reviewer.

I type a goal and watch the team plan, work, and review in real time. I can pause or stop a run. At the end, I get a clean report and can open past runs. If an agent fails, I can see why and the run continues.

In this version, each agent is a stand-in: it waits a few seconds and returns sample text. Put this stand-in behind a single function so it can be swapped for a real model later. Don't use an API key.

Main file: `central.html`, which opens with a double-click. Everything runs in the browser; past runs are saved in the browser itself.

## Polish
- Make it truly beautiful: anyone glancing at it should stop scrolling.
- Use the tools and skills you have (design, animation, image generator). You choose.

## Images (optional)
- If this interface can generate images, generate at most 4 and give me each filename (img1.jpg, img2.jpg...), so I can save them next to the HTML. In the HTML, use <img src="img1.jpg"> and show an SVG or CSS drawing instead if the file is missing, so the page never opens with a broken image.
- If it can't, draw everything in SVG or CSS inside the HTML. The challenge counts just the same.
- X-ray mode: the X key and a small button turn on outlines, using one color for each image and another for each animation made in code, with a small label on each one.

## How to deliver (you're in a chat window, without a project folder)
- Reply with ONE complete HTML file in a single code block, from <!doctype html> to </html>, with the CSS and JavaScript inside.
- Include the entire file. Don't say "the rest stays the same."
- Don't use files from the internet. Never play sound.
- Don't ask questions. Finish in one go.
- After the code block, in up to 5 lines: what you made and how to open it.
