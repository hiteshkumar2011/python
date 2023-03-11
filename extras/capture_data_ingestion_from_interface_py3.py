import smtplib
def send_email(to,subject,body):
    # Sender's email address and password
    smtp_user = ""
    smtp_password = ""
    sent_from = ""
    # Receiver's email address
    to = [to]
    # Message to be sent
    email_text = f"Subject: {subject}\n\n{body}"
    try:
        # Connect to the email server
        server = smtplib.SMTP('SMTP_IP', 25)
        server.ehlo()
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sent_from,to,email_text)
        server.close()
        print("Email Sent")
    except Exception as e:
        print(f"Something went wrong..{e}")

def read_network_stats():
    with open("/proc/net/dev") as f:
        lines = f.readlines()
    # Remove the header and footer lines
    lines = lines[2:-2]       ##Check the line trimming by printing the output
    stats = {}
    for line in lines:
        # Split the line into columns
        columns = line.strip().split()
        # Extract the interface name and receive bytes
        global iface
        iface = columns[0].split(":")[0]
        print('Transfer and  Receive Bytes For Interface',iface)
        recv_bytes = int(columns[1])
        tx_bytes = int(columns[9])
        # Store the results in a dictionary
        stats[iface+'_tx_bytes'] = tx_bytes
        stats[iface+'_rx_bytes'] = recv_bytes
    return stats



def main():
    stats = read_network_stats()
    data = {}
    for keys in stats:
       # Convert the transfer & receive bytes to gigabytes
        recv_gb =  stats[keys]/ (1000.0 ** 3)
        #tx_gb = tx_bytes / (1000.0 ** 3)
        print(recv_gb)
#        #print("The interface is ",iface + ":", recv_gb + "GB" )
        print("{} - {:.2f} GB".format(keys, recv_gb))
        data += "{} - {:.2f} GB".format(keys, recv_gb)
    message = "Subject: ELK Data Ingestion at Elastic Search LB Interface  \n\n"
    message += "Transfer and  Receive Bytes For Interface " + str(iface) + "\n" + str(data)
   


if __name__ == "__main__":
    main()

#d= {"key1":"value1","key2":"value2"}
#body = ""
#for key,value in d.items():
#    body+=f"{key}:{value}\n"
# Send the email
#send_email(to="xyz@gmail.com", subject="Data Size Capture from Interface", body=body)





