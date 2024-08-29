# Trivia Game

A Python-based Trivia game that uses the Open Trivia Database (opentdb) API to fetch true/false questions. The project uses Tkinter to create a simple GUI where users can answer the questions. The game tracks correct and incorrect answers and displays the results after 10 questions.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [API Used](#api-used)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Fetches trivia questions from the opentdb API.
- Simple GUI with True/False buttons for answering.
- Visual feedback for correct and incorrect answers.
- Displays the final score after 10 questions.

## Installation

### Prerequisites

- Python 3.x

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/GabrielCarp7/Trivia_Project.git
    cd Trivia_Project
    ```

2. **Install the required dependencies:**

    Tkinter and requests are included with Python, so no additional packages are needed.

3. **Run the application:**

    ```bash
    python main.py
    ```

## Usage

1. **Start the game:**

    Run the script to open the trivia game interface.

2. **Answer questions:**

    The trivia question will be displayed in the window. Click the green button if you think the answer is "True" and the red button if you think it's "False."

3. **View feedback:**

    The entire window will turn green for a correct answer and red for a wrong answer.

4. **Check your score:**

    After 10 questions, a new window will appear showing how many answers you got right and wrong.

## Technologies

- **GUI:** Tkinter
- **API Requests:** requests
- **Language:** Python

## API Used

- **[Open Trivia Database (opentdb) API](https://opentdb.com/)**: Used to fetch true/false trivia questions.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Contact

Gabriel Carp - [LinkedIn](https://www.linkedin.com/in/gabriel-carp-3b704022b/)
