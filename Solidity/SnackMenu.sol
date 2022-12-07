// SnackCoin Menu and Deployer Contracts


//SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.5.0;

// Import SnackCoin contract
import "./SnackCoin.sol";

//  Import the following contracts from the OpenZeppelin library:
//    * Crowdsale
//    * MintedCrowdsale
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract SnackCoinMenu is Crowdsale, MintedCrowdsale{
    
    // Holds the wallet to which the customer pays for the order
    address payable owner;

    // Create constructor for SnackCoinMenu
    constructor(

        uint rate,
        address payable wallet,
        SnackCoin token
    
    ) public Crowdsale(rate, address(this), token) {
    
        owner = wallet;
    
    }

    // Create an event to log submitted orders
    event NewOrder();

    // Mints tokens and sends them to the customer
    function orderSnack() public payable{

        // Call the buyTokens function from Crowdsale ERC20
        buyTokens(msg.sender);

        // Log NewOrder event
        emit NewOrder();

    }

    // Permits a function to only be called by the contract owner
    modifier onlyOwner() {
        
        require(msg.sender == owner, "-- You are not the owner of the contract!");
        _;
    
    }

    // Withdraws contract funds to the restaurant's wallet
    function WithdrawToOwner(uint amount) onlyOwner public{
        
        require(address(this).balance > amount, "-- Not enough funds in contract!");
        require(amount > 0, "-- Can't withdraw amount of 0!");

        // Send ether from the contract to the owner
        owner.transfer(amount);

    }

    // Allows owner to check the balance of the contract
    function CheckBalance() public view onlyOwner returns(uint){

        return address(this).balance;

    }

    // Fallback function to make contract payable
    function() external payable {}

}

contract SnackCoinMenuDeployer{

    // Holds the SnackCoin token contract address
    address public snackcoin_token_address;
    // Holds the SnackCoinMenu contract address
    address public snackcoin_menu_address;

    constructor() public {
        
        string memory name = "SnackCoin";
        string memory symbol = "SNAK";
        address payable owner_wallet = msg.sender;
        uint rate = 1000;

        // Create instance of SnackCoin contract & save its address
        // Initial supply is Zero SNAK
        SnackCoin snack_token = new SnackCoin(name, symbol, 0);
        snackcoin_token_address = address(snack_token);

        // Create instance of SnackCoinMenu contract & save its address
        SnackCoinMenu snack_menu = new SnackCoinMenu(rate, owner_wallet, snack_token);
        snackcoin_menu_address = address(snack_menu);

        // Allow SnackCoinMenu contract to mint SnackCoin
        snack_token.addMinter(snackcoin_menu_address);

        // Remove SnackCoinDeployer contract's ability to mint
        snack_token.renounceMinter();

    }
}