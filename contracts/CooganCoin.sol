pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";
/// Inherit from libraries ///

contract CooganCoin is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;

    enum Coog {FANATIC, SUPERFAN, FAN}

    mapping(bytes32 => address) public requestIdToSender;
    mapping(bytes32 => string) public requestIdToTokenURI;
    mapping(uint256 => Coog) public tokenIdToCoog;
    mapping(bytes32 => uint256) public requestIdToTokenId;
    event requestedCollectible(bytes32 indexed requestId);

    bytes32 internal keyHash;
    uint256 public fee;

    constructor(address _VRFCoordinator, address _LinkToken, bytes32 _keyhash)
    public
    VRFConsumerBase(_VRFCoordinator, _LinkToken)
    ERC721("Coogans", "COOG")
    {
        tokenCounter = 0;
        keyHash = _keyhash;
        fee = 0.1 * 10 ** 18; //0.1 LINK
    }

    function createCollectible(string memory tokenURI)
        public returns (bytes32){
            bytes32 requestId = requestRandomness(keyHash, fee);
            requestIdToSender[requestId] = msg.sender;
            requestIdToTokenURI[requestId] = tokenURI;
            emit requestedCollectible(requestId);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override{
        address coogStudent = requestIdToSender[requestId];
        string memory tokenURI = requestIdToTokenURI[requestId];
        uint256 newItemId = tokenCounter;
        _safeMint(coogStudent, newItemId);
        _setTokenURI(newItemId, tokenURI);
        Coog coog = Coog(randomNumber % 3);
        tokenIdToCoog[newItemId] = coog;
        requestIdToTokenId[requestId] = newItemId;
        tokenCounter = tokenCounter + 1;
    }   

    function  setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner_approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
