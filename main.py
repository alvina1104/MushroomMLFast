from fastapi import FastAPI
import uvicorn
import joblib
from pydantic import BaseModel
import numpy as np


model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

mushrooms_app = FastAPI()

class MushroomsSchema(BaseModel):
    cap_shape: str
    cap_surface: str
    cap_color: str
    bruises: str
    odor: str
    gill_attachment: str
    gill_spacing: str
    gill_size: str
    gill_color: str
    stalk_shape: str
    stalk_root: str
    stalk_surface_above_ring: str
    stalk_surface_below_ring: str
    stalk_color_above_ring: str
    stalk_color_below_ring: str
    veil_type: str
    veil_color: str
    ring_number: str
    ring_type: str
    spore_print_color: str
    population: str
    habitat: str


# Ар бир feature үчүн мүмкүн болгон категориялар
CATEGORIES = {
    'cap_shape': ['c', 'f', 'k', 's', 'x'],
    'cap_surface': ['g', 's', 'y'],
    'cap_color': ['c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y'],
    'bruises': ['t'],
    'odor': ['c', 'f', 'l', 'm', 'n', 'p', 's', 'y'],
    'gill_attachment': ['f'],
    'gill_spacing': ['w'],
    'gill_size': ['n'],
    'gill_color': ['e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y'],
    'stalk_shape': ['t'],
    'stalk_root': ['c', 'e', 'r'],
    'stalk_surface_above_ring': ['k', 's', 'y'],
    'stalk_surface_below_ring': ['k', 's', 'y'],
    'stalk_color_above_ring': ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y'],
    'stalk_color_below_ring': ['c', 'e', 'g', 'n', 'o', 'p', 'w', 'y'],
    'veil_color': ['o', 'w', 'y'],
    'ring_number': ['o', 't'],
    'ring_type': ['f', 'l', 'n', 'p'],
    'spore_print_color': ['h', 'k', 'n', 'o', 'r', 'u', 'w', 'y'],
    'population': ['c', 'n', 's', 'v', 'y'],
    'habitat': ['g', 'l', 'm', 'p', 'u', 'w'],
}

@mushrooms_app.post("/predict")
async def predict(mushroom: MushroomsSchema):
    mushroom_dict = mushroom.dict()

    # One-hot encoding — ар бир feature үчүн автоматтык
    features = []
    for field, categories in CATEGORIES.items():
        value = mushroom_dict.get(field, '')
        features += [int(value == cat) for cat in categories]

    # Scale + predict
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)[0]

    return {
        "prediction": int(prediction),
        "result": "poisonous" if prediction == 1 else "edible"
    }



if __name__ == '__main__':
    uvicorn.run(mushrooms_app, host="127.0.0.1", port=8000)




