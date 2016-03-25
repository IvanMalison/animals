import json

from .app import app
from . import models


@app.route('/animals')
def animals():
    return json.dumps(
        [animal.as_dict for animal in models.Animal.query.all()]
    )
