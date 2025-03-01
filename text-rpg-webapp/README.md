# README for Text RPG Web Application

## Project Overview
This project is a web-based text RPG game built using Flask. It serves the game logic from the `game_logic.py` file and provides an interactive interface for users to engage with the game.

## Project Structure
```
text-rpg-webapp
├── src
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── game.js
│   ├── templates
│   │   ├── base.html
│   │   ├── game.html
│   │   └── index.html
│   ├── app.py
│   ├── game_logic.py
│   └── routes.py
├── requirements.txt
├── config.py
└── README.md
```

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd text-rpg-webapp
   ```

2. **Install dependencies**:
   Make sure you have Python and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Flask application by running:
   ```bash
   python src/app.py
   ```

4. **Access the game**:
   Open your web browser and go to `http://127.0.0.1:5000` to start playing the game.

## Features
- Interactive game interface
- Character creation and management
- Combat system with various classes and abilities
- Inventory and shop systems

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.