from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret123"  # needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name:
            flash("Name is required!")
            return redirect(url_for('contact'))

        flash("Form submitted successfully!")
        return redirect(url_for('home'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)