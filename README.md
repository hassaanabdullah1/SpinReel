# SpinReel - A Terminal Slot Game & Probability Simulator

**SpinReel** is a simple yet engaging terminal-based slot game written in Python. It also includes a simulation tool to analyze the probability of winning based on randomly drawn symbols.

This project is great for beginners learning Python, game logic, randomness, and basic simulations.

---

## 🕹️ Gameplay Overview

- Choose how many "slots" (symbols) you want.
- Spin the reels!
- If all symbols match — you **win** 🎉. Otherwise, try again.
- The game tracks total wins and losses.
- After you finish playing, a summary is displayed with your win rate.

---

## 📁 Project Structure

```

SpinReel/
│
├── SpinReel.py       # Core game logic
├── main.py           # Entry point to play the game
├── test.py           # Run large-scale simulation to analyze win rate
└── README.md         # This file

````

---

## ✅ Requirements

- Python 3.7+
- No external libraries needed (uses only built-in modules like `random`& `sys`)

---

## 🚀 How to Play the Game

1. Clone the repository:
   ```bash
   git clone https://github.com/hassaanabdullah1/spinreel.git
   cd spinreel

2. Run the game:

   ```bash
   python main.py
   ```

3. Follow the prompts in your terminal:

   * Choose to play or exit.
   * Select how many slot symbols you want.
   * Spin the reels and see if you win!

---

## 🧪 Running the Probability Simulation

Want to know how likely it is to win?

1. Run the simulation script:

   ```bash
   python test.py
   ```

2. It simulates millions of spins with a given slot size and calculates:

   * Total wins
   * Total losses
   * Win percentage
   * Time taken for the simulation

You can adjust the number of spins and slot count directly in the script by modifying these variables:

```python
SLOTS = 7           # Number of slot icons per spin
GAMES = 10_000_000  # Number of simulated games
```

---

## 🧠 How the Game Works

* There are 7 unique symbols: `$`, `%`, `@`, `#`, `?`, `*`, `&`
* Each spin randomly selects symbols (with replacement)
* Win condition: all selected symbols must match
* Probability of winning with 7 slots:
  [
  P(\text{win}) = \frac{1}{7^6} \approx 0.0000587 \ (≈ 0.00587%)
  ]

This rare win rate makes it exciting!

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🤝 Contributions

Pull requests are welcome! If you'd like to improve the game or add features, feel free to fork the project and submit a PR.

---

## 🙋‍♂️ Author

Created by [hassaanabdullah1]
