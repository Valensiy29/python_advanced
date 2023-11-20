from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField
from wtforms import validators
from flask_wtf.csrf import CSRFProtect


post = Flask(__name__)
csrf = CSRFProtect(post)

class Reg(FlaskForm):
    email = StringField([validators.InputRequired(),validators.Email()])
    phone = IntegerField([validators.InputRequired(),validators.NumberRange(min=1000000000,max=999999999)])
    name = StringField([validators.InputRequired()])
    address = StringField([validators.InputRequired()])
    index = IntegerField([validators.NumberRange()])
    comment =StringField()

@post.route('/cor_check', methods = ['POST'])
def array_sum():
    form = Reg()
    if form.validate_on_submit():
        email,phone = form.email.data, form.phone.data
        return email,phone
    return form.errors,400


if __name__ == '__main__':
    #post.config['WTF_CSRF_ENABLE'] = False
    post.run()
