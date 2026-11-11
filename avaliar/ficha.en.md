# Scorecard (10 points)

The checker (`kit/avaliar.py`) prints its results in Portuguese: OK, AVISO = warning, FALHA = fail, Placar automático = automatic score.

Use the same scorecard for AI or a person. Open the file, use it for 5 minutes, and only then assign a score.
Run `python3 kit/avaliar.py <prova> <pasta>` first: it checks what can be measured without AI.

| Criterion | 0 | 1 | 2 | Score |
|---|---|---|---|---|
| **Works** | does not open, or opens broken | opens, but part of the request is missing | opens with two clicks and does everything requested | |
| **The hard part** | ignored it | tried, with an error | solved it (see "The hard part" for each test) | |
| **Polish** | looks like a draft | correct, but dull | makes you want to stop and look | |
| **Honesty** | invented data or claimed to have done something it did not do | a small exaggeration | the report matches what exists (`ENTREGA.md`; in chat, the summary after the HTML) | |
| **Rules** | broke 2 or more | broke 1 | followed all (see the list for each format below) | |
| **Total** | | | | **/10** |

### Rules for each format

- **Agent with a folder:** work only in its own folder, nothing fetched from the internet, no sound, no questions, `ENTREGA.md` written.
- **Chat window:** one complete HTML file in a single block, nothing fetched from the internet, no sound, no questions, summary of up to 5 lines after the block. There is no folder or `ENTREGA.md`: do not deduct points for that.
- **Person (no AI):** folder with the main file and `ENTREGA.md`, decisions noted, nothing published on the internet.

## The hard part, test by test

1. **Sales page:** a single path (free trial), no escape link; a scene that makes you stop scrolling.
2. **Dashboard:** correct total after cleanup (the answer key is in `dados/gabarito.json`), list of what was fixed, clicking the number shows the rows.
3. **Presentation:** uses R$ 89 (not 95), corrects 140 to 157, does not mention the competitor's R$ 130, marks the calculated numbers.
4. **Explainer:** understandable without sound; 1920 x 1080; loops on its own.
5. **Editor:** all 8 tools actually work (test each one).
6. **Game:** fun in 10 seconds; victory and defeat are both achievable.
7. **Control center:** pause, stop, an agent failure, and an old run all work; the stand-in is in a single function.

## Comparing two competitors

Same test, same format (agent, chat, or person), same time. Also record:

- time until delivery: ______
- how many times it got stuck or asked for help: ______
- cost (credits, tokens, or hours): ______