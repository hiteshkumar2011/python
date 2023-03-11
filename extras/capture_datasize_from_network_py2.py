#!/usr/bin/env python
import smtplib
def send_email(to,subject,body):
    # Sender's email address and password
    smtp_user = "SMTP User"
    smtp_password = "SMTP PWD"
    sent_from = "abc@ts.com"
    # Receiver's email address
    to = [to]
    # Message to be sent
    email_text = "Subject:"+ subject+ "\n\n"+body
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
        print("Something went wrong..",e)

def read_network_stats():
    with open("/proc/net/dev") as f:
        lines = f.readlines()
    # Remove the header and footer lines
    lines = lines[2:-1]         #### Print the output after the trimming to check the interface 
    stats = {}
    for line in lines:
        # Split the line into columns
        columns = line.strip().split()
        # Extract the interface name and receive bytes
        global iface
        iface = columns[0].split(":")[0]
        recv_bytes = int(columns[1])
        tx_bytes = int(columns[9])
        # Store the results in a dictionary
        stats[iface+'_tx_bytes'] = tx_bytes
        stats[iface+'_rx_bytes'] = recv_bytes
    return stats

def main():
    stats = read_network_stats()
    body = ""
    body += "Transfer and  Receive Bytes For Interface From ElasticSearch LB- 10.12.209.71 interface "+iface +"\n\n"

    for keys in stats:
   # Convert the transfer & receive bytes to gigabytes
        recv_gb =  stats[keys]/ (1000.0 ** 3)
        body+= "Data Ingestion for ELK in Gigabyte  "+"-" + str(keys) +"  :"+ str(recv_gb)+" Gb"  +"\n\n"
#        #print("The interface is ",iface + ":", recv_gb + "GB" )
#        print("{} - {:.2f} GB".format(keys, recv_gb))
# Send the email
#    send_email(to="hitesh.talhilyani@emaratech.ae", subject="ELK DATA INGESTION FROM ES LB", body=body)
    send_email(to="xyz@gmail.com", subject="ELK DATA INGESTION FROM ES LB", body=body)

if __name__ == "__main__":
    main()
