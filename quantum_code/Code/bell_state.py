from qiskit import *

def BellState():
    # Create a Quantum Circuit object acting on a quantum and classical
    # register of two qubits/bits
    qr = QuantumRegister(2)
    cr = ClassicalRegister(2)
    circ = QuantumCircuit(qr, cr)
    circ.initialize('00', circ.qubits)
    # Add a H gate on qubit 0, putting this qubit in superposition
    circ.h(qr[0])
    # Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting the
    # qubits in a bell state
    circ.cx(qr[0], qr[1])
    # Add measurement to the circuit
    circ.measure(qr, cr)

    # Execute the circuit
    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(circ, backend, shots=1000)
    counts = job.result().get_counts()
    print(counts)
    return counts

BellState()