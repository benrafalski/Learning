pragma solidity >=0.6.0 <0.9.0; 

import "./simple_storage.sol";

contract StorageFactory {

    SimpleStroage[] public simpleStorageArray;


    function createSimpleStorageContract() public {
        SimpleStroage simple = new SimpleStroage();
        simpleStorageArray.push(simple);
    }

    function sfStore(uint256 _index, uint256 _number) public{
        // adress, abi
        SimpleStroage simple = SimpleStroage(address(simpleStorageArray[_index]));
        simple.store(_number);
    }

    // function sfGet(uint256 _index) public view returns (uint256) {
    //     SimpleStorage simple = SimpleStorage(address(simpleStorageArray[_index]))
    // }
}