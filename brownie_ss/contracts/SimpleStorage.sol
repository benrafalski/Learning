// SPDX-License-Identifier: MIT
// version 
pragma solidity >=0.6.0 <0.9.0; 

contract SimpleStorage {

    // types
    uint256 public favoriteNumber;
    // bool favotiteBool = true;
    // string favString = "string"; 
    // int256 = favInt;
    // address favAddress = "0xb6e2549f020Be31f56C2Eac1E8787b514Fb53Dd6";
    // bytes32 favBytes = "cat";


    // struct
    struct People {
        uint256 favNumber;
        string name;
    }

    People public person = People({
        favNumber: 2, 
        name: "Ben"
    });

    // arrays
    People[] public people;

    // mapping
    mapping(string => uint256) public nameTopFavNum;



    // functions
    function store(uint256 _favNum) public{
        favoriteNumber = _favNum;
    }

    // function addPerson(string memory _name, uint256 _favNum) public{
    //     people.push(People({
    //         favNumber: _favNum,
    //         name: _name
    //     }));
    //     nameTopFavNum[_name] = _favNum;
    // }



    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }

}