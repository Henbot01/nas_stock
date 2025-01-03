from ftplib import FTP
from datetime import datetime
import os
import csv

def log_message_csv(log_file, message):
    #Helper function to log messages to a CSV file with SQL-compatible datetime.
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([timestamp, message])

def download_selected_files():
    # FTP server details
    ftp_host = "ftp.nasdaqtrader.com"
    ftp_user = "anonymous"
    ftp_pass = "guest"
    remote_dir = "/symboldirectory"
    local_dir = "./downloads"  # Local directory to save the files
    log_file = "./log.csv"  # Log file in CSV format

    # List of files to download
    target_files = {"nasdaqlisted.txt", "nasdaqtraded.txt", "mfundslist.txt"}

    log_message_csv(log_file, "Starting download process...")
    log_message_csv(log_file, "Connecting to the FTP server...")
    
    # Connect to the FTP server
    ftp = FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_pass)
    log_message_csv(log_file, "Connected successfully.")

    # Navigate to the desired directory
    ftp.cwd(remote_dir)
    log_message_csv(log_file, f"Navigated to directory: {remote_dir}")

    # List all files in the directory
    files = ftp.nlst()
    log_message_csv(log_file, f"Found {len(files)} files in {remote_dir}")

    # Ensure the local directory exists
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
        log_message_csv(log_file, f"Created local directory: {local_dir}")

    # Get today's date in YYYYMMDD format
    current_date = datetime.now().strftime("%Y%m%d")

    # Download only the target files
    for file in files:
        if file in target_files:
            # Prepend the current date to the file name
            new_file_name = f"{current_date}_{file}"
            local_file_path = os.path.join(local_dir, new_file_name)

            # Download the file
            log_message_csv(log_file, f"Downloading: {file}")
            with open(local_file_path, "wb") as local_file:
                ftp.retrbinary(f"RETR {file}", local_file.write)
            log_message_csv(log_file, f"Downloaded and saved as: {new_file_name}")

    # Close the FTP connection
    ftp.quit()
    log_message_csv(log_file, "Disconnected from the FTP server.")
    log_message_csv(log_file, "Selected files have been downloaded and renamed.")

if __name__ == "__main__":
    download_selected_files()