# make a quantum circuit and simulate it and apply a measurement and use quantum error correction to correct the errors

# import the necessary libraries
from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.utils.mitigation import CompleteMeasFitter, complete_meas_cal
from qiskit_aer.noise import NoiseModel

# make a quantum circuit
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
qc.barrier()
qc.measure([0, 1, 2], [0, 1, 2])
qc.draw()

# simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1000).result()
counts = result.get_counts(qc)
print(counts)

# make a noise model
noise_model = NoiseModel.from_backend(simulator)
print(noise_model)

# make a calibration circuit
qr = QuantumRegister(3)
meas_calibs, state_labels = complete_meas_cal(qubit_list=[0, 1, 2], circlabel='mcal')
print(meas_calibs[2].draw())

# simulate the calibration circuit
job = execute(meas_calibs, simulator, shots=1000)
cal_results = job.result()
plot_histogram(cal_results.get_counts(meas_calibs[2]))

# make a measurement filter
meas_fitter = CompleteMeasFitter(cal_results, state_labels)
meas_fitter

# make a mitigation filter
meas_filter = meas_fitter.filter
mitigated_results = meas_filter.apply(result)
mitigated_counts = mitigated_results.get_counts(qc)
plot_histogram([counts, mitigated_counts], legend=['raw', 'mitigated'])

# print the results
print(counts)
print(mitigated_counts)


# make a plotting function
def get_noise():
    noise_model = NoiseModel.from_backend(simulator)
    return noise_model


def get_mitigated_counts(counts):
    meas_calibs, state_labels = complete_meas_cal(qubit_list=[0, 1, 2], circlabel='mcal')
    job = execute(meas_calibs, simulator, shots=1000)
    cal_results = job.result()
    meas_fitter = CompleteMeasFitter(cal_results, state_labels)
    meas_filter = meas_fitter.filter
    mitigated_results = meas_filter.apply(counts)
    mitigated_counts = mitigated_results.get_counts(qc)
    return mitigated_counts


def get_counts(qc):
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1000).result()
    counts = result.get_counts(qc)
    return counts


def plot_histograms(counts, mitigated_counts):
    plot_histogram([counts, mitigated_counts], legend=['raw', 'mitigated'])
    return


# call the functions
counts = get_counts(qc)
noise_model = get_noise()
mitigated_counts = get_mitigated_counts(counts)
plot_histograms(counts, mitigated_counts)

# print the results
print(counts)
print(mitigated_counts)
