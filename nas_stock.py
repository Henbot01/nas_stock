from ftplib import FTP
from datetime import datetime
import os

def download_selected_files():
    # FTP server details    
    ftp_host = "ftp.nasdaqtrader.com"
    ftp_user = "anonymous"
    ftp_pass = "guest"
    remote_dir = "/symboldirectory"
    local_dir = "./Downloads"  # Local directory to save the files

    # List of files to download
    target_files = {"nasdaqlisted.txt", "nasdaqtraded.txt", "mfundslist.txt"}

    # Connect to the FTP server
    ftp = FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_pass)

    # Navigate to the desired directory
    ftp.cwd(remote_dir)

    # List all files in the directory
    files = ftp.nlst()
    print(f"Found {len(files)} files in {remote_dir}")

    # Ensure the local directory exists
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # Get today's date in YYYYMMDD format
    current_date = datetime.now().strftime("%Y%m%d")

    # Download only the target files
    for file in files:
        if file in target_files:
            # Prepend the current date to the file name
            new_file_name = f"{current_date}_{file}"
            local_file_path = os.path.join(local_dir, new_file_name)

            # Download the file
            with open(local_file_path, "wb") as local_file:
                ftp.retrbinary(f"RETR {file}", local_file.write)
            print(f"Downloaded and saved as: {new_file_name}")

    # Close the FTP connection
    ftp.quit()
    print("Selected files have been downloaded and renamed.")

if __name__ == "__main__":
    download_selected_files()
