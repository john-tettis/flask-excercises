from flask import Flask

app = Flask(__name__)

# /welcome
# Returns “welcome”
# /welcome/home
# Returns “welcome home”
# /welcome/back
# Return “welcome back”

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/<end>')
def welcome_end(end):
    return f'welcome {end}'