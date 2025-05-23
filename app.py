from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Simple in-memory storage for now (we'll add MongoDB later)
survey_data = []


@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Healthcare Survey</title>
        <style>
            body { font-family: Arial; margin: 50px; background: #f0f8ff; }
            .container { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #2c3e50; text-align: center; }
            .btn { background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; }
            .btn:hover { background: #2980b9; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🏥 Healthcare Survey Tool</h1>
            <p>Help us understand healthcare spending patterns!</p>
            <a href="/survey"><button class="btn">Start Survey</button></a>
            <br><br>
            <a href="/results"><button class="btn">View Results</button></a>
        </div>
    </body>
    </html>
    '''


@app.route('/survey')
def survey():
    return '''
    <html>
    <head>
        <title>Healthcare Survey Form</title>
        <style>
            body { font-family: Arial; margin: 50px; background: #f0f8ff; }
            .container { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #2c3e50; text-align: center; }
            .form-group { margin: 20px 0; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input, select { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
            .btn { background: #27ae60; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; width: 100%; }
            .btn:hover { background: #229954; }
            .expense-item { background: #f8f9fa; padding: 15px; margin: 10px 0; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📋 Survey Form</h1>
            <form action="/submit" method="POST">
                <div class="form-group">
                    <label>Age:</label>
                    <input type="number" name="age" min="18" max="100" required>
                </div>

                <div class="form-group">
                    <label>Gender:</label>
                    <select name="gender" required>
                        <option value="">Select Gender</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>Total Annual Income ($):</label>
                    <input type="number" name="total_income" min="0" required>
                </div>

                <h3>💰 Annual Expenses</h3>

                <div class="expense-item">
                    <label>
                        <input type="checkbox" name="categories" value="utilities"> Utilities
                    </label>
                    <input type="number" name="utilities" placeholder="Enter amount" min="0">
                </div>

                <div class="expense-item">
                    <label>
                        <input type="checkbox" name="categories" value="entertainment"> Entertainment
                    </label>
                    <input type="number" name="entertainment" placeholder="Enter amount" min="0">
                </div>

                <div class="expense-item">
                    <label>
                        <input type="checkbox" name="categories" value="school_fees"> School Fees
                    </label>
                    <input type="number" name="school_fees" placeholder="Enter amount" min="0">
                </div>

                <div class="expense-item">
                    <label>
                        <input type="checkbox" name="categories" value="shopping"> Shopping
                    </label>
                    <input type="number" name="shopping" placeholder="Enter amount" min="0">
                </div>

                <div class="expense-item">
                    <label>
                        <input type="checkbox" name="categories" value="healthcare"> Healthcare
                    </label>
                    <input type="number" name="healthcare" placeholder="Enter amount" min="0">
                </div>

                <button type="submit" class="btn">Submit Survey</button>
            </form>
        </div>
    </body>
    </html>
    '''


@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    data = {
        'age': request.form['age'],
        'gender': request.form['gender'],
        'total_income': request.form['total_income'],
        'utilities': request.form.get('utilities', 0),
        'entertainment': request.form.get('entertainment', 0),
        'school_fees': request.form.get('school_fees', 0),
        'shopping': request.form.get('shopping', 0),
        'healthcare': request.form.get('healthcare', 0)
    }

    # Store data
    survey_data.append(data)

    return '''
    <html>
    <head>
        <title>Thank You</title>
        <style>
            body { font-family: Arial; margin: 50px; background: #f0f8ff; text-align: center; }
            .container { max-width: 600px; margin: auto; background: white; padding: 30px; border-radius: 10px; }
            h1 { color: #27ae60; }
            .btn { background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; margin: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✅ Thank You!</h1>
            <p>Your survey has been submitted successfully!</p>
            <a href="/"><button class="btn">Back to Home</button></a>
            <a href="/survey"><button class="btn">Submit Another</button></a>
        </div>
    </body>
    </html>
    '''


@app.route('/results')
def results():
    if not survey_data:
        return '''
        <html>
        <body style="font-family: Arial; margin: 50px; text-align: center;">
            <h1>No Data Yet</h1>
            <p>No survey responses have been submitted yet.</p>
            <a href="/survey"><button style="background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 5px;">Take Survey</button></a>
        </body>
        </html>
        '''

    # Simple results display
    total_responses = len(survey_data)
    avg_age = sum(int(d['age']) for d in survey_data) / total_responses

    results_html = f'''
    <html>
    <head>
        <title>Survey Results</title>
        <style>
            body {{ font-family: Arial; margin: 50px; background: #f0f8ff; }}
            .container {{ max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; }}
            h1 {{ color: #2c3e50; text-align: center; }}
            .stat {{ background: #ecf0f1; padding: 15px; margin: 10px 0; border-radius: 5px; }}
            .btn {{ background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 5px; margin: 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Survey Results</h1>
            <div class="stat">
                <strong>Total Responses:</strong> {total_responses}
            </div>
            <div class="stat">
                <strong>Average Age:</strong> {avg_age:.1f} years
            </div>
            <a href="/"><button class="btn">Back to Home</button></a>
            <a href="/export"><button class="btn">Export CSV</button></a>
        </div>
        </body>
    </html>
    '''
    return results_html


@app.route('/export')
def export_csv():
    if not survey_data:
        return "No data to export"

    # Create CSV content
    import csv
    import io

    output = io.StringIO()
    writer = csv.writer(output)

    # Write header
    writer.writerow(
        ['age', 'gender', 'total_income', 'utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare'])

    # Write data
    for data in survey_data:
        writer.writerow([
            data['age'], data['gender'], data['total_income'],
            data['utilities'], data['entertainment'], data['school_fees'],
            data['shopping'], data['healthcare']
        ])

    # Save to file
    with open('survey_data.csv', 'w', newline='') as f:
        f.write(output.getvalue())

    return '''
    <html>
    <body style="font-family: Arial; margin: 50px; text-align: center;">
        <h1>✅ CSV Exported!</h1>
        <p>Data has been saved to survey_data.csv</p>
        <a href="/results"><button style="background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 5px;">Back to Results</button></a>
    </body>
    </html>
    '''


if __name__ == '__main__':
    print("🚀 Starting Healthcare Survey Tool...")
    print("📱 Open your browser and go to: http://localhost:5000")
    app.run(debug=True, port=5000)