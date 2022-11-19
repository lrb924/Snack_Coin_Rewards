# SnackCoin Streamlit WebApp


# Imports
import os
import json
from pathlib import Path
from dotenv import load_dotenv

import sqlite3
# import pandas as pd

from web3 import Web3

import streamlit as st


# Load .env
load_dotenv()

# Create Web3 instance with Ganache URI
# w3 = Web3(Web3.HTTPProvider(os.getenv("WEB_PROVIDER_URI")))

# Get the acccounts from Ganache
# accounts = w3.eth.accounts


# Load the contract
@st.cache(allow_output_mutation=True)
def load_contract():

    with open(Path("abi.json")) as abi_:
        abi = json.load(abi_)

    contract_address = os.getenv("SMART_CONTRACT_DEPLOYED_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi=abi
    )

    return contract


# contract = load_contract()


# Load menu database
st.markdown("# Snack Menu")
st.markdown("## ...")
st.text("\n")
st.text("\n")

con = sqlite3.connect('snack.db')
cur = con.cursor()


# Display the menu with streamlit
def display_menu():

    # Get all the rows in Food table
    #   that are in Menu1
    res = cur.execute(
        '''
        SELECT * FROM Food
        WHERE id IN (
            SELECT food_id from MenuItems
            WHERE menu_id = 1
        );
        '''
    ).fetchall()

    for row in res:
        id_, name_, about_, category_, image_, unit_price_ = row

        st.image(image_, width=200)
        st.markdown(f'### {name_}')
        st.markdown(f'{about_}')
        st.markdown(f'{unit_price_} ETH')


display_menu()

'''
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

'''
