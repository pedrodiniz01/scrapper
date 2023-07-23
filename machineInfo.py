import psutil
import platform
import GPUtil

def check_ram_usage():
    # Get the virtual memory usage statistics
    virtual_memory = psutil.virtual_memory()
    ram_percentage = virtual_memory.percent

    return ram_percentage

def check_cpu_usage():
    # Get the CPU usage of the container (as seen from within the container)
    container_cpu_percent = psutil.cpu_percent(interval=1)

    # Get the number of CPUs/cores on the host machine
    host_cpu_count = psutil.cpu_count(logical=False)

    # Estimate the host CPU usage based on the container's view
    cpu_usage_percent = container_cpu_percent * host_cpu_count

    return cpu_usage_percent

def get_cpu_info():
    cpu_info = {
        "CPU": platform.processor(),
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
    }
    return cpu_info

def get_ram_info():
    ram = psutil.virtual_memory()
    ram_info = {
        "Total": f"{ram.total / (1024**3):.2f} GB",
        "Available": f"{ram.available / (1024**3):.2f} GB",
        "Used": f"{ram.used / (1024**3):.2f} GB",
        "Percentage Used": f"{ram.percent:.2f}%",
    }
    return ram_info

def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        gpu_info = [{
            "GPU": gpu.name,
            "GPU Memory": f"{gpu.memoryTotal:.2f} MB",
            "GPU Memory Used": f"{gpu.memoryUsed:.2f} MB",
            "GPU Memory Free": f"{gpu.memoryFree:.2f} MB",
            "GPU Utilization": f"{gpu.load * 100:.2f}%",
        } for gpu in gpus]
    except Exception as e:
        gpu_info = "GPU information not available."

    return gpu_info


def check_host_cpu_usage():
    # Get the CPU usage of the container (as seen from within the container)
    container_cpu_percent = psutil.cpu_percent(interval=1)

    # Get the number of CPUs/cores on the host machine
    host_cpu_count = psutil.cpu_count(logical=False)

    # Estimate the host CPU usage based on the container's view
    host_cpu_usage_percent = container_cpu_percent * host_cpu_count

    return host_cpu_usage_percent

if __name__ == "__main__":
    host_cpu_usage_percent = check_host_cpu_usage()
    print("Estimated Host CPU Usage:", host_cpu_usage_percent, "%")