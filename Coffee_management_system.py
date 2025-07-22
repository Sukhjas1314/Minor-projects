import streamlit as st

# define menu
menu = {
    "Pizza" : 120,
    "Burger" : 80,
    "Maggie" : 50,
    "Hot coffee" : 40,
    "Cold Coffee" : 60
}

st.title("🍵 Hotel Management System🥤")
st.subheader("Menu")

# Display items in a table
st.table([{"Item" : item,"Price (₹)" : price} for item,price in menu.items()])

# Initialize session state for order management
if 'order' not in st.session_state:
    st.session_state.order = []

# Ordering system
selected_item = st.selectbox("Select an item to order : ",list(menu.keys()))
if st.button("Add to Order"):
    st.session_state.order.append(selected_item)
    st.success(f"{selected_item} added to your order!")

# Dispaly current order
if st.session_state.order:
    st.subheader("🛒 Your Order")
    order_summary = {item : st.session_state.order.count(item) for item in set(st.session_state.order)}
    total_amount = sum(menu[item] * qty for item,qty in order_summary.items()) 

    st.table([{"Item": item,"Quantity":qty,"Price (₹)":menu[item]*qty} for item,qty in order_summary.items()])
    st.write(f"### Total amount : ₹{total_amount}")

    if st.button("Confirm Order"):
        st.success("✅ Order Confirmed! Thank you for ordering .Enjoy your meal!")
        st.session_state.order = []