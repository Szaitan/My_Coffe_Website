from flask import Flask, render_template, request, url_for, flash, abort
import os
from datetime import datetime
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('app_secret_key')
Bootstrap(app)
this_year = datetime.today().year

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Table config
class Cafe(db.Model):
    __tablename__ = "cafe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, primary_key=True)
    map_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    has_sockets = db.Column(db.Integer, nullable=False)
    has_toilet = db.Column(db.Integer, nullable=False)
    has_wifi = db.Column(db.Integer, nullable=False)
    can_take_calls = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    coffee_price = db.Column(db.Integer, nullable=False)


@app.route('/')
def cover():
    return render_template("cover_page.html", this_year=this_year)


@app.route('/london')
def london_page():
    # db.create_all()
    coffee_shops = Cafe.query.all()
    num = len(coffee_shops)
    return render_template("london.html", coffee_shops=coffee_shops, num=num)


@app.route('/london', methods=["GET", "POST"])
def filter_london_page():
    socket_value = request.form.get('Sockets')
    toilet_value = request.form.get('Toilet')
    wifi_value = request.form.get('Wi-Fi')
    calls_value = request.form.get('Calls')

    filter_list = [socket_value, toilet_value, wifi_value, calls_value]
    list_to_use = ""
    for num in filter_list:
        if num is None:
            num = "0"
        list_to_use += num

    filtr_dict = {"0000": Cafe.query.all(),
                  "1000": db.session.query(Cafe).filter_by(has_sockets=list_to_use[0]).all(),
                  "0100": db.session.query(Cafe).filter_by(has_toilet=list_to_use[1]).all(),
                  "0010": db.session.query(Cafe).filter_by(has_wifi=list_to_use[2]).all(),
                  "0001": db.session.query(Cafe).filter_by(can_take_calls=list_to_use[3]).all(),
                  "1100": db.session.query(Cafe).filter_by(has_sockets=list_to_use[0],
                                                           has_toilet=list_to_use[1]).all(),
                  "1010": db.session.query(Cafe).filter_by(has_sockets=list_to_use[0], has_wifi=list_to_use[2], ).all(),
                  "1001": db.session.query(Cafe).filter_by(has_sockets=list_to_use[0],
                                                           can_take_calls=list_to_use[3]).all(),
                  "0101": db.session.query(Cafe).filter_by(has_toilet=list_to_use[1],
                                                           can_take_calls=list_to_use[3]).all(),
                  "0011": db.session.query(Cafe).filter_by(has_wifi=list_to_use[2],
                                                           can_take_calls=list_to_use[3]).all(),
                  "1110": db.session.query(Cafe).filter_by(has_sockets=list_to_use[0], has_toilet=list_to_use[1],
                                                           has_wifi=list_to_use[2]).all(),
                  "1011": db.session.query(Cafe).filter_by(has_sockets=list_to_use[0], has_wifi=list_to_use[2],
                                                           can_take_calls=list_to_use[3]).all(),
                  "1101": db.session.query(Cafe).filter_by(has_sockets=list_to_use[0], has_toilet=list_to_use[1],
                                                           can_take_calls=list_to_use[3]).all(),
                  "0111": db.session.query(Cafe).filter_by(has_toilet=list_to_use[1],
                                                           has_wifi=list_to_use[2],
                                                           can_take_calls=list_to_use[3]).all(),
                  "1111": db.session.query(Cafe).filter_by(has_sockets=list_to_use[0], has_toilet=list_to_use[1],
                                                           has_wifi=list_to_use[2], can_take_calls=list_to_use[3]).all()
                  }

    filltred_data = filtr_dict[list_to_use]
    num = len(filltred_data)
    return render_template("london.html", coffee_shops=filltred_data, num=num)


if __name__ == "__main__":
    app.run(debug=True)
