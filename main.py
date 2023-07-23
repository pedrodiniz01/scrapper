from machineInfo import check_cpu_usage, get_cpu_info, get_ram_info, get_gpu_info, check_host_cpu_usage



if __name__ == "__main__":
    # RAM Information
    ram_info = get_ram_info()
    print("\nRAM Information:\n")
    for key, value in ram_info.items():
        print(f"{key}: {value}")

    # CPU Information
    print("\n\nCPU Information:\n")
    cpu_usage_percent = check_cpu_usage()
    cpu_info = get_cpu_info()
    print("CPU Percentage Usage:", cpu_usage_percent, "%")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")

