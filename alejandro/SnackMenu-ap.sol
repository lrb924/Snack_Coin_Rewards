// SnackCoin Menu and Deployer Contracts
//SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.5.0;
// Import SnackCoin contract
import "./SnackCoin-ap.sol";
//  Import the following contracts from the OpenZeppelin library:
//    * Crowdsale
//    * MintedCrowdsale
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
contract SnackCoinMenu is Crowdsale, MintedCrowdsale{
    // Create constructor for SnackCoinMenu
    constructor(
        uint rate,
        address payable wallet,
        SnackCoin token
    ) public Crowdsale(rate, wallet, token) {}
    // Create an event to log submitted orders
    event NewOrder(uint order_total, uint token_amount);
    // Function that places a new order
    function orderSnack(uint order_total, uint token_amount) public payable{
        // Add if/else for order total & token quantity requirements
        // e.g.
        // if amount not enough
        // requir( x,y )
        // transfer(from msg.sender to contract owner)
        // Call the buyTokens function from Crowdsale ERC20
        buyTokens(msg.sender);
        // Log NewOrder event with item details
        emit NewOrder(order_total, token_amount);
    }
}
contract SnackCoinMenuDeployer{
    // Holds the SnackCoin token contract address
    address public snackcoin_token_address;
    // Holds the SnackCoinMenu contract address
    address public snackcoin_menu_address;
    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    ) public {
        // Create instance of SnackCoin contract & save its address
        // Initial supply is Zero SNAK
        SnackCoin snack_token = new SnackCoin(name, symbol, 0);
        snackcoin_token_address = address(snack_token);
        // Create instance of SnackCoinMenu contract & save its address
        SnackCoinMenu snack_menu = new SnackCoinMenu(1000, wallet, snack_token);
        snackcoin_menu_address = address(snack_menu);
        // Allow SnackCoinMenu contract to mint SnackCoin
        snack_token.addMinter(snackcoin_menu_address);
        // Remove SnackCoinDeployer contract's ability to mint
        snack_token.renounceMinter();
    }
}