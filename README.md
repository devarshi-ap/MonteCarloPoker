# Monte Carlo Poker

<div align="center">
    <p>Augmenting Thinking with Monte Carlo Simulations & Poker</p>
    <img src="https://i0.wp.com/25.media.tumblr.com/tumblr_mdpoi4Mhgh1qlggcwo2_500.gif" width="450" title="The Sting">
</div>

<br>

---


#### About Project

**> 🔮 Inspiration**:
- `MTH380 coursework` ∪ `Ocean's 11` ∪ `The Sting`

**> 💫 Goal**:
- Determine the winning percentage of every possible pocket combination across games of varying sizes

**> 🛠 Tools**: 
- Python3
- SQLite3
- MatPlotLib
- Jupyter Notebook
- Unittest
- Course-Notes

> assumptions:
> 1. *no betting or money*
>    - shouldn’t affect probabilities outside of eliminating the players involved; addressed in my next assumption
> 2. *no players would fold*

---

<br>

#### > Central Theory

***`Monte Carlo Simulation/Method`***
- Probabilistic numerical technique used to estimate outcomes of an uncertain (stochastic) process.
- Results of simulations can then be used to analyze the probabilities of certain outcomes of the event being simulated
- one can get a better understanding of the range of possible outcomes without having to actually experience each personally
- Verbatim for *Glorified Law of Large Numbers*.

<br>

#### > Why Poker?

**Poker is very much a probability-based game**- though it contains elements of psychology, heuristics, and risk taking.

The best players understand that one of the most important elements is understanding the underlying probability. There're so many different scenarios to factor in that it’s quite difficult for average poker players to get an intuitive feel for the probabilities of the game and how they may assist in making certain in-the-moment decisions.

This is what makes poker an ideal game for Monte Carlo simulation. Even if you’re an amateur player who plays the game every so often, you can still develop more of a probabilistic understanding of the game by letting a computer play the game for you millions of times, without having to do it yourself.

<br>

#### > Getting Started

1. run simulations (set `NUM_SIMULATIONS`, default 10,000)
```bash
$ python3 main.py
```
2. perform data analysis and generate graphs
```bash
$ python3 analysis.py
```