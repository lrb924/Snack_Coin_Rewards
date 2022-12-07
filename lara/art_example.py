import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB_PROVIDER_URI")))

## loading the contract
@st.cache(allow_output_mutation=True)
def load_contract():
    
    with open(Path("abi.json")) as abi:
        artwork_abi = json.load(abi)
        
    artwork_address = os.getenv("SMART_CONTRACT_DEPLOYED_ADDRESS")
    
    contract = w3.eth.contract(
        address=artwork_address,
        abi = artwork_abi
    )
    
    return contract

contract = load_contract()


st.title("Art Registry Appraisal")
st.write("Choose an account to start")

accounts = w3.eth.accounts

address = st.selectbox("Select an Account", options=accounts)

# register your art
st.markdown("## Register a New Artwork")

name = st.text_input("Enter a name for the artwork")
artist = st.text_input("Enter an artist name for the artwork")
appraisalValue = st.text_input("Enter an appraisal value for the artwork")
tokenURI = st.text_input("Enter a URI")

if st.button("Register Artwork"):
    tx_hash = contract.functions.registerArtWork(address, name, artist, int(appraisalValue), tokenURI).transact({"from":address})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Receipt is ready. Here it is:")
    st.write(dict(receipt))
    
    

# new appraisal
st.markdown("## New Appraisal")

totalTokenSupply = contract.functions.totalSupply().call()
tokenID = st.selectbox("Choose a Token", options=list(range(totalTokenSupply)))

newAppraisalValue = st.text_input("Enter the New Appraisal Value")

tokenURI = st.text_area("Enter information about the appraisal")

# address_ = st.selectbox("Select an Account", options=accounts)

if st.button("New Appraisal"):
    tx_hash = contract.functions.newAppraisal(tokenID, int(newAppraisalValue), tokenURI).transact({"from":address})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Receipt is ready. Here it is:")
    st.write(dict(receipt))


# appraisal history
st.markdown("## Appraisal History")

tokenID = st.number_input("ID of ArtWork", value = 0, step = 1)

if st.button("Get Appraisal History"):
    appraisalFilter = contract.events.Appraisal.createFilter(fromBlock = 0, argument_filters = {"tokenID": tokenID})
    appraisals = appraisalFilter.get_all_entries()
    
    if appraisals:
        for x in appraisals:
            reportDict = dict(x)
            st.markdown("### Event Logs")
            st.write(reportDict)
            st.markdown("Log Details")
            st.write(reportDict["args"])
    else:
        st.write("This artwork has no new appraisals")
        
        
        
