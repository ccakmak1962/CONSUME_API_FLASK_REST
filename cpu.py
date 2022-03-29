import psutil
import os

def main():
    # TODO Enter code here..
 
  # Output current CPU load as a percentage.
    print('System CPU load is {} %'.format(get_cpu_usage_pct()))
    print('CPU frequency is {} MHz'.format(get_cpu_frequency()))
    print('CPU temperature is {} degC'.format(get_cpu_temp()))
    # Output current RAM usage in MB
    print('RAM usage is {} MB'.format(int(get_ram_usage() / 1024 / 1024)))
    # Output total RAM in MB
    print('RAM total is {} MB'.format(int(get_ram_total() / 1024 / 1024)))
    # Output current RAM usage as a percentage.
    print('RAM usage is {} %'.format(get_ram_usage_pct()))
    # Output current Swap usage in MB
    print('Swap usage is {} MB'.format(int(get_swap_usage() / 1024 / 1024)))
    # Output total Swap in MB
    print('Swap total is {} MB'.format(int(get_swap_total() / 1024 / 1024)))
    # Output current Swap usage as a percentage.
    print('Swap usage is {} %'.format(get_swap_usage_pct()))

def get_swap_usage_pct():
    """
    Obtains the system's current Swap usage.
    :returns: System Swap usage as a percentage.
    :rtype: float
    """
    return psutil.swap_memory().percent
def get_swap_total():
    """
    Obtains the total amount of Swap in bytes available to the system.
    :returns: Total system Swap in bytes.
    :rtype: int
    """
    return int(psutil.swap_memory().total)
def get_swap_usage():
    """
    Obtains the absolute number of Swap bytes currently in use by the system.
    :returns: System Swap usage in bytes.
    :rtype: int
    """
    return int(psutil.swap_memory().used)
def get_ram_usage_pct():
    return psutil.virtual_memory().percent
def get_ram_total():
    return int(psutil.virtual_memory().total)
def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)
def get_cpu_usage_pct():
    return psutil.cpu_percent(interval=0.5)
def get_cpu_frequency():
    return int(psutil.cpu_freq().current)
def get_cpu_temp():
    # Initialize the result.
    result = 0.0
    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.
    if os.path.isfile('/sys/class/thermal/thermal_zone0/temp'):
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            line = f.readline().strip()
        # Test if the string is an integer as expected.
        if line.isdigit():
            # Convert the string with the CPU temperature to a float in degrees Celsius.
            result = float(line) / 1000
    # Give the result back to the caller.
    return result



if __name__ == "__main__":
    main()