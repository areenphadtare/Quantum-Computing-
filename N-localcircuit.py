from qiskit.circuit.library import n_local

two_local = n_local(3, "rx", "cz")
two_local.draw("mpl")