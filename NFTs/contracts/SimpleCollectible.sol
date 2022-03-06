// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;


import "@openzepplin/contracts/token/ERC721/ERC721.sol*";

contract SimplieCollectible is ERC721 {
    constructor () public ERC721 ("Dogie", "DOG"){
        
    }

    function createCollectible() public returns (uint256) {
        
    }
}

