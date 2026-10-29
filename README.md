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

### More examples: game theory, sociology, philosophy

<details>
<summary><b>Game theory: "what's the prisoner's dilemma?"</b> — overturns "it went wrong because she's selfish"</summary>

> 🎬 The Story
>
> Lin's daughter Xiaoman and her neighbour Mrs. Wu's son Dou are in the same class, and the two kids have been neck and neck for years. The school has exactly one place at the city science camp, and it goes to whoever ranks first in the end-of-term exams.
>
> Early in the term, Lin heard that Mrs. Wu had signed Dou up for weekend maths classes, 4,000 a term (all numbers made up). At dinner she exploded: "At the parents' meeting she said kids should have their weekends free. Now look at her. She can't stand to give an inch." The next day, Lin signed Xiaoman up too.
>
> A term later, both kids had spent every Sunday in a classroom. The rankings came out the same as always: Dou first, Xiaoman second, one point behind.
>
> Lin was winding up to complain again when her husband asked her a few questions.
>
> "Say you knew for sure Mrs. Wu hadn't signed Dou up. Would you have signed Xiaoman up?" Lin thought about it. "...Yes. Then Xiaoman would pull ahead."
>
> "And if Mrs. Wu had signed him up?" "Then I'd have to, or Xiaoman would fall behind."
>
> "So whatever Mrs. Wu does, you sign up." He paused. "Now guess what Mrs. Wu worked out at her dinner table."
>
> Lin went quiet. Mrs. Wu was facing the exact same two roads. Nobody had to be selfish: as long as each family was looking out for its own kid, both would sign up. But with both signed up, neither kid gained a place, and each family was out 4,000 and a whole term of Sundays. If neither had signed up, the ranking would have been the same, and they'd still have the money and the weekends.
>
> She turned the receipt face down on the table. "She's not a bad person, and neither am I. It's just set up so that each family makes its smartest move, and together we both lose."
>
> 💡 This is called: The prisoner's dilemma
>
> Each person makes the choice that's best for them, and added together the result is worse than if everyone had held back. Like in the story: whether or not the other family signs up, signing up is better for your own family, so both do, neither kid gets ahead, and both families lose money and weekends. The name comes from a classic thought experiment: two suspects questioned in separate rooms each do better by confessing, so both end up with longer sentences than if they'd both kept quiet.
>
> ⚠️ Don't Mix It Up
>
> What traps the two families isn't their character, it's the setup, so the way out is usually in the setup too: say, the school stops deciding everything on one ranking, or the families deal with each other long enough to see who keeps their word. A one-off encounter is the easiest trap to fall into; people who deal with each other again and again are more likely to learn to cooperate.
>
> 🤔 Your Turn
>
> Everyone in the office stays until 9 p.m., even though there isn't much work and the boss doesn't track hours; nobody wants to look lazier than their colleagues. What are the two roads in front of each person, and why does nobody leave first?
>
> Tell me what you think and I'll pick it up from there. Want the answer straight away? Reply /answer

</details>

<details>
<summary><b>Sociology: "explain the self-fulfilling prophecy"</b> — overturns "it came true, so the predictor saw it coming"</summary>

> 🎬 The Story
>
> Friday lunch at the campus canteen means the famous sweet-and-sour ribs on the second floor. Lin posted in the dorm group chat: "Heard there aren't enough ribs today — get there late and they're gone!"
>
> The chat lit up. Several people replied: "I'll grab an extra portion for my roommate, then."
>
> At 12:05 the rib counter put up a "Sold out" sign. Lin snapped a photo and posted it, grinning: "Told you. Was I right or was I right?"
>
> His roommate Nan didn't congratulate him. He just asked: "Last Friday nobody said anything. What time did the ribs sell out?"
>
> Lin thought about it. "There were still thirty-odd portions left at one o'clock."
>
> "Did the canteen make fewer this week?"
>
> "No — the server said it's three hundred portions every Friday (all numbers made up)."
>
> "Then that's odd. Three hundred portions lasted until one last week, and today they were gone by noon. Where did all the extra people come from?"
>
> Lin scrolled back through the chat and counted, one by one: extra portions for roommates, people buying two just in case... On their floor alone, more than forty extra portions had been bought.
>
> He froze. "There were enough ribs. People believed what I said and rushed to buy extra — that's what made them run out. I didn't guess right. My message made it come true."
>
> 💡 This is called: Self-fulfilling prophecy
>
> A belief that starts out false comes true because people believe it and act on it. Like in the story: there were enough ribs, until "there won't be enough" made everyone buy extra. The idea comes from the sociologist Robert K. Merton.
>
> ⚠️ Don't Mix It Up
>
> Not every prediction that comes true counts. The key question is: if nobody had believed it, would the outcome have been the same? If the canteen had only made a hundred portions, Lin would simply have been well informed — whether people believed him wouldn't matter.
>
> 🤔 Your Turn
>
> The weather forecast says "heavy rain on Saturday," and it does rain on Saturday. Someone in the residents' group chat says "the supermarket will run out of bottled water tomorrow," and the next day it does. Which one is a self-fulfilling prophecy, and why isn't the other?
>
> Tell me what you think and I'll pick it up from there. Want the answer straight away? Reply /answer

