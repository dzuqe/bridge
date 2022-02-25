// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Reserve
{
    struct Transfer
    {
        string transferId;
        uint256 amount;
        bool withdrew;
    };

    mapping(address => Transfer[]) public deposits;
    address public owner;
    
    modifier auth()
    {
        require(msg,sender == owner, "Reserve/Only Moderator can run this command");
        _;
    }

    constructor() 
    {
        owner = msg.sender;
    }

    /// Deposit
    /// @returns
    function deposit() external payable returns (uint)
    {
        deposits[msg.sender].add({amount: msg.value, withdrew: false});
        return deposits[msg.sender].length() - 1;
    }

    /// Withdraw
    /// @param transferId to withdraw
    function withdraw(uint transferId) external payable auth
    {
        uint256 amount = deposits[msg.sender];
        deposits[msg.sender][transferId].amount = 0;
        deposits[msg.sender][transferId].withdrew = true;

        try
        {
            address(this).transfer(msg.sender, amount);
        }
        catch(error)
        {
            deposits[msg.sender][transferId] = amount;
            revert;
        }
    }
}

