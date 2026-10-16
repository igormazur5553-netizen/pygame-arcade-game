# 2D Arcade Game (Pygame Architecture Case)
A lightweight 2D arcade desktop application built with Python and Pygame, demonstrating clean code principles, structured state management, and strict separation of concerns.
## 🛠 Tech Stack
- **Language:** Python 3.x
- **Framework:** Pygame
- **Database:** SQLite (Local high-scores persistence via context manager)
- **Architecture Pattern:** Model-View-Controller (MVC)
## 🚀 Key Architectural Features
- **MVC Pattern Implementation:** Clear separation between game logic (Model), rendering processes (View), and user input handling (Controller).
- **Event-Driven Architecture:** Robust handling of keyboard events, frame-rate throttling (FPS locking), and precise rectangle-based collision detection.
- **Data Persistence:** Integrated SQLite database layer utilizing native Python context managers (`with` statements) to store and manage top scores seamlessly.
- **Clean Configuration:** Global game constants and constants extraction managed through a centralized settings configuration module.
## 📦 Project Structure
```text
├── database/          # Automatically generated local SQLite DB
├── src/
│   ├── ball.py        # Ball physics, movements and boundaries logic
│   ├── block.py       # Breakable block matrix and color rendering
│   ├── database.py    # Clean SQLite data access object (DAO)
│   ├── game_stats.py  # Score metrics, lives and text rendering
│   ├── paddle.py      # User controlled paddle movement constraints
│   └── settings.py    # Centralized global constants and configurations
└── main.py            # Primary application entry point & core loop
```
## ⚙️ Installation & Launch
1. Clone the repository:
   ```bash
   git clone https://github.com/igormazur5553-netizen/pygame-arcade-game.git
   cd pygame-arcade-game
   ```

2. Run the application:
   ```bash
   python main.py
   ```
