from qiskit import QuantumCircuit, assemble
from qiskit_aer import Aer
import matplotlib.pyplot as plt

# Create a quantum circuit with 1 qubit and 1 classical bit
circuit = QuantumCircuit(1, 1)
circuit.name = "Single qubit random"

# Apply a Hadamard gate to the qubit, putting it in a superposition 
# of |0> and |1> states (equal probability of measuring either)
circuit.h(0)

# Measure the qubit and store the result in the classical bit
circuit.measure(0, 0)

# Draw the circuit in the terminal
print("Circuit diagram:")
print(circuit.draw())

# --- Simulation and Measurement ---

# Initialize a simulator backend from Qiskit Aer
simulator = Aer.get_backend('qasm_simulator')

# Assemble the circuit for the simulator and run it 1000 times (shots)
job = simulator.run(circuit, shots=1000)

# Get the results from the job
result = job.result()
counts = result.get_counts(circuit)

# Print the result counts
print("\nResult counts (0s and 1s):", counts)
