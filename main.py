# coding: utf-8

from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

app = Flask(__name__, template_folder="templates")

API_KEY = "AIzaSyAeWu0zu9VchrXlJzumD3B2CPN2vLYyiPM"

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = API_KEY

# you can also pass key here
GoogleMaps(
    app,
    key=API_KEY
)


@app.route('/')
def main():
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:100%;"
            "width:100%;"
            "top:0;"
            "left:0;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "Hello I am GREEN!"
            },
            {
                'icon': '//maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "Hello I am BLUE!"
            },
            {
                'icon': icons.dots.yellow,
                'lat': 37.4500,
                'lng': -122.1350,
                'infobox': "Hello I am Yellow!"
            }
        ]
    )
    return render_template(
        'main.html',
        fullmap=fullmap,
        GOOGLEMAPS_KEY=API_KEY
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
