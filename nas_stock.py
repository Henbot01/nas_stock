from ftplib import FTP, all_errors
import ftplib


#connection details
host = 'ftp.nasdaqtrader.com'
port = 21

usr = ''
passwrd = ''

local_file = '\mfunds' # local file directory path.
remote_dir = ''

filename = 'nasdaqlisted.txt'

with FTP(host = host, user = usr, passwd = passwrd) as ftp:
    # returns the welcome code, you want to see a 220
    print(ftp.getwelcome())
    # navigate to the symbol directory
    print(ftp.cwd('Symboldirectory'))
    print('----')
    #prints the files as a list
    files = []
    ftp.dir(files.append)
    for f in files:
        print(f)
    # downloads the daily securities list
    with open('nasdaqlisted.txt', 'w') as local_file:
        response = ftp.retrbinary("RETR " + filename,open(filename,'wb').write)
        if response.startswith('226'):
            print('Transfer complete')
        else:
            print('Error transferring')

#be nice ensure the closure of the connection to use elsehwere.
ftp.close()
