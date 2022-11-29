# Snack Coin Rewards

## **Project Overview**

Welcome to Snack Coin Rewards! This Streamlit-based application enables the user to order food from a provided menu, and earn SNAK tokens based on the total amount of eth spent on the order. 

### *Package Requirements and Versions*
`pip install x` ; where 'x' is the package listed below:
* `python == 3.10.6`
* `web3 == 5.31.1`
* `streamlit == 1.13.0`

### *Files Navigation*
* `Images`: Directory containing images of menu itmes and sub directory of application examples
* `Solidity`: Directory containing the the token contract file, the menu and deployer contracts file, and the associated JSON files of the required abi for both contracts.
  * `Solidity/SnackCoin.sol`
  * `Solidity/SnackMenu.sol`
  * `Solidity/abi-menu.json`
  * `Solidity/abi-token.json`
* `SQL`: Directory containing the SQL files creating the database framework and the associated queries.
  * `SQL/create_db.sql`
  * `SQL/insert_data.sql`
* `snack.db`: Database containing the completed order information, including the Customers, Food, MenuItems, Menus, OrderItems, Orders, and Rewards
* `app.py`: Python script containing the code that’s associated with the web interface of the application

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

Once installed, you can use the contracts and the python script to run the Snack Coin Rewards interface through Streamlit. The user will be able to add menu items to their order, use eth to pay for the order, and earn SNAK tokens based on the total cost of their order. And because we used SQLite, we are also able to see the data behind each order through the `snack.db`.

## Examples of Application

After the application is launched, the user/customer can fill out their information in the sidebar, and then click the "Add Customer" button before moving on to the Snack Menu. <br>
![Add Customer](https://github.com/lrb924/Snack_Coin_Rewards/blob/main/Images/Screenshots/Add%20Customer%20Sidebar.png)

The customer can then browse the menu items, and scroll down and must click the "Start an Order" button before continuing. <br>
![Start an Order](https://github.com/lrb924/Snack_Coin_Rewards/blob/main/Images/Screenshots/Start%20an%20Order.png)

Once menu items are added to the cart, the total amount due in eth will display. The customer can then complete their order by clicking on the "Place Order" button and get a receipt and find out how many SNAK tokens they earned. <br>
![Place Order](https://github.com/lrb924/Snack_Coin_Rewards/blob/main/Images/Screenshots/Place%20Order%20with%20Receipt.png)

Finally, the customer can check their SNAK token balance by going back to the sidebar and clicking on the "Check SNAK Balance" button. <br>
![SNAK Balance](https://github.com/lrb924/Snack_Coin_Rewards/blob/main/Images/Screenshots/SNAK%20Balance.png)

## Challenges, Limitations, and Future Developments

Unfortunately Streamlit's limitations did not allow us to make all of the connections to the database that we would have liked to make. For example, we were not able to import environment variables such as the contract addresses, so those had to be hard-coded in the python script after deploying the contracts in Remix IDE. We were also unable to index customers based on their wallets, and instead had to use customer_id as an index. Despite many attempts, we believe this is another Streamlit limitation. If we had more time, one option to adjust this would be to shift the app to a different framework with more options, such as Django.

Additionally, another challenge with the app is that there is no way (using Streamlit) for multiple people to interact or order using the app at the same time. If multiple people try to use the app at the same time, the most recent order will combine with the next order that's attempting to complete. This also coincides with the issue that customers are not able to start a new order as a new customer unless the "Start New Order" button is selected. For example, if the page is refreshed, the order will continue with the last customer's order instead of starting new. Again, this seems to be a Streamlit limitation and if more time allowed, we would adjust and shift the app to a different framework that has more functionality. 

If more time allowed, in addition to shifting the app to a different framework, our team would likely move the frontend and the backend to a server, and deploy the contract on the testnet.

## Team Members
1. Lara Barger
2. Bryan Follenweider
3. Alec Gladkowski
4. Alejandro Palacios