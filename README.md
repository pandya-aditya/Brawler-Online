# BrawlerOnline

## Project Overview

BrawlerOnline is a multiplayer online game where players can engage in real-time battles with others over the internet. The game is built using Python and is designed to provide an engaging and interactive experience with customizable player avatars and dynamic gameplay.

## Features

- Real-time multiplayer battles.
- Customizable player avatars.
- Interactive and dynamic gameplay.
- Server-client architecture for online play.

## Installation

To get started with BrawlerOnline, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd BrawlerOnline
   ```

3. **Install the required dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

   > Note: Ensure you have all the necessary libraries installed as listed in the `requirements.txt` file.

## Usage

To start the game, you can run the `main.py` script:

```bash
python main.py
```

### Running the Server

If you want to host the game server locally, run the `server.py` script:

```bash
python server.py
```

### Connecting to a Server

The client will automatically attempt to connect to the specified server address, which can be configured in the `network.py` file.

## File Descriptions

- **`main.py`**: The main script to launch the game.
- **`network.py`**: Handles all network communication between the client and server.
- **`player.py`**: Defines the player class and related functionalities.
- **`server.py`**: Sets up and manages the game server for online multiplayer.
- **`pictures/`**: Contains game assets such as images and sprites.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes. Make sure to follow the code style guidelines and include comments for clarity.