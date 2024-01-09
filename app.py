import streamlit as st
import requests

# Replace with your backend API URL
API_URL = "http://localhost:8000"

# Streamlit UI components
st.title("Financial Portfolio Management System")

# Login functionality
login_username = st.text_input("Username")
login_password = st.text_input("Password", type="password")
login_button = st.button("Login")

if login_button:
    # Send login request to the backend and receive JWT token
    response = requests.post(
        f"{API_URL}/token",
        data={"username": login_username, "password": login_password}
    )

    if response.status_code == 200:
        st.success("Login successful!")
        access_token = response.json().get("access_token")
        # Save the access token for future requests
    else:
        st.error("Login failed. Check your credentials.")

# Portfolio management functionality
if "access_token" in locals():
    st.subheader("Portfolio Management")

    # Implement UI components for portfolio management
    portfolio_name = st.text_input("Portfolio Name")
    st.write("Add Asset:")
    asset_symbol = st.text_input("Symbol")
    asset_quantity = st.number_input("Quantity", value=0.0, step=0.1)
    add_asset_button = st.button("Add Asset")

    if add_asset_button:
        # Send request to backend to add asset to the portfolio
        response = requests.post(
            f"{API_URL}/add_asset",
            headers={"Authorization": f"Bearer {access_token}"},
            json={"portfolio_name": portfolio_name, "symbol": asset_symbol, "quantity": asset_quantity}
        )
        if response.status_code == 200:
            st.success("Asset added successfully!")
        else:
            st.error("Failed to add asset. Check the input.")

    # Implement additional UI components for managing portfolios
    # ...

# ... (additional code)
