# pop-explainer（梗讲师）

**English** | [中文](README.zh-CN.md)

**Teach any concept with a misconception-reversal story.** An agent skill for Claude Code, Codex and other tools that support the Agent Skills format.

Ask "explain X" and you get one short, complete story: the hero believes the most common wrong idea about X, acts on it, and then *works out* why it's wrong. Then the concept's name, one warning, and a quiz set in a different world — answer withheld until you try.

> **The twist must come from figuring it out, never from a lucky reveal.** No culprit is caught, no result is announced: the turn is a question, a comparison or a count you can follow. You learn the reasoning, not the ending.

## See it in action

**You:** explain regression to the mean like a story

> **🎬 The Story**
>
> Fang runs a noodle shop that does delivery only. Every night before bed she checks the day's average rating. It usually sits around 4.6 (all numbers made up).
>
> One day it dropped to 4.1, and she stormed into the kitchen and chewed out her chef, Song. The next day it was back at 4.5. Another day it shot up to 4.9, and she happily sent Song a 200-yuan bonus. The next day it slid back to 4.6.
>
> After a few rounds of this, Fang had her rule: "Bonuses make people sloppy. Yelling is what works."
>
> Then she went away on a two-week supply trip and left her cousin Yu in charge. Yu is a softie. In two weeks she never yelled at anyone and never handed out a bonus.
>
> When Fang got back she went through the records, and stopped short. Of the 4 worst days in those two weeks, 3 were followed by a better day. Of the 4 best days, 3 were followed by a worse one. No yelling, no bonuses, and the exact same pattern.
>
> She opened the bad reviews from the worst days one by one. One day a rainstorm made every rider late and the noodles arrived soggy. One day a power cut next door threw the kitchen into chaos. And the best day? Cool weather, few orders, every rider on time.
>
> Song's cooking hadn't changed at all in those two weeks. What changed was each day's luck. A really low day was usually Song cooking as normal and just happening to get hit by bad luck. But it doesn't storm every day, so the next day's luck went back to ordinary and the score drifted back toward 4.6. The really high days worked the same way: good luck doesn't promise to show up two days in a row.
>
> Fang put her phone face down. "Every time I yelled, I was yelling right after the unluckiest day. The score came back because the luck came back, not because I yelled it back."
>
> **💡 This is called: Regression to the mean**
>
> An unusually good or bad result usually has a big chunk of luck mixed in. Next time the luck is probably ordinary again, so the result drifts back toward the usual level, without anyone doing anything. Like in the story: while Yu was in charge, nobody yelled and nobody got a bonus, and the worst days were still followed by better ones. The Victorian scientist Francis Galton first noticed it when comparing the heights of parents and their children.
>
> **⚠️ Don't Mix It Up**
>
> It isn't "what goes up must come down." No force is pulling the score back; only the luck part goes back to normal. If Song's cooking had really got worse, the score would stay low and never come back by itself.
>
> **🤔 Your Turn**
>
> The city put speed cameras at the three intersections that had the most crashes last year, and this year all three had fewer crashes. Does that show the cameras work? What would you want to check first?
>
> Tell me what you think and I'll pick it up from there. Want the answer straight away? Reply /answer

What to notice: Fang acts on the misconception (she yells, she stops giving bonuses); the twist is a comparison — two weeks with nobody yelling show the same bounce — plus a count, not a reveal; the term appears only once, after the story; the quiz moves from a noodle shop to traffic cameras. Full example: [`regression-to-the-mean.en.md`](skills/pop-explainer/examples/regression-to-the-mean.en.md).

<details>
<summary><b>What happens when you answer the quiz</b></summary>

- **Right:** it names the key point you caught and ties it back: "same idea as the story: the luck came back, not the yelling."
- **Right verdict, wrong reason** (the most common case): it confirms the verdict, then uses a moment from the story to lead you to the real mechanism.
- **Not there yet:** it never says "wrong" — it replays one beat of the story as a hint and lets you try again. After a second miss it gives the answer kindly and moves on.

</details>

### More examples

- **Prisoner's dilemma** (game theory) — two neighbouring parents both sign their kids up for weekend maths classes to win the school's one science-camp place; the ranking doesn't move and both lose the money and their Sundays. The turn is two questions — "would you sign up if she hadn't? if she had?" — then "what did she work out at her table?" Overturns "it went wrong because she's selfish". → [`prisoners-dilemma.en.md`](skills/pop-explainer/examples/prisoners-dilemma.en.md)

- **Self-fulfilling prophecy** (sociology, Merton; in Chinese) — someone posts "the ribs will run out today" in the dorm chat; everyone buys extra and the ribs do run out. The turn is two questions and a count (same 300 portions as last week, when they lasted until 1pm; 40-odd extra bought on one floor alone). Overturns "it came true, so the predictor saw it coming". → [`self-fulfilling-prophecy.zh.md`](skills/pop-explainer/examples/self-fulfilling-prophecy.zh.md)
- **Veil of ignorance** (philosophy, Rawls; in Chinese) — four roommates agree how to split a sweet-potato stall's takings *before* drawing lots for the worst job. The turn is one question: "if I draw the worst job, which split leaves me better off?" Overturns "fair means equal shares", and ⚠️ notes it's a thought experiment whose conclusion is contested. → [`veil-of-ignorance.zh.md`](skills/pop-explainer/examples/veil-of-ignorance.zh.md)

## Output shape

```
🎬 Story            300–500 Chinese characters (≈200–400 English words), no jargon
💡 This is called   the name, once, tied back to the story
⚠️ Don't mix it up  the one thing most likely to mislead
📌 One-liner        only when you mention an interview, exam, thesis or report
🤔 Your turn        a quiz in a different setting — answer withheld
```

Follow-ups: `/answer` `/deeper` `/retell` `/simpler` `/quiz` `/comic` `/compare` (Chinese: `/答案` `/深挖` `/换故事` `/更简单` `/考我` `/漫画` `/对比`), or just say "still don't get it" / "quiz me".

## Install

```bash
git clone https://github.com/liuxiaoyuu/pop-explainer.git
cp -R pop-explainer/skills/pop-explainer ~/.claude/skills/   # Claude Code
cp -R pop-explainer/skills/pop-explainer ~/.codex/skills/    # Codex
```

Other tools that support Agent Skills: copy `skills/pop-explainer/` into that tool's skills directory (check its docs). With the open-source `skills` CLI: `npx skills add liuxiaoyuu/pop-explainer`. Start a new session afterwards.

More on the design, the learning research behind it, and the accuracy guardrails: [`skills/pop-explainer/README.md`](skills/pop-explainer/README.md).

## Test it

`evals/prompts.md` lists five prompts (including one that must *not* get a story — a personal medication question). `evals/expected.md` says what a good answer must do; `evals/check_story.py` checks the structure:

```bash
python3 evals/check_story.py out/P2.md --terms "p-value,null hypothesis,significance"
```

## Languages

The instructions are written in Chinese; the skill answers in whatever language you write in.

## Companion skills

Reading research papers? See [**scholar-screen-skills**](https://github.com/liuxiaoyuu/scholar-screen-skills): `paper-triage` (is this paper worth reading?) and `methods-decomposer` (what does this paper's design actually identify?). pop-explainer works on its own; it just points you there when your question is about a specific paper.

## License

MIT — see `LICENSE`. Citation: `CITATION.cff`. Provenance: `PROVENANCE.md`.
