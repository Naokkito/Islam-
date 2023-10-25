try:
    file_name = input("Enter a file name: ")

    with open(file_name, 'r') as file:
        for line in file:
            print(line.upper(), end='')

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
    ///////////////////////////////////////////////////

file_name = "mbox.txt"  
email_hosts = {}

with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("From:"):
                email = line.split()[1]
                host = email.split('@')[1]
                email_hosts[host] = email_hosts.get(host, 0) + 1
for host in email_hosts:
        print(host)
print(f"Total {len(email_hosts)} hosts printed")
/////////////////////////////////////////////////
try:
    file_name = input("Enter a file name: ")
    total_confidence = 0
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    confidence = float(line.split(":")[1])
                    total_confidence += confidence
                    count += 1
                except ValueError:
                    continue

    if count > 0:
        average_confidence = total_confidence / count
        print(f"Average spam confidence: {average_confidence:.14f}")
    else:
        print("No X-DSPAM-Confidence lines found in the file.")

except FileNotFoundError:
    print(f"File cannot be opened: {file_name}")
