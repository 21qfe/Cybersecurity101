with open("server_logs.txt", "w") as file:
    file.write("2026-06-07 10:00:12 - INFO - User milind logged in successfully.")
    file.write("2026-06-07 10:02:45 - WARN - Failed login attempt from IP: 192.168.1.50")
    file.write("2026-06-07 10:02:47 - WARN - Failed login attempt from IP: 192.168.1.50")
    file.write("2026-06-07 10:02:49 - WARN - Failed login attempt from IP: 192.168.1.50")
    file.write("2026-06-07 10:05:00 - INFO - Database backup completed.")
    file.write("2026-06-07 10:08:14 - ERROR - Unauthorized database access attempt from IP: 10.0.0.99")
    file.write("2026-06-07 10:12:33 - INFO - User admin logged out.")
    file.write("2026-06-07 10:15:22 - WARN - Failed login attempt from IP: 192.168.1.50")
alert=[]
with open("server_logs.txt", "r") as file:
    logs=file.readlines()
    c1=0
    for log in logs:
        if "Failed login attempt" in log:
            c1+=1
        if "ERROR" in log:
            alert.append(log.split(": ")[1])
    
with open("alerts.txt", "w") as outfile:
    outfile.write("SECURITY ALERT REPORT\n")
    outfile.write("=====================\n\n")
    outfile.write("Crtical Alerts from some source :\n")
    for alert_msg in alert:
        outfile.write(f"- {alert_msg}\n")
    if c1>3:
        outfile.write("\nMultiple failed login attempts detected  ")