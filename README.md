# Quantum_Error_Correction

A lot of the packages have been migrated and removed edit to get a better experience
Quantum error correction (QEC) is a set of methods used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise 1. 
QEC is theorized as essential to achieve fault-tolerant quantum computing that can reduce the effects of noise on stored quantum information, faulty quantum gates, faulty quantum preparation, and faulty measurements. 
This would allow algorithms of greater circuit depth 1.

Quantum error correction is not the same as classical error correction, which employs redundancy. The simplest albeit inefficient approach in classical error correction is the repetition code. The idea is to store the information multiple times, and—if these copies are later found to disagree—take a majority vote 1. However, copying quantum information is not possible due to the no-cloning theorem. 
This theorem seems to present an obstacle to formulating a theory of quantum error correction. But it is possible to spread the (logical) information of one qubit onto a highly entangled state of several (physical) qubits 1.

QEC codes do not always correctly decode logical qubits, but their use reduces the effect of noise. Similar to classical error correction, QEC codes use a syndrome measurement to diagnose which error corrupts an encoded state. 
An error can then be reversed by applying a corrective operation based on the syndrome 1. Depending on the QEC code used, syndrome measurement can determine the occurrence, location and type of errors. 
In most QEC codes, the type of error is either a bit flip, or a sign (of the phase) flip, or both (corresponding to the Pauli matrices X, Z, and Y) 1.
