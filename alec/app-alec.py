import streamlit as st

import os
import json
from pathlib import Path
from dotenv import load_dotenv

# from sqlalchemy import create_engine
# import psycopg2
# import connectorx as cx

from web3 import Web3

load_dotenv()

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

accounts = generate_accounts(web3)

# Menu database

#db1 = "postgresql://postgres:8264@localhost:5432/nu_week7"
#menu_items = cx.read_sql(db1, "select * from address")


st.markdown("# Snack Menu")
st.markdown("## ...")
st.text("\n")
st.text("\n")

def get_menu():
    pass

st.markdown("## Order Food")
st.text("\n")

cart = dict()

order_item = st.selectbox("Select a Person", menu_items)
order_quantity = st.sidebar.number_input("Enter quantity:")

if st.button("Add to Cart"):
    
    # order_item: [quantity, price]
    # {'Hot dogs': [1, 0.001], 'Burger': [2, 0.002]}
    cart[order_item] = [order_quantity, menu_items[order_item]]

    
cart_total = 0

for x in cart.keys():
    
    cart_total +=  cart[x][0] * cart[x][1]

