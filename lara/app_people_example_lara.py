import streamlit as st
from ethereum import generate_accounts, get_balance, send_transaction
from web3 import Web3
# import pydbgen

web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

account = generate_accounts(web3)

st.markdown("# Ethereum Account")
st.text("\n")
st.markdown("## Account Address")
st.write(account.address)

st.text("\n")
st.markdown("## Balance")
ether_balance = get_balance(web3, account.address)
st.write(ether_balance)

# st.text("\n")
# st.text("\n")
# receiver = st.text_input("Receiver Address")
# ether = st.number_input("Amount of Ether")

# if st.button("Send Transaction"):
#     transaction_hash = send_transaction(web3,account,receiver,ether)
#     st.text("\n")
#     st.text("\n")
#     st.markdown("## Transaction Hash")
#     st.write(transaction_hash)


###################################################################################


menu_database = {
    "ash":["Ash","0xA50880B765cC5C25Cb96690cbBdCC4D5e46ABE38", "4.3", .20, "Images/ash.jpeg"],
    "jo":["Jo","0x0f12fAf99FA57Ffb8BEE5E000E51b9FBBc68397f","5.0", .33, "Images/jo.jpeg"],
    "kendall":["Kendall","0xDb7b49E75Cb3EDF59Cbd45864D7c624f2113855e","4.7", .19, "Images/kendall.jpeg"],
    "lane":["Lane","0xDb37611FB179D49829f3203d4081a455BDdd0018","4.1", .17, "Images/lane.jpeg"]
}

person_names = ["ash","jo","kendall", "lane"]


def get_person():
    db_list = list(person_database.values()) 
    
    for x in range(len(person_names)):
        st.image(db_list[x][4], width = 200)
        
        st.write("Name: ", db_list[x][0])
        st.write("Address: ", db_list[x][1])
        st.write("Rating: ", db_list[x][2])
        st.write("Hourly Rate per ETH: ", db_list[x][3])
        st.text("\n")
        
        
st.markdown("# Person Database")
st.markdown("## Choose a Person to Hire")
st.text("\n")
st.text("\n")

person = st.sidebar.selectbox("Select a Person", person_names)
st.sidebar.markdown("## Person Name and Price")
name_of_person = person_database[person][0]
address_of_person = person_database[person][1]
rating_of_person = person_database[person][2]
rate_of_person = person_database[person][3]


hours = st.sidebar.number_input("How many hours to hire for?")
wage = hours * rate_of_person
st.sidebar.write(wage)




if wage <= ether_balance:
    new_balance = float(ether_balance) - float(wage)
    st.sidebar.write(f"You can hire {name_of_person} for {wage} ether")
    get_person()
else:
    st.sidebar.write(f"You cannot hire {name_of_person} for {wage} ether")
    get_person()


st.text("\n")

if st.button("Hire a Person"):
    transaction_hash = send_transaction(web3, account, address_of_person, wage)
    st.text("\n")
    st.text("\n")
    st.markdown("## Transaction Hash")
    st.write(transaction_hash)
    
    
        

