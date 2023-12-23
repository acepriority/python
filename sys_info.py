import platform
import multiprocessing

print("Operating System:", platform.system())
print("CPU Processor:", platform.processor())
print("Number of CPU cores:", multiprocessing.cpu_count())
