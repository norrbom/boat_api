from flask import jsonify
from boat_api.model import ChargingStationSchema, Boat, BoatType, BoatSchema
from boat_api.providers import charging
import logging
from os import getenv

log = logging.getLogger(getenv("APP_NAME"))


def add_routes(app):
    """
    Add routes to the app
    """

    @app.route("/healthz/live")
    def liveness():
        """
        Kubernetes Liveness probe
        """
        return jsonify({"status": 200})

    @app.route(
        "/api/v1/stations/<int:radius>/<float:longitude>,<float:latitude>",
        methods=["GET"],
    )
    def stations(radius: int, longitude: float, latitude: float):
        """
        Returns nearby charging stations
        """
        stations = charging.nearby_stations(radius, longitude, latitude)
        schema = ChargingStationSchema(many=True)
        return jsonify(schema.dump(stations))
    
    @app.route("/api/v1/boat", methods=["POST"])
    def add_boat():
        boat = Boat(
            name="Kalle",
            type=BoatType.C8_DC,
            owner="Kalle Anka"
        )
        schema = BoatSchema()
        return jsonify(schema.dump(boat)), 201
    
    @app.route("/api/v1/boat/type/<boat_type>", methods=["GET"])
    def get_boat_by_type(boat_type: str):
        boats = [
            Boat(
                name=f"{boat_type}_{i}", type=BoatType.C8_DC, owner="Kalle Anka"
            )
            for i in range(10)
        ]
        schema = BoatSchema(many=True)
        return jsonify(schema.dump(boats)), 200
    
    @app.route("/api/v1/boat/", methods=["GET"])
    def get_boats():
        boats = [
            Boat(
                name=f"boat_{i}", type=BoatType.C8_DC, owner="Kalle Anka"
            )
            for i in range(10)
        ]
        schema = BoatSchema(many=True)
        return jsonify(schema.dump(boats)), 200
    
    @app.route("/api/v1/boat", methods=["PUT"])
    def update_boat():
        boat = Boat(
            name="Kalle", type=BoatType.C8_DC, owner="Kalle Anka"
        )
        schema = BoatSchema()
        return jsonify(schema.dump(boat)), 200
