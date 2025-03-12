# -*- coding: utf-8 -*-
import google.generativeai as genai
import os
import re
import pandas as pd

# Set the Excel file path (Modify this path as needed)
excel_path = "/mnt/c/Users/amanm/OneDrive/Desktop/trial/course_reviews.xlsx"

# Ensure the API key is set in the environment variables
if 'GEMINI_API_KEY' not in os.environ:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit(1)

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-pro-latest')

def normalize_course_code(course_code):
    """
    Normalizes course code by converting to uppercase, removing spaces and special characters.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', course_code.upper())

def generate_course_summary():
    """
    Generates a summary for a course based on Excel data using Gemini AI.

    Returns:
        str: Generated summary if successful, error message if unsuccessful.
    """
    try:
        # Load and process Excel file
        df = pd.read_excel(excel_path)

        # Get course ID input
        course_id = input("Enter the course ID to filter: ").strip()
        normalized_course_id = normalize_course_code(course_id)

        # Normalize course names in dataframe
        df['Normalized_Course_Name'] = df['Course Name'].fillna('').apply(normalize_course_code)

        # Filter rows
        filtered_rows = df[df['Normalized_Course_Name'].str.startswith(normalized_course_id, na=False)]

        if filtered_rows.empty:
            return f"No such course with ID '{course_id}' available in the database."

        # Create paragraph from filtered data
        paragraph = "\n".join(
            " | ".join(f"{col}: {row[col]}" for col in df.columns if col != 'Normalized_Course_Name')
            for _, row in filtered_rows.iterrows()
        )

        # Generate prompt for Gemini
        prompt = f"""
        The following is data about a course:

        {paragraph}

        Task: Please provide a concise summary of this course information in a single flowing paragraph without bullet points or sections. 
        Include key details about the course name, content, instructor, evaluation methods, and student feedback.
        """

        # Generate and return summary
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    # Check if the file exists before running
    if not os.path.exists(excel_path):
        print(f"Error: The file '{excel_path}' does not exist.")
        exit(1)

    summary = generate_course_summary()
    print("\nSummary:\n", summary)
