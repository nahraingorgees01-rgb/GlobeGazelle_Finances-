from flask import Flask, render_template, request

app = Flask(__name__)

# AI-GENERATED FUNCTION: Logic for currency calculation
def calculate_travel_budget(expenses, exchange_rate):
    total_local = sum(expenses)
    total_converted = total_local * exchange_rate
    return round(total_converted, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            raw_expenses = request.form.get('expenses')
            rate = float(request.form.get('rate'))
            # Split string by comma and convert to numbers
            expense_list = [float(x.strip()) for x in raw_expenses.split(',')]
            result = calculate_travel_budget(expense_list, rate)
        except:
            result = "Error: Please use numbers and commas only."
    return render_template('calculator.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)