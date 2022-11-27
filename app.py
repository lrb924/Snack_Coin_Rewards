# SnackCoin Streamlit WebApp

# Imports
import os
from decimal import Decimal
import json
from pathlib import Path
from dotenv import load_dotenv
import sqlite3
from web3 import Web3
import streamlit as st

# Load .env
load_dotenv()

# Create Web3 instance with Ganache URI
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB_PROVIDER_URI")))
# st.write(w3.)

# Get the acccounts from Ganache
accounts = w3.eth.accounts

# Load the contracts
@st.cache(allow_output_mutation=True)
def load_contract(which_contract):

    # Choose which hard-coded contract to load
    # contract_address = os.getenv("SMART_CONTRACT_DEPLOYED_ADDRESS")
    if which_contract == 'menu':
        contract_address = '0x90331E26a98070eB0328748B8BDd8c57097952Ea'
        with open(Path("abi-menu.json")) as abi_:
            abi = json.load(abi_)
    
    elif which_contract == 'token':
        contract_address = '0xd77EacA1C78Cab747fD7864CA2bf4B20a5b87229'
        with open(Path("abi-token.json")) as abi_:
            abi = json.load(abi_)

    contract = w3.eth.contract(
        address=contract_address,
        abi=abi
    )

    return contract


# Load menu database
con = sqlite3.connect('snack.db', timeout=10)
cur = con.cursor()

st.markdown("# Snack Menu")
st.markdown("## ...")
st.text("\n")
st.text("\n")

# Choose customer wallet
st.sidebar.markdown("## Please Enter Customer Info:")

wallet = st.sidebar.selectbox(label='Ethereum Wallet: ', options=accounts)

# Ask for customer info
customer_first = st.sidebar.text_input('First Name: ', key=1)
customer_last = st.sidebar.text_input('Last Name: ', key=2)
customer_phone = st.sidebar.text_input('Phone: ', key=3)
customer_email = st.sidebar.text_input('Email: ', key=4)

if st.sidebar.button('Add Customer'):
    # Optional instructor lines:
    # query = f"INSERT INTO Customers VALUES (1, {wallet}, {customer_first}, {customer_last}, {int(customer_phone)}, {str(customer_email)})"
    # query = f"INSERT INTO Customers VALUES (1, :wallet, :customer_first, :customer_last, :customer_phone, {str(customer_email)})"

    # Insert data into database
    query = "INSERT INTO Customers ('wallet', 'first_name', 'last_name', 'phone', 'email') VALUES(?,?,?,?,?)"
    params = (wallet, customer_first, customer_last, customer_phone, customer_email)
    cur.execute(query, params)
    con.commit()

    st.sidebar.write('Customer Added!')

menu_items = dict()

# Display the menu items in columns
col1, col2 = st.columns(2)

# Display the menu with streamlit
def display_menu():
    
    counter = 0

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

    # Formatting for column displays: going through each menu item
    for row in res:
        counter += 1
        id_, name_, about_, category_, image_, unit_price_ = row

        menu_items[name_] = [id_, about_, category_, image_, unit_price_]

        if counter < 4:
            with col1:
                st.image(image_, width=200)
                st.markdown(f'### {name_}')
                st.markdown(f'{about_}')
                st.markdown(f'{unit_price_} ETH')
        else:
            with col2:
                st.image(image_, width=200)
                st.markdown(f'### {name_}')
                st.markdown(f'{about_}')
                st.markdown(f'{unit_price_} ETH')

display_menu()

# Starting an order and adding menu items to cart
st.markdown("## Order Food")
st.text("\n")

st.text("Please click Start an Order and then begin adding items to your cart.")

cart = dict()

if st.button("Start an order"):

    # Load most recent customer_id
    query = "SELECT id FROM Customers ORDER BY id DESC LIMIT 1 OFFSET 0"
    res = cur.execute(query)
    for row in res:
        customer_id = int(str(row).strip('(,)'))

    # Add data to most recent order
    query = "INSERT INTO Orders (customer_id, order_total, time, completed) VALUES (?, 0.000, datetime('now'), FALSE)"
    params = (customer_id,)
    cur.execute(query, params)
    con.commit()

    st.write("Order started. Add items to cart below..")


def add_to_order():

    key1 = 5
    key2 = 6

    order_item = st.selectbox("Select an item", menu_items, key=key1)
    item_quantity = st.number_input("Enter quantity:", min_value=1, key=key2)

    if st.button("Add item to Order"):

        # Load most recent order_id
        query = "SELECT id FROM Orders ORDER BY id DESC LIMIT 1 OFFSET 0"
        res = cur.execute(query)
        for row in res:
            order_id = int(str(row).strip('(,)'))

        item_total = menu_items[order_item][4] * item_quantity

        cart[order_item] = [order_item, item_quantity]

        # Add items to most recent order
        query = '''
                INSERT INTO OrderItems (order_id, food_id, menu_id, quantity, item_total)
                VALUES
                        (?, ?, 1, ?, ?)
                '''
        params = (order_id, menu_items[order_item][0], item_quantity, item_total)
        cur.execute(query, params)

        for x in cart.keys():

            # Load order_total from the most recent order
            query = "SELECT order_total FROM Orders WHERE id = ?"
            params = (order_id,)
            res = cur.execute(query, params)
            for row in res:
                order_total = float(str(row).strip('(,)'))       

            # Compute most recent order_total
            price = menu_items[cart[x][0]][4]
            cart_total = order_total + cart[x][1] * float(price)

            st.markdown("### Order Total in Ether: ")
            st.write(cart_total)

            # Add most recent order_total to orders database
            query = "UPDATE Orders SET order_total = ? WHERE id = ?"
            params = (cart_total, order_id)
            cur.execute(query, params)
            con.commit()


add_to_order()

if st.button("Place Order"):

    # Load menu contract
    contract = load_contract('menu')

    # Get most recent order info
    query = "SELECT id, customer_id, order_total FROM Orders ORDER BY id DESC LIMIT 1 OFFSET 0"
    res = cur.execute(query).fetchall()
    for row in res:
        order_id, customer_id, order_total = row

    # Get customer wallet
    query = "SELECT wallet FROM Customers WHERE id = ?"
    params = (customer_id,)
    res = cur.execute(query, params).fetchall()
    for row in res:
        wallet = str(row).strip("(,')")

    # Convert order total from eth to wei
    order_total_wei = w3.toWei(Decimal(order_total), 'ether')
    token_amount = int(order_total * 1000)
    
    # Show order total amount paid from selected wallet
    st.write(f"Paying {order_total} ETH from wallet: {wallet}")

    # Submit transaction to contract
    txn_hash = contract.functions.orderSnack(order_total_wei, token_amount).transact({
        'from': wallet,
        'value': order_total_wei
    })
    receipt = w3.eth.waitForTransactionReceipt(txn_hash)
    st.write("Receipt is ready. Here it is: ")
    st.write(dict(receipt))
    
    # Get most recent order total 
    query = "SELECT id, customer_id, order_total FROM Orders ORDER BY id DESC LIMIT 1 OFFSET 0"
    res = cur.execute(query).fetchall()
    for row in res:
        id, customer_id, order_total = row
    
    # Add rewards earned to rewards database    
    order_tokens = order_total * 1000
    query = "INSERT INTO Rewards (customer_id, order_id, snak_tokens) VALUES(?,?,?)"
    params = (customer_id, id, order_tokens)
    cur.execute(query, params)
    con.commit()

    # Show rewards earned
    st.write(f"You earned: {order_tokens} SNAK, eat more and earn more!")

st.sidebar.write("Please add yourself as a customer before placing an order!")

if st.sidebar.button("Check SNAK Balance"):

    # Load SNAK Token Address
    contract = load_contract('token')
    
    # Get most recent order info
    query = "SELECT id, customer_id, order_total FROM Orders ORDER BY id DESC LIMIT 1 OFFSET 0"
    res = cur.execute(query).fetchall()
    for row in res:
        order_id, customer_id, order_total = row

    # Get customer wallet
    query = "SELECT wallet FROM Customers WHERE id = ?"
    params = (customer_id,)
    res = cur.execute(query, params).fetchall()
    for row in res:
        wallet = str(row).strip("(,')")
    
    # Show customer token balance    
    token_balance = contract.functions.balanceOf(wallet).call()
    token_balance /= 10**18
    token_balance = round(token_balance,1)
    st.sidebar.write(token_balance)

st.sidebar.write("Check your SNAK token balance after placing an order..")

con.close()
