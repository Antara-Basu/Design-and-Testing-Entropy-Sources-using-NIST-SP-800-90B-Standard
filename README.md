# Design-and-Testing-Entropy-Sources-using-NIST-SP-800-90B-Standard
**Introduction**
To secure any communication between 2 parties, both the sender and receiver must ensure the channel is secure. To achieve this, the transmitted signals are encrypted  using an encryption algorithm and at the reciever's end, they're decrypted to retrieve the original message. Both encryption and decryption algorithms rely on a key, which is shared between the communicating parties.
However, if an attacker gets hold of the key, they can easily decode the message. In order to eradicate this type of risk, random keys are used which are represented as bitstrings of 0s and 1s- to prevent prediction.This is pricely when Random Number Generators(RNGs) comes into picture. RNGs provides the much needed randomness for generating secure keys that strengthen the encryption process against potential breaches.
**There are 2 types of Random Number Generators(RNG):
 1) **True RNG:** A True RNG uses a nondeterministic source to make randomness.
For this the computer must use some external physical variable that is unpredictable, such as at the quantum level, subatomic particles have completely random behaviour, making them ideal variables of an unpredictable system.
 2) **Pseudo RNG:** Software-generated numbers only are pseudorandom. They are not truly random because the computer uses an algorithm based on a distribution and are not secure because they rely on deterministic  predictable algorithms.
DRDO is looking for Quantum RNG. As quantum gives it a true property.They need a setup which can generate the Quantum Random Bitstring.
In DYSL-QT - They have a project of developing Quantum Random Number Generator. However, they must be sure that bitstrings are entirely random after they are generated.
To determine whether those bitsrings are truly random or not, there is a Randomness Test. DYSL-QT has executed over 150 Randomness Tests thus far.
Once the Bitstrings were found to be truly random by passing the Randomness test, my work started. I had to quantify the bitstring's randomness. Entropy is a useful metric to quantify it.
**Entropy -** Measure of randomness or disorder in a system.
Entropy of 1 - Fully random
Entropy of 0 -  Not at all random
**My part was developement and implementation of entropy**
Assume for the moment that I have written a function to determine the entropy of a bitsring with 20K bits. Thus, the bitstring's entropy value will be provided by this entropy estimation program.  Then a report will be generated after the test is completed saying "QRNG has successfully passed the test with this [entropy value]".
So how do we calculate the entropy ?
By entropy estimation methods:
1)Maximum Entropy:

2)Minimum Entropy:

