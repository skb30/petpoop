from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="development-key",
    WTF_CSRF_SECRET_KEY="development-key"
))

#
# app.config['SECERT_KEY'] = 'development-key'
# app.secert_key = "development-key"


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password')


@app.route('/form', methods=['GET', 'POST'])
def form():
   form = LoginForm()
   if form.validate_on_submit():
         return "<h1> username: {}. password: {}".format(form.username.data, form.password.data)
   return render_template('test-form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
