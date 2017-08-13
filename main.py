from flask import Flask, render_template
import rpi


app = Flask(__name__)
raspi = rpi.raspi()

# @app.route("/")
# def hello():
#     return "Hello World!"


# index route
@app.route("/")
def index():
    # read gpio value
    Value = raspi.readgpio()
    # render the html index value by passing the gpio value
    return render_template('index.html', gpio_value=Value)


# change gpio value
@app.route("/toggle_gpio_state/int:status>", methods=['POST'])
def toggle_gpio_status(status):
    # check the value of the parameter
    if not status:
        raspi.togglegpio(0)
    elif status:
        raspi.togglegpio(1)
    else:
        return ('Error', 500)

    return ('', 200)


# about route
@app.route("/about")
def about():
    # Render the about.html template
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)