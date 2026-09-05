with open("server.log", "r") as file:
    log_data = file.readlines()
    info = 0
    warning = 0
    error = 0

    for line in log_data:

        if "INFO" in line:
            info += 1

        elif "WARNING" in line:
            warning += 1

        elif "ERROR" in line:
            error += 1

print("----- LOG REPORT -----")
print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)