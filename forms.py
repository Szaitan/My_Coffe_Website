from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL, NumberRange


class CreateAddForm(FlaskForm):
    name = StringField("Coffe Shop Name", validators=[DataRequired()])
    map_url = StringField("Shop Location URL", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Shop Address", validators=[DataRequired()])
    has_sockets = SelectField("Has Sockets", choices=[(1, "Yes"), (0, "No")], validators=[DataRequired()])
    has_toilet = SelectField("Has Free Toilets", choices=[(1, "Yes"), (0, "No")], validators=[DataRequired()])
    has_wifi = SelectField("Has Free Wi-Fi", choices=[(1, "Yes"), (0, "No")], validators=[DataRequired()])
    can_take_calls = SelectField("Can take calls inside", choices=[(1, "Yes"), (0, "No")], validators=[DataRequired()])
    seats = SelectField("Number of seats", choices=[("0-10", "0-10"), ("10-20", "10-20"), ("20-30", "20-30"),
                                                    ("30-40", "30-40"), ("40-50", "40-50"), ("50+", "50+")],
                        validators=[DataRequired()])
    coffee_price = IntegerField("Coffe Price", validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField("Add CoffeShop")
