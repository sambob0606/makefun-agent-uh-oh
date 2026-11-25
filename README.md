# makefun-agent-uh-oh

[![make.fun · u-danu-the-agent-s-uh-oh-4c0911e4](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/sambob0606/makefun-agent-uh-oh/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/sambob0606/makefun-agent-uh-oh/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)

One word for make.fun's "The Agent's Uh-Oh" bounty: the word an agent says when it has no idea what to do. The program writes the word to `/output/entry.txt`.

> recalculating

Why this word: it is the voice every lost navigator uses, human or machine. An agent that has lost the plot does not admit it is lost — it stalls, spins, and announces it is recalculating, as if a better route is just one more pass away. It lands instantly, sounds exactly like a machine caught out mid-task, and it is not the first obvious word anyone types.

## Run it

```sh
python3 main.py
```

It writes the single word (no trailing newline) to `/output/entry.txt`, then reads it back and verifies the gate (1–99 characters, exactly one word, not blank) before exiting.
