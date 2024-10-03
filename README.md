# Lesson Plan Generator

## Overview
The Lesson Plan Generator is a Streamlit-based web application that helps educators create comprehensive lesson plans using OpenAI's GPT model. This tool streamlines the process of lesson planning by generating structured, detailed plans based on user input.

## Features
- Interactive web interface for inputting lesson details
- Generates detailed lesson plans including learning outcomes, experiences, and assessments
- Utilizes OpenAI's GPT model for intelligent content generation
- Allows downloading of generated lesson plans in JSON format

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher installed
- An OpenAI API key (you can obtain one from [OpenAI's website](https://openai.com))

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory:
   ```
   cd path/to/lesson-plan-generator
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Setting Up the OpenAI API Key

You have two options for providing your OpenAI API key:

1. **Environment Variable (Recommended):**
   - On Windows:
     ```
     set OPENAI_API_KEY=your-api-key-here
     ```
   - On macOS or Linux:
     ```
     export OPENAI_API_KEY=your-api-key-here
     ```

2. **User Input:**
   If you don't set the environment variable, the app will prompt you to enter the API key when you run it.

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the address shown in the terminal (usually `http://localhost:8501`).

3. If you didn't set the API key as an environment variable, you'll be prompted to enter it.

4. Fill in the lesson details in the provided form:
   - Lesson Title
   - Subject
   - Grade
   - Duration
   - Key Vocabulary
   - Supporting Materials and Resources

5. Click the "Generate Lesson Plan" button.

6. Review the generated lesson plan displayed on the page.

7. Optionally, download the lesson plan as a JSON file using the provided button.

## Customization

You can customize the system message or other parameters in the `app.py` file to adjust the behavior of the lesson plan generation.

## Troubleshooting

- If you encounter any issues with the OpenAI API, ensure that your API key is correct and that you have sufficient credits.
- For any other issues, check the console output for error messages.

## Contributing

Contributions to the Lesson Plan Generator are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT model
- Streamlit for the web application framework