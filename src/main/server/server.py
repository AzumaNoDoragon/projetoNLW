from flask import Flask
from src.main.route.event import event_route_bp
from src.main.route.subs import subs_route_bp
from src.main.route.events_link import event_link_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)
app.register_blueprint(subs_route_bp)
app.register_blueprint(event_link_route_bp)