from qiskit import *

def GHZState():
    qr = QuantumRegister(3)
    cr = ClassicalRegister(3)
    circ = QuantumCircuit(qr, cr)
    circ.initialize('00', circ.qubits)
    circ.h(qr[0])
    circ.cx(qr[0], qr[1])
    circ.cx(qr[1], qr[2])
    circ.measure(qr, cr)

    # Execute the circuit
    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(circ, backend, shots=1000)
    counts = job.result().get_counts()
    print(counts)
    return counts

GHZStateState()