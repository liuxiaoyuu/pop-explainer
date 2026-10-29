# Evals

No model calls — you run the skill, save the reply, then check it.

1. Install the skill and open a fresh session.
2. Send each prompt from `prompts.md`; save each reply as `out/P1.md` … `out/P5.md`.
3. Structural check:

   ```bash
   python3 evals/check_story.py out/P1.md --terms "均值回归,regression to the mean,回归"
   ```

4. Read each reply against `expected.md`: is the core idea right, does the turn come from reasoning, is the quiz in a different world, did P5 give rules instead of a story?

`check_story.py` can't tell whether a story is clear or correct — only a reader can. The best test: give the story and the "This is called" block to someone who doesn't know the concept, and ask them to explain it back in their own words.