</details>

<details>
<summary><b>Philosophy: "what is Rawls's veil of ignorance?"</b> — overturns "fair means equal shares"</summary>

> 🎬 The Story
>
> In the first week of term, four roommates set up a roast sweet-potato stall outside their dorm. There are two kinds of work: one person does the roasting — up at five to pick potatoes at the wholesale market, then minding the stove all evening — and the other three take turns running the stall and taking money. Who does what will be decided by drawing lots tomorrow.
>
> Mi said: "Before we draw, let's agree how we split the money. If we wait until after, whoever draws the roasting will want more and whoever draws the stall will want equal shares, and we'll argue forever."
>
> Qing answered straight away: "Easy. Equal shares is fairest — everyone gets a quarter."
>
> Everyone nodded. Only Mi pulled out the notebook from last week's trial run (all numbers made up): "Last week we split it equally. We made 400 in a night, 100 each. But whoever was roasting felt that working harder got them nothing extra, so they picked the potatoes carelessly and didn't watch the fire, and loads got burnt. The stall next door gives the roaster a bigger cut, and they make 600 a night."
>
> She wrote two splits on a piece of paper: equal shares, where each stall-minder gets 100; or the roaster gets 180 and each stall-minder gets 140.
>
> "Forget whether it feels fair for a second. Just ask yourself: if tomorrow I draw the least rewarding job, minding the stall, which split leaves me with more?"
>
> Qing stared at the two lines of numbers for a long time, then laughed. "I thought fair meant everyone gets the same. But I don't even know what I'll draw — so the thing I should protect most is 'what if I'm the one who gets the least'. 140 beats 100. Let the roaster take more, as long as the stall-minders get more too, and I'm in."
>
> 💡 This is called: Veil of ignorance
>
> When you set the rules, imagine you don't know where you'll end up — your background, your talents, your luck, all unknown. The philosopher John Rawls argued that people reasoning for themselves in this position would first guarantee everyone the same basic liberties; and when it comes to dividing money and resources, they wouldn't insist on equal shares, but would accept inequalities that also make the worst-off better off. Like in the story: nobody knew what they'd draw, so everyone compared how much the worst share would get.
>
> ⚠️ Don't Mix It Up
>
> Allowing a gap doesn't mean any gap is fine. If the roaster got more but sales didn't improve, the stall-minders would drop to 80 each — and nobody would agree to that before the draw. Also, the veil of ignorance is a thought experiment for testing whether rules are fair, and Rawls's conclusion is contested: some argue people behind the veil would choose the rule with the highest average income rather than protect the worst-off first.
>
> 🤔 Your Turn
>
> A band has to set its rules before drawing lots for who sings lead: does the lead singer get an extra share of the gig fee, or does everyone get the same? If you don't know whether you'll draw lead singer or drummer, what's the one thing you should find out before you vote?
>
> Tell me what you think and I'll pick it up from there. Want the answer straight away? Reply /answer

</details>

What to notice: the maths-class story reaches its turn through two questions — "would you sign up if she hadn't? if she had?" — and ⚠️ says the rules trap people, not their character; the ribs story uses two questions and a count, and ⚠️ separates "came true" from "came true *because* people believed it"; the veil story turns on one "what if I draw the worst job?" and ⚠️ notes it's a contested thought experiment. Each example also exists in Chinese: `examples/*.zh.md`.

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

## License

MIT — see `LICENSE`. Citation: `CITATION.cff`. Provenance: `PROVENANCE.md`.
