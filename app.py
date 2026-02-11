from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return '''
        <h2>Temperature Converter</h2>

        <form action="/c_to_f">
            Celsius: <input name="value">
            <button type="submit">Convert to Fahrenheit</button>
        </form><br>

        <form action="/f_to_c">
            Fahrenheit: <input name="value">
            <button type="submit">Convert to Celsius</button>
        </form>
    '''

@app.route("/c_to_f")
def c_to_f():
    c = float(request.args.get("value"))
    f = (c * 9/5) + 32
    return f"Fahrenheit: {f}"

@app.route("/f_to_c")
def f_to_c():
    f = float(request.args.get("value"))
    c = (f - 32) * 5/9
    return f"Celsius: {c}"

app.run(host="0.0.0.0", port=5000)
