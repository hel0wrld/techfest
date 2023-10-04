Certainly! Here's an updated `README.md` with the provided GitHub repository link.

# 🚀 TechFest Project

Welcome to the **TechFest Project** repository! This README provides detailed instructions on how to set up the project locally, create a virtual environment, install the required dependencies, and run the Flask application in debug mode.

## Prerequisites

Before you dive in, make sure you have the following prerequisites:

- Python (3.x recommended) installed on your local machine.

## 🛠️ Local Setup

To set up the project locally, follow these steps:

1. **Clone the Repository**:

   📥 Clone this repository to your local machine using the following command:

   ```bash
   git clone git@github.com:saurabhbakolia/techfest.git
   ```

2. **Navigate to the Project Directory**:

   📂 Change your working directory to the project's directory:

   ```bash
   cd techfest
   ```

3. **Create a Virtual Environment (Optional but Recommended)**:

   🌐 It's a good practice to work within a virtual environment to isolate project dependencies. Create a virtual environment using the following command:

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:

   ⚡ Activate the virtual environment based on your operating system:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**:

   📦 Use `pip` to install the project's dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

6. **Configure Environment Variables (if needed)**:

   ⚙️ If the project relies on environment variables, create a `.env` file in the project directory to store them. Update the variables as needed for your local environment.

7. **Run the Flask Application in Debug Mode**:

   🔍 Start the Flask application in debug mode using the following command:

   ```bash
   flask run --app hello --debug
   ```

   By default, the Flask app will run on `http://localhost:5000`. Open a web browser and navigate to this address to access your locally running Flask application.

8. **Access Your Application**:

   🌐 Open a web browser and navigate to `http://localhost:5000` (or the address specified by Flask). You should see your Flask application running locally.



>## Now here is an overview of the code and its functionalities.

## 🤖 Code Explanation

- `hello.py` is the main Python script that creates a Flask web application.
- We use the uagents library to create an asynchronous agent named "Alice" that periodically checks the weather for a specified location.
- The application has three API endpoints:

### 🏠 Root Endpoint (`/`)

- HTTP Method: GET
- Purpose: Serves as the main landing page for the application.

### 🌦️ `/techfest/` Endpoint

- HTTP Method: POST
- Purpose: Allows you to check the weather for a specific location. Provide a location in the POST request to get weather information.

### 🌡️ `/techfest/location/check_temperature` Endpoint

- HTTP Method: POST
- Purpose: Creates an asynchronous agent to periodically check the temperature for a specified location within a temperature range. Provide lower and upper temperature bounds in the POST request.

## 🌟 Development and Contributions

Feel free to make contributions or report issues by [creating a pull request](https://github.com/saurabhbakolia/techfest/pulls) or [opening an issue](https://github.com/saurabhbakolia/techfest/issues).

## 📜 License

This project is licensed under the [MIT License](LICENSE).
