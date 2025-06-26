# Match-momentum
This project develops a machine learning model to predict the outcome of Indian Premier League (IPL) cricket matches based on live match data. By analyzing factors like current score, required run rate, and wickets remaining, the model provides insights into the "momentum" of the match and the probability of each team winning.
## Features

*   **Real-time Predictions:** The model can provide win probability updates as the match progresses.
*   **Key Factors Analysis:** Identifies the most influential factors determining match outcomes.
*   **Interactive Visualization (Coming Soon):** Visualize match momentum swings and win probabilities over time.
## How it Works

The project utilizes a Logistic Regression model trained on historical IPL match data. The model takes various match parameters as input and outputs the predicted probability of the chasing team winning.
## Technologies Used

*   **Python:** The primary programming language used for development.
*   **Pandas:** Used for data manipulation and analysis.
*   **NumPy:** Used for numerical operations.
*   **Scikit-learn:** Used for building and training the machine learning model (Logistic Regression).
*   **Joblib:** Used for saving and loading the trained model.
*   **Jupyter Notebook/Colab:** Used for development, experimentation, and running the code.
*   **Streamlit:** Used for creating the web application interface.
*   **PyCharm:** Used for developing and deploying the application.

## Usage

1.  **Prepare your data:** Ensure you have the `DATA1.csv` and `DATA2.csv` files in the correct directory as specified in the Installation section.
2.  **Train the model (if necessary):** If the `pipe1.pkl` model file is not provided, run the training script or notebook to generate it.
3.  **Run the prediction script/notebook:** Execute the code that uses the trained model to make predictions. You will likely need to input match details (teams, city, etc.) to get a prediction.
