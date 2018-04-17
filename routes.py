from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User, Place, PetProfile
from forms import SignupForm, LoginForm, AddressForm, PetProfileForm
from wtforms import DateField
from datetime import date

import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:hje00sb@localhost/learningflask'
db.init_app(app)
app.config.update(dict(
    SECRET_KEY="development-key",
    WTF_CSRF_SECRET_KEY="development-key"
))
app.secert_key = "development-key"
app.config['secert_key'] = 'development-key'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup", methods=['GET','POST'])
def signup():
    try:
        if 'email' in session:
            return redirect(url_for('home'))
        form = SignupForm()

        if request.method == 'POST':
            if form.validate() == False:
                return render_template('signup.html', form=form)
            else:
                newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
                db.session.add(newuser)
                db.session.commit()

                session['email'] = newuser.email
                return redirect(url_for('home'))
        elif request.method == "GET":
            return render_template('signup.html', form=form)
    except:
        return redirect(url_for('login'))

@app.route("/petprofile", methods=['GET','POST'])
def petprofile():
    # if 'email' in session:
    #     return redirect(url_for('home'))
    form = PetProfileForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('pet-profile.html', form=form)
        else:
            petProfile = PetProfile(form.first_name.data, form.last_name.data, form.email.data, form.dropOffDate.data, form.dropOffTime.data)
            db.session.add(petProfile)
            db.session.commit()

            return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template('pet-profile.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    form = LoginForm()

    if request.method == "POST":
        if form.validate() == "False":
            return render_template("login.htm", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('signup'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)
def about():
    return render_template("about.html")

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route("/home", methods=["GET", "POST"])
def home():
    if 'email' not in session:
        return redirect(url_for('login'))

    form = AddressForm()

    places = []
    my_coordinates =(37.4221, -122.0844)
    if request.method == 'POST':
        if form.validate == 'FALSE':
            return render_template('home.html', form=form)
        else:
            # get the address
            address = form.address.data

            # query for placess around it
            p = Place()
            my_coordinates = p.address_to_latlng(address)
            places = p.query(address)

            # return those results
            return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)
    elif request.method == 'GET':
        return render_template("home.html", form=form, my_coordinates=my_coordinates, places=places)

if __name__ == "__main__":
    app.run(debug=True)
