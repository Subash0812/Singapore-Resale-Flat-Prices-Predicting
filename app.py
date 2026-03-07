import streamlit as st
import pandas as pd
import pickle
import numpy as np
import joblib
from variable import street_options, block_options, flat_model_options, flat_type_options, town_options, storey_options

# -------------------------
# Load Pickle Files
# -------------------------
model = pickle.load(open("Pkl Files/model.pkl", "rb"))
ohe = joblib.load("Pkl Files/ohe.pkl")
block_enc = joblib.load("Pkl Files/block_freq.pkl")
street_enc = joblib.load("Pkl Files/street_freq.pkl")

# -------------------------
# Custom Storey Function
# -------------------------
def extract_storey_midpoint(storey_range):
    if ' TO ' in storey_range:
        parts = storey_range.split(' TO ')
    else:
        try:
            return float(storey_range)
        except ValueError:
            return None

    lower = int(parts[0])
    upper = int(parts[1])
    return (lower + upper) / 2


# -------------------------
# Streamlit UI
# -------------------------
st.title("🏠 HDB Resale Price Prediction")

st.write("Enter flat details to predict resale price.")


# Inputs
town = st.selectbox(
    "Town",
    town_options
)

flat_type = st.selectbox(
    "Flat Type",
    flat_type_options
)

block = st.selectbox(
    "Select Block",
    block_options,
    placeholder="Choose block number"
)

street_name = st.selectbox(
    "Select Street Name",
    street_options,
    placeholder="Choose street name"
)

floor_area_sqm = st.number_input("Floor Area (sqm)", min_value=28.0, max_value=370.0, step=0.1)

flat_model = st.selectbox(
    "Flat Model",
    flat_model_options,
    placeholder="Select flat model"
)

# lease_commence_date = st.number_input("Lease Commence Year", min_value=1960, max_value=2025)

lease_commence_date = st.selectbox(
    "Lease Commence Year",
    list(range(1966, 2022))
)

year = st.selectbox(
    "Year",
    list(range(1990, 2027))
)

mon = st.selectbox(
    "Month",
    list(range(1, 13))
)

storey_range = st.selectbox(
    "Storey Range",
    storey_options,
    placeholder="Select Storey range"
)


# -------------------------
# Prediction
# -------------------------
if st.button("Predict Price"):

    # Storey conversion
    storey_mid = extract_storey_midpoint(storey_range)

    # Create dataframe
    df = pd.DataFrame({
        'town':[town],
        'flat_type':[flat_type],
        'flat_model':[flat_model]
    })

    # One Hot Encoding
    encoded = ohe.transform(df)
    encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out())

    # Block encoding
    block_val = block_enc[block]

    # Street encoding
    street_val = street_enc[street_name]

    # Final dataframe
    final_df = pd.concat([
        encoded_df,
        pd.DataFrame({
            'block_freq':[block_val],
            'street_freq':[street_val],
            'floor_area_sqm':[floor_area_sqm],
            'lease_commence_date':[lease_commence_date],
            'year':[year],
            'mon':[mon],
            'storey_mid':[storey_mid]
        })
    ], axis=1)

    # Prediction
    final_df = final_df[model.feature_names_in_]
    prediction = model.predict(final_df)

    prediction = np.expm1(prediction) 

    st.success(f"Estimated Resale Price: ${prediction[0]:,.2f}")