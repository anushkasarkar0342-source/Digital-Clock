
# Digital Clock Using Python and PyQt5

## Overview
A desktop digital clock application built with Python and PyQt5. It displays the current system time in a graphical window and updates every second.

## Features
- Real-time digital clock
- Black background and green text
- Custom digital font support
- Automatic time updates every second

## Technologies Used
- Python
- PyQt5
- Qt Timer
- Qt Font Database

## Installation

Install the dependency:

```bash
pip install -r requirements.txt
```

## Run the Application

Make sure `DS-DIGIT.TTF` is in the same folder as the Python script, then run:

```bash
python digital_clock.py
```

## Note
The application displays the local system time. The custom font is optional; the application falls back to the default font if it cannot load the font file.
