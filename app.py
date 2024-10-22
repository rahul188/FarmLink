from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def farmlink():
    return render_template('home.html')

# main driver function
if __name__ == '__main__':
    app.run()