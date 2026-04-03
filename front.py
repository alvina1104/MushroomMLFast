import streamlit as st
import requests

st.title("🍄 Mushroom Classifier")

cap_shape = st.selectbox("Cap shape", ["b","c","f","k","s","x"])
cap_surface = st.selectbox("Cap surface", ["f","g","s","y"])
cap_color = st.selectbox("Cap color", ["b","c","e","g","n","p","r","u","w","y"])
bruises = st.selectbox("Bruises", ["f","t"])
odor = st.selectbox("Odor", ["a","c","f","l","m","n","p","s","y"])
gill_attachment = st.selectbox("Gill attachment", ["a","f"])
gill_spacing = st.selectbox("Gill spacing", ["c","w"])
gill_size = st.selectbox("Gill size", ["b","n"])
gill_color = st.selectbox("Gill color", ["b","e","g","h","k","n","o","p","r","u","w","y"])
stalk_shape = st.selectbox("Stalk shape", ["e","t"])
stalk_root = st.selectbox("Stalk root", ["b","c","e","r","?"])
stalk_surface_above_ring = st.selectbox("Stalk surface above ring", ["f","k","s","y"])
stalk_surface_below_ring = st.selectbox("Stalk surface below ring", ["f","k","s","y"])
stalk_color_above_ring = st.selectbox("Stalk color above ring", ["b","c","e","g","n","o","p","w","y"])
stalk_color_below_ring = st.selectbox("Stalk color below ring", ["b","c","e","g","n","o","p","w","y"])
veil_type = st.selectbox("Veil type", ["p","u"])
veil_color = st.selectbox("Veil color", ["n","o","w","y"])
ring_number = st.selectbox("Ring number", ["n","o","t"])
ring_type = st.selectbox("Ring type", ["e","f","l","n","p"])
spore_print_color = st.selectbox("Spore print color", ["b","h","k","n","o","r","u","w","y"])
population = st.selectbox("Population", ["a","c","n","s","v","y"])
habitat = st.selectbox("Habitat", ["d","g","l","m","p","u","w"])

if st.button("Predict"):
    data = {
        "cap_shape": cap_shape, "cap_surface": cap_surface,
        "cap_color": cap_color, "bruises": bruises,
        "odor": odor, "gill_attachment": gill_attachment,
        "gill_spacing": gill_spacing, "gill_size": gill_size,
        "gill_color": gill_color, "stalk_shape": stalk_shape,
        "stalk_root": stalk_root, "stalk_surface_above_ring": stalk_surface_above_ring,
        "stalk_surface_below_ring": stalk_surface_below_ring,
        "stalk_color_above_ring": stalk_color_above_ring,
        "stalk_color_below_ring": stalk_color_below_ring,
        "veil_type": veil_type, "veil_color": veil_color,
        "ring_number": ring_number, "ring_type": ring_type,
        "spore_print_color": spore_print_color,
        "population": population, "habitat": habitat
    }
    result = requests.post("http://127.0.0.1:8000/predict", json=data).json()

    if result["result"] == "poisonous":
        st.error("☠️ Уулуу — Poisonous")
    else:
        st.success("✅ Жеңил — Edible")