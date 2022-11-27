# Snack Coin Rewards

## **Project Overview**

Welcome to Snack Coin Rewards! This Streamlit-based application enables the user to order food from a provided menu, and earn SNAK tokens based on the total amount of eth spent on the order. 

### *Package Requirements and Versions*
`pip install x` ; where 'x' is the package listed below:
* `python == 3.10.6`
* `web3 == 5.31.1`
* `streamlit == 1.13.0`

### *Files Navigation*
* `SnackCoin.sol`: Solidity file containing the token contract
* `SnackMenu.sol`: Solidity file containing the menu and deployer contracts
* `abi-menu.json`: JSON file of the abi for the menu contract
* `abi-token.json`: JSON file of the abi for the token contract
* `create_db.sql`: SQL file creating the database framekwork
* `insert_data.sql`: SQL file containing the queries
* `snack.db`: Database containing the menu items
* `app.py`: Python script containing the code that’s associated with the web interface of the application
* `Images`: Directory containing images of menu itmes and sub directory of application examples

--------------

## Installation

1. fs
2. Add your mnemonic seed phrase (which Ganache provides) to the SAMPLE.env file as WEB_PROVIDER_URI. Then rename the file to .env.


## Usage

Once installed, you can use the contracts and the python script to run thhe Snack Coin Rewards interface through Streamlit. 

## Examples of Application

tk

## Challenges, Limitations, and Future Developments

Unfortunately Streamlit's limitations did not allow us to make all of the connections to the database that we would have liked to make. For example, we were not able to import environment variables such as the contract addresses, so those had to be hard-coded in the python script after deploying the contracts in Remix. If we had more time, one option to change this would be to shift the app to a different framework with more options, such as Django.

## Team Members
1. Lara Barger
2. Bryan Follenweider
3. Alec Gladkowski
4. Alejandro Palacios