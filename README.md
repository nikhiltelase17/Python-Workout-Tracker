## Python Workout Tracker with Nutritionix and Sheety APIs

This Python script automates logging your workout data, fetching details from the Nutritionix API and saving them to a Google Sheet using the Sheety API.

**Features:**

* **Simplified Tracking:** Tell the script your exercise, and it handles the rest.
* **Accurate Data:** Retrieves duration and calorie information directly from the Nutritionix API.
* **Convenient Storage:** Automatically sends workout data to a designated Google Sheet.

**Requirements:**

* Python 3.x
* `requests` library (install with `pip install requests`)
* Nutritionix API credentials (app ID and API key)
* Sheety API access (sheet URL and authorization header)

**Instructions:**

1. **Replace placeholders:**
    * Update `app_id`, `api_key`, and `sheet_url` with your own credentials.
    * Replace `sheet_header` value with your Sheety authorization header.
2. **Install dependencies:**
    ```bash
    pip install requests
    ```
3. **Run the script:**
    ```bash
    python main.py
    ```

**How it works:**

1. You enter the exercise you did.
2. The script sends the exercise name, weight, height, and age to the Nutritionix API.
3. The API returns detailed information about the exercise, including duration and calories burned.
4. The script formats the date and time and creates a dictionary with exercise details.
5. It sends this data to your Google Sheet using the Sheety API.

**Additional notes:**

* This script requires basic Python knowledge and understanding of APIs.
* Ensure you have internet access for the script to function.
* Consider adding error handling and user input validation for robustness.

**Feel free to contribute or ask questions!**
