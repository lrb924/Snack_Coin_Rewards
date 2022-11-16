//SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.5.0;

// Import SnackCoin contract
import "./SnackCoin-alec.sol";

//  Import the following contracts from the OpenZeppelin library:
//    * Crowdsale
//    * MintedCrowdsale
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract SnackCoinMenu is Crowdsale, MintedCrowdsale{

    constructor(
        uint rate,
        address payable wallet,
        SnackCoin token
    ) public Crowdsale(rate, wallet, token) {}

}

contract SnackCoinMenuDeployer{

    // Holds the SnackCoin token contract address
    address public snackcoin_token_address;
    // Holds the SnackCoinMenu contract address
    address public snackcoin_menu_address;

    constructor(
        string memory name = "SnackCoin",
        string memory symbol = "SNAK",
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