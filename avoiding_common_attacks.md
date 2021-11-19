Using Specific Compiler Pragma 
https://swcregistry.io/docs/SWC-103  - Floating Pragma
Since the contract isn’t meant for consumption by other developers it was decided to lock the contract compiler to a specific version rather than having a floating pragma where the compiler version can vary in its implementation.


Proper Use of Require
https://swcregistry.io/docs/SWC-123 - Requirement Violation 
In order to make sure that either an owner or approved user is able to take possession of the NFT a strong logical condition (require statement) is strongly set so that there are no precondition violations. The requirement statement is needed to validate the external input and is not in violation.


Timestamp Dependence
https://swcregistry.io/docs/SWC-120 - Weak Sources of Randomness from Chain Attributes
Knowing some of the pitfalls in smart contracts related to the EVM it was decided to use an external source of randomness that was not reliant on a timestamp or the deterministic nature of the EVM. Chainlink VRF (Verifiable Random Function) is a provably-fair and verifiable source of randomness designed for smart contracts. Smart contract developers can use Chainlink VRF as a tamper-proof random number generator (RNG) to build reliable smart contracts for any applications which rely on unpredictable outcomes:




