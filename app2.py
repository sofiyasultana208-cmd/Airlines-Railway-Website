# Importing required libraries
import streamlit as st
import pandas as pd
from datetime import datetime

# Set page title and icon
st.set_page_config(page_title="RailEase", page_icon="🚆", layout="wide")

# Add custom font using Google Fonts
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

body {
    font-family: 'Roboto', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Light/Dark mode CSS styles
dark_mode_css = """
<style>
body {
    background-color: #1e1e1e;
    color: white;
}
h1, h2, h3 {
    color: #00aaff;
}
</style>
"""

light_mode_css = """
<style>
body {
    background-color: #f8f9fa;
    color: black;
}
</style>
"""

# Sample train data - 30 entries
trains = [
    {'train_no': '101', 'name': 'Golden Temple Mail', 'source': 'AMRITSAR', 'destination': 'MUMBAI',
     'departure': '15:30', 'arrival': '14:45', 'duration': '23h 15m', 'class': 'Sleeper', 'fare': 750},
    {'train_no': '102', 'name': 'Deccan Queen', 'source': 'PUNE', 'destination': 'MUMBAI',
     'departure': '08:00', 'arrival': '11:10', 'duration': '3h 10m', 'class': 'AC', 'fare': 900},
    {'train_no': '103', 'name': 'Chennai Express', 'source': 'CHENNAI', 'destination': 'DELHI',
     'departure': '18:00', 'arrival': '16:00', 'duration': '22h', 'class': 'AC', 'fare': 1800},
    {'train_no': '104', 'name': 'Goa Express', 'source': 'MADGAON', 'destination': 'DELHI',
     'departure': '20:00', 'arrival': '02:30', 'duration': '30h 30m', 'class': 'Sleeper', 'fare': 1000},
    {'train_no': '105', 'name': 'Howrah Superfast', 'source': 'KOLKATA', 'destination': 'PATNA',
     'departure': '06:00', 'arrival': '14:00', 'duration': '8h', 'class': 'AC', 'fare': 650},

    {'train_no': '106', 'name': 'North East Express', 'source': 'GUWAHATI', 'destination': 'CHANDIGARH',
     'departure': '14:00', 'arrival': '11:30', 'duration': '21h 30m', 'class': 'Sleeper', 'fare': 1200},
    {'train_no': '107', 'name': 'Duronto Express', 'source': 'HOWRAH', 'destination': 'NEW DELHI',
     'departure': '18:00', 'arrival': '10:00', 'duration': '16h', 'class': 'AC', 'fare': 2200},
    {'train_no': '108', 'name': 'Shatabdi Express', 'source': 'CHANDIGARH', 'destination': 'DELHI',
     'departure': '07:00', 'arrival': '10:00', 'duration': '3h', 'class': 'AC', 'fare': 800},
    {'train_no': '109', 'name': 'Rajdhani Express', 'source': 'MUMBAI', 'destination': 'DELHI',
     'departure': '17:00', 'arrival': '09:00', 'duration': '16h', 'class': 'AC', 'fare': 2000},
    {'train_no': '110', 'name': 'Jan Shatabdi', 'source': 'BANGALORE', 'destination': 'MYSORE',
     'departure': '06:30', 'arrival': '09:00', 'duration': '2.5h', 'class': 'Sleeper', 'fare': 150},

    {'train_no': '111', 'name': 'Intercity Express', 'source': 'DELHI', 'destination': 'JAIPUR',
     'departure': '08:00', 'arrival': '12:00', 'duration': '4h', 'class': 'Sleeper', 'fare': 300},
    {'train_no': '112', 'name': 'Tejas Express', 'source': 'MUMBAI', 'destination': 'AHMEDABAD',
     'departure': '08:00', 'arrival': '13:00', 'duration': '5h', 'class': 'AC', 'fare': 1200},
    {'train_no': '113', 'name': 'Maharaja Express', 'source': 'DELHI', 'destination': 'MUMBAI',
     'departure': '20:00', 'arrival': '18:00', 'duration': '22h', 'class': 'AC', 'fare': 3000},
    {'train_no': '114', 'name': 'Garib Rath', 'source': 'LUCKNOW', 'destination': 'DELHI',
     'departure': '19:00', 'arrival': '06:30', 'duration': '11h 30m', 'class': 'Sleeper', 'fare': 400},
    {'train_no': '115', 'name': 'Sampark Kranti', 'source': 'PATNA', 'destination': 'DELHI',
     'departure': '21:00', 'arrival': '07:00', 'duration': '10h', 'class': 'AC', 'fare': 600},

    {'train_no': '116', 'name': 'Himalayan Queen', 'source': 'SHIMLA', 'destination': 'CHANDIGARH',
     'departure': '09:00', 'arrival': '12:00', 'duration': '3h', 'class': 'Sleeper', 'fare': 200},
    {'train_no': '117', 'name': 'Nilgiri Express', 'source': 'CHENNAI', 'destination': 'COIMBATORE',
     'departure': '10:00', 'arrival': '18:00', 'duration': '8h', 'class': 'Sleeper', 'fare': 300},
    {'train_no': '118', 'name': 'Kalinga Utkal', 'source': 'BHUBANESHWAR', 'destination': 'MUMBAI',
     'departure': '22:00', 'arrival': '16:00', 'duration': '18h', 'class': 'Sleeper', 'fare': 800},
    {'train_no': '119', 'name': 'Coromandel Express', 'source': 'CHENNAI', 'destination': 'KOLKATA',
     'departure': '18:00', 'arrival': '16:00', 'duration': '22h', 'class': 'AC', 'fare': 1600},
    {'train_no': '120', 'name': 'Yeshvantpur Express', 'source': 'BANGALORE', 'destination': 'PUNE',
     'departure': '16:00', 'arrival': '12:00', 'duration': '20h', 'class': 'Sleeper', 'fare': 600},

    {'train_no': '121', 'name': 'Jammu Tawi Express', 'source': 'JAMMU', 'destination': 'DELHI',
     'departure': '15:00', 'arrival': '08:00', 'duration': '17h', 'class': 'Sleeper', 'fare': 550},
    {'train_no': '122', 'name': 'Lokmanya Tilak Express', 'source': 'MUMBAI', 'destination': 'DELHI',
     'departure': '20:00', 'arrival': '18:00', 'duration': '22h', 'class': 'Sleeper', 'fare': 700},
    {'train_no': '123', 'name': 'Sachkhand Express', 'source': 'DELHI', 'destination': 'AMRITSAR',
     'departure': '06:00', 'arrival': '11:00', 'duration': '5h', 'class': 'AC', 'fare': 850},
    {'train_no': '124', 'name': 'Vande Bharat', 'source': 'DELHI', 'destination': 'KATRA',
     'departure': '08:00', 'arrival': '13:00', 'duration': '5h', 'class': 'AC', 'fare': 1500},
    {'train_no': '125', 'name': 'Udyan Express', 'source': 'BANGALORE', 'destination': 'MUMBAI',
     'departure': '18:00', 'arrival': '12:00', 'duration': '18h', 'class': 'Sleeper', 'fare': 600}
]

df_trains = pd.DataFrame(trains)

# Food menu for different classes
food_items = {
    "AC": [
        {"item": "Veg Thali", "price": 120},
        {"item": "Paneer Sandwich", "price": 80},
        {"item": "Masala Dosa", "price": 90},
        {"item": "Cold Drink", "price": 40},
        {"item": "Tea", "price": 20},
        {"item": "Coffee", "price": 25},
        {"item": "Vegetable Roll", "price": 70},
        {"item": "Spring Roll", "price": 60},
        {"item": "Fruit Salad", "price": 50},
        {"item": "Mini Samosa", "price": 30},
        {"item": "Biscuits Pack", "price": 25},
        {"item": "Water Bottle", "price": 20}
    ],
    "Sleeper": [
        {"item": "Packed Lunch", "price": 60},
        {"item": "Biscuits", "price": 15},
        {"item": "Water Bottle", "price": 20},
        {"item": "Snacks Pack", "price": 30},
        {"item": "Boiled Eggs (2 pcs)", "price": 30},
        {"item": "Tea", "price": 15},
        {"item": "Coffee", "price": 20},
        {"item": "Namkeen Packet", "price": 25},
        {"item": "Chips Packet", "price": 20},
        {"item": "Dry Fruit Mix", "price": 50},
        {"item": "Banana", "price": 10},
        {"item": "Orange", "price": 15}
    ]
}

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    nav_option = st.radio("Go to", ["Search Trains", "All Trains", "Book Food"])

    st.markdown("---")
    st.markdown("Theme")
    dark_mode = st.checkbox("Dark Mode")

    if dark_mode:
        st.markdown(dark_mode_css, unsafe_allow_html=True)
    else:
        st.markdown(light_mode_css, unsafe_allow_html=True)

# Main content area
if nav_option == "Search Trains":
    st.title("RailEase – Smart Train Booking Platform")
    st.subheader("Find Your Train")
    st.write("Search for trains based on source, destination, and class.")

    col1, col2, col3 = st.columns(3)
    with col1:
        source = st.selectbox("From", sorted(df_trains["source"].unique()))
    with col2:
        destination = st.selectbox("To", sorted(df_trains["destination"].unique()))
    with col3:
        travel_class = st.radio("Class Type", ["Sleeper", "AC"])

    travel_date = st.date_input("Travel Date", min_value=datetime.now().date())

    if st.button("Search Trains"):
        with st.spinner("Searching for trains... Please wait."):
            if source == destination:
                st.error("Source and Destination cannot be the same.")
            else:
                results = df_trains[
                    (df_trains["source"] == source) &
                    (df_trains["destination"] == destination) &
                    (df_trains["class"] == travel_class)
                ]

                if not results.empty:
                    st.success(f"Found {len(results)} trains:")
                    st.dataframe(results, use_container_width=True)
                else:
                    st.warning("No trains found for your criteria.")

elif nav_option == "All Trains":
    st.title("RailEase – Smart Train Booking Platform")
    st.subheader("All Available Trains")
    st.dataframe(df_trains, use_container_width=True)

elif nav_option == "Book Food":
    st.title("RailEase – Smart Train Booking Platform")
    st.subheader("Order Food for Your Journey")
    selected_train = st.selectbox("Select Train Number", options=df_trains["train_no"])
    
    if selected_train:
        train_info = df_trains[df_trains["train_no"] == selected_train].iloc[0]
        st.info(f"Selected Train: {train_info['name']} | Class: {train_info['class']}")
        
        menu = food_items[train_info['class']]
        cart = []

        with st.form("food_order_form"):
            st.markdown("#### Choose Your Items:")
            for item in menu:
                qty = st.number_input(f"{item['item']} - ₹{item['price']}", min_value=0, max_value=10, step=1, key=item['item'])
                if qty > 0:
                    cart.append({"item": item['item'], "qty": qty, "price": item['price']})
            
            confirm = st.form_submit_button("Confirm Order")
            if confirm:
                if cart:
                    total = sum(i['qty'] * i['price'] for i in cart)
                    st.balloons()
                    st.success("Your food order is confirmed!")
                    st.markdown("### Summary:")
                    for item in cart:
                        st.markdown(f"- {item['item']} x {item['qty']} = ₹{item['qty'] * item['price']}")
                    st.markdown(f"**Total Amount: ₹{total}**")
                else:
                    st.warning("Please select at least one item.")

# Footer
st.markdown("---")
st.markdown("Demo Only | © 2025")