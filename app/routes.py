from app import app

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    with open('C:/Users/WASIU/Documents/GitHub/Movies_recommender/index.html') as home:
        hp=home.read()
    return hp