from flask import Flask, render_template, jsonify
import os, random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get_memes/<category>')
def get_memes(category):
    base_dir = os.path.join('static', 'photos', category)
    if not os.path.exists(base_dir):
        return jsonify([])

    images = [os.path.join(f'static/photos/{category}', file) for file in os.listdir(base_dir) if file.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    random.shuffle(images)
    print(images)
    return jsonify(images)

if __name__ == '__main__':
    app.run(debug=True)
