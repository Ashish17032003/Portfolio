from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

'''
@app.route('/thankyou.html')
def thankyou():
    return render_template('thankyou.html')

'''
'''
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{firstname},{lastname},{email},{subject}, {message}')
'''

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([firstname,lastname,email,subject,message])

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app. route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            #print(data)
            return redirect('/thankyou.html')
        except:
            return 'Did Not Save To Database'

    else:
        return 'Something went wrong. Try again!'



