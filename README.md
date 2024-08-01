```markdown
# TRPG Web Service with Generative AI

This project is a Tabletop Role-Playing Game (TRPG) web service that uses generative AI to create dynamic and interactive storytelling experiences.

## Features

- Dynamic story generation based on player actions
- Real-time interaction through a web interface
- Uses GPT-2 model for AI-driven narrative creation

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/trpg-web-service.git
   cd trpg-web-service
   ```

2. **Set up a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install flask transformers torch
   ```

## Usage

1. **Run the Flask application:**
   ```bash
   python app.py
   ```

2. **Open a web browser and go to `http://127.0.0.1:5000/`.**

3. **Interact with the application:**
   - Enter your action in the text box and click "Submit" to see the AI-generated response.

## File Structure

- `app.py`: The Flask backend application.
- `index.html`: The frontend HTML file.
- `README.md`: Project overview and instructions.
- `LICENSE`: Project license information.
- `venv/`: Virtual environment directory.
