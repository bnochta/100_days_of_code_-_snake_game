# 🐍 Snake Game

A classic Snake game built with Python's `turtle` module. This project is part of my **100 Days of Code** challenge — Day 20.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![100DaysOfCode](https://img.shields.io/badge/100DaysOfCode-Day%2020-orange)

## About

A simple recreation of the classic Snake arcade game. Control the snake with the arrow keys, eat the food to grow longer, and try to survive as long as possible without hitting the walls or your own tail.

## Features

- Smooth snake movement using the `turtle` graphics library
- Randomly spawning food
- Live scoreboard that updates as you eat food
- Collision detection with walls and the snake's own body
- Game over screen

## How to Play

- Use the **arrow keys** (`Up`, `Down`, `Left`, `Right`) to control the direction of the snake
- Eat the red food dots to grow and increase your score
- Avoid colliding with the walls or the snake's own tail
- The game ends and displays "GAME OVER" when a collision occurs

## Project Structure
- main.py         # Game loop and main logic
- snake.py        # Snake class: movement, growth, direction control
- food.py         # Food class: spawning and repositioning
- scoreboard.py   # Scoreboard class: score tracking and display
- .gitignore



## Built With

- [Python](https://www.python.org/) — programming language
- [turtle](https://docs.python.org/3/library/turtle.html) — built-in graphics library

## Part of 100 Days of Code

This project was built as part of the **100 Days of Code** challenge, a commitment to code every day for 100 days while building real projects to practice and improve Python skills.
