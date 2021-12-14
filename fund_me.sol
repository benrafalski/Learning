// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract fundMe{

    mapping(address => uint256) public addressToAmountFunded;


    // function used to pay for things
   function fund() public payable{
       // msg. sender and value are keywords
       addressToAmountFunded[msg.sender] += msg.value;
       // what is the eth to usd conversion rate?
       // use an oracle
   } 
}