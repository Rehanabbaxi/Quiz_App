# Quizzler App

A modern Python-based quiz application with a graphical user interface that fetches trivia questions from the Open Trivia Database API and presents them in an interactive True/False format.

## Features

- **Dynamic Question Fetching**: Retrieves 10 random True/False questions from the Open Trivia Database API
- **Interactive GUI**: Clean, modern interface built with Tkinter
- **Real-time Feedback**: Visual feedback with color-coded responses (green for correct, red for incorrect)
- **Score Tracking**: Live score display throughout the quiz
- **HTML Entity Decoding**: Properly handles special characters in questions

## Project Structure

| File                | Description                                |
| ------------------- | ------------------------------------------ |
| `main.py`           | Entry point and API integration            |
| `question_model.py` | Defines the `Question` data model          |
| `quiz_brain.py`     | Manages quiz logic and game mechanics      |
| `ui.py`             | Implements the GUI using Tkinter           |
| `README.md`         | Project documentation (this file)          |
| `requirements.txt`  | Lists Python dependencies for the project  |
| `images/`           | Directory for image assets                 |
| `  ├── true.png`    | Image for the 'True' button                |
| `  └── false.png`   | Image for the 'False' button               |
