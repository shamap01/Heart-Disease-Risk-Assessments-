from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Define the input page
@app.route('/')
def input_page():
    return render_template('input.html')

# Define the prediction page
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    age = float(request.form['age'])
    blood_pressure = float(request.form['blood_pressure'])
    cholesterol = float(request.form['cholesterol'])

    # Create a dataframe with the input data
    input_data = pd.DataFrame([[age, blood_pressure, cholesterol]], columns=['age', 'blood_pressure', 'cholesterol'])

    # Standardize the input data
    input_data = scaler.transform(input_data)

    # Apply the machine learning model to the input data
    risk = rf.predict(input_data)

    # Display the predicted risk
    return render_template('prediction.html', risk=risk[0])

# Run the
