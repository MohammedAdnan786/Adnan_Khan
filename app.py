from flask import *
import views.adminbp, views.userbp

app = Flask(__name__)

app.secret_key = "abc"
app.register_blueprint(views.adminbp.admin_bp)
app.register_blueprint(views.userbp.user_bp)

@app.route('/')
def home():
    return render_template("home.html")


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

if __name__ == '__main__':
    app.run()
