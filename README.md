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

1. Clone `Snack_Coin_Rewards` repository to a local drive.
2. Upload the smart contract files (`SnackCoin.sol` and `SnackMenu.sol`) to Remix IDE. Compile both contracts.
3. Before deploying the contracts, make sure that “Ganache Provider” is selected as the environment and that the RPC Server from Ganache matches the one in Remix IDE.
4. Add your mnemonic seed phrase (which Ganache provides as the RPC Server) to the SAMPLE.env file as WEB_PROVIDER_URI. Then rename the file to .env.
5. Select an account from Ganache in Remix IDE to deploy the contracts.
6. First, choose the `SnackCoinMenuDeployer` contract from the Contract pulldown.
7. Fill in the NAME, SYMBOL, and WALLET under the DEPLOY, and then press transact. <br>
![Initial Deployer](https://github.com/lrb924/Snack_Coin_Rewards/blob/main/Images/Screenshots/Deployer.png)
8. Open the Deployed Contracts, specifically the `SNACKCOINMENUDEPLOYER`, and call the `snackcoin_menu_address` button and the `snackcoin_token_address` button.
9. Next, choose the `SnackCoinMenu` contract and paste the `snackcoin_menu_address` in the AT ADDRESS box under the DEPLOY. <br>
![Menu Contract](https://github.com/lrb924/Snack_Coin_Rewards/blob/main/Images/Screenshots/Menu.png)
11. Scroll down and under the Deployed Contracts you will see the `SNACKCOINMENU`.
12. Next, choose the `SnackCoin` contract and follow the same instructions in step 9, except paste the `snackcoin_token_address` in the AT ADDRESS box under the DEPLOY.
13. Scroll down and under the Deployed Contracts and you will see the `SNACKCOIN`.
14. Due to limitations, paste both the `snackcoin_menu_address` and the `snackcoin_token_address` in `app.py`.
15. Save the updated `app.py` and run the file via Streamlit by running the following code in your bash or terminal: 
    ```
    streamlit run app.py
    ```
16. Make sure to fill out the sidebar menu before cotinuing to the Snack Menu.

## Usage

Once installed, you can use the contracts and the python script to run the Snack Coin Rewards interface through Streamlit. The user will be able to add menu items to their order, use eth to pay for the order, and earn SNAK tokens based on the total cost of their order.  

## Examples of Application

tk

## Challenges, Limitations, and Future Developments

Unfortunately Streamlit's limitations did not allow us to make all of the connections to the database that we would have liked to make. For example, we were not able to import environment variables such as the contract addresses, so those had to be hard-coded in the python script after deploying the contracts in Remix IDE. If we had more time, one option to adjust this would be to shift the app to a different framework with more options, such as Django.

Additionally, our biggest challenge with the app is that there is no way (using Streamlit) to completely start a new order with a new customer unless the "Start New Order" button is selected. For example, if the page is refreshed, the order will continue with the last customer's order instead of starting new. Again, this seems to be a Streamlit limitation and if more time allowed, we would adjust and shift the app to a different framework that has more functionality such as this.  

## Team Members
1. Lara Barger
2. Bryan Follenweider
3. Alec Gladkowski
4. Alejandro Palacios