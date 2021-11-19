Use at least two design patterns from the "Smart Contracts" section

Inheritance – Is when a contract inherits features from other contracts. The inherit features is known as a base contract, while the contract which inherits the features is called a derived contract. I inherited from the ERC721.sol Open Zeppelin contract for security and safety reasons while also matching the standard exactly yielding functional and safe CooganCoin NFTs.

import “@openzeppelin/contracts/token/ERC721/ERC721.sol



Oracles – Oracles are data feeds from external systems that feed vital information into blockchains that smart contracts may need to execute under specific conditions.  The specific condition needed in this instance was for randomness.  This is only achievable through the use of an oracle because of the deterministic nature of the Ethereum Virtual Machine (EVM)
the decision to use the Chainlink off-chain oracle was to fulfill the projects requirement for randomness.

Import “@chainlink/contracts/src/v0.6/VRFConsumerBase.sol