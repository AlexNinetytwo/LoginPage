from flask import flash, current_app, Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models import Light

views = Blueprint('views', __name__)

def getTemp():
    return "21°C"

def getLights(roomName):
    return Light.query.filter_by(room=roomName)

@views.route('/', methods=['GET', 'POST'])
def sentToHome():
    return redirect(url_for('views.home'))

route_data = [
    {'path': '/', 'previousPage': '', 'header': 'HOME', 'template': 'menu.html', 'is_floor': False, 'floor': None},
    {'path': '/Erdgeschoss', 'previousPage': '/Home', 'header': 'ERDGESCHOSS', 'template': 'menu.html', 'is_floor': True, 'floor': 0},
    {'path': '/1.OG', 'previousPage': '/Home', 'header': '1.OG', 'template': 'menu.html', 'is_floor': True, 'floor': 1},
    {'path': '/Erdgeschoss/Flur', 'previousPage': '/Home/Erdgeschoss', 'header': 'FLUR', 'template': 'room.html'},
    {'path': '/Erdgeschoss/Wohnzimmer', 'previousPage': '/Home/Erdgeschoss', 'header': 'WOHNZIMMER', 'template': 'room.html'},
    {'path': '/Erdgeschoss/Esszimmer', 'previousPage': '/Home/Erdgeschoss', 'header': 'ESSZIMMER', 'template': 'room.html'},
    {'path': '/Erdgeschoss/Küche', 'previousPage': '/Home/Erdgeschoss', 'header': 'KÜCHE', 'template': 'room.html'},
    {'path': '/1.OG/Büro1', 'previousPage': '/Home/1.OG', 'header': 'BÜRO1', 'template': 'room.html'},
    {'path': '/1.OG/Büro2', 'previousPage': '/Home/1.OG', 'header': 'BÜRO2', 'template': 'room.html'},
    {'path': '/1.OG/Herrenzimmer', 'previousPage': '/Home/1.OG', 'header': 'HERRENZIMMER', 'template': 'room.html'},
    {'path': '/Alle', 'previousPage': '/Home', 'header': 'ALLE MODULE', 'template': 'room.html'},
    {'path': '/Erdgeschoss/Alle', 'previousPage': '/Home/Erdgeschoss', 'header': 'ERDGESCHOSS-ALLE', 'template': 'room.html'},
    {'path': '/1.OG/Alle', 'previousPage': '/Home/1.OG', 'header': '1.OG-ALLE', 'template': 'room.html'},
]

@views.route('/Home', methods=['GET', 'POST'])
@login_required
def home():
    house = current_app.config['home']
    return render_template('menu.html', house=house, celsius=getTemp(), header='HOME')

@views.route('/Home/<path:subpath>', methods=['GET', 'POST'])
@login_required
def dynamic_route(subpath):
    house = current_app.config['home']
    for data in route_data:
        if data['path'].lstrip('/') == subpath:
            header = data['header']
            template = data['template']
            previousPage = data['previousPage']
            is_floor = data.get('is_floor', False)
            floor = house.floors[data.get('floor', 0)] if is_floor else None
            return render_template(template,
                                   house=house,
                                   celsius=getTemp(),
                                   header=header,
                                   isFloor=is_floor,
                                   floor=floor,
                                   previousPage=previousPage,
                                   lights=getLights("Flur"))
    return redirect(url_for('views.home'))

