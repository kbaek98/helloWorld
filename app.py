from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Katie Baek! This is my first code change.'
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    print(f'First Name: {request.args.get("first_name")}')
    print(f'Last Name: {request.args.get("last_name")}')
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/favorite-course', methods=['GET', 'POST'])
def favoritecourse():
    print(f'Subject: {request.args.get("subject")}')
    print(f'Course Number: {request.args.get("course_number")}')
    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
