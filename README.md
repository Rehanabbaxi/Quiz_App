# Quizzler App

A modern Python-based quiz application with a graphical user interface that fetches trivia questions from the Open Trivia Database API and presents them in an interactive True/False format.

## Features

- **Dynamic Question Fetching**: Retrieves 10 random True/False questions from the Open Trivia Database API
- **Interactive GUI**: Clean, modern interface built with Tkinter
- **Real-time Feedback**: Visual feedback with color-coded responses (green for correct, red for incorrect)
- **Score Tracking**: Live score display throughout the quiz
- **HTML Entity Decoding**: Properly handles special characters in questions

## Project Structure

quizzler-app-start/
├── main.py              # Entry point and API integration
├── question_model.py    # Question data model
├── quiz_brain.py        # Quiz logic and game mechanics
├── ui.py               # GUI implementation
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
└── images/
├── true.png        # True button image
└── false.png       # False button image
