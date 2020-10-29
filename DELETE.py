from glob import glob
import os
import ftplib

print('\nудаление файлов в текущей директории\n')
files_for_del = glob('*-???-*.SCR;1')
for file in files_for_del:
    
    #delete local files
    print('...deleting old .scr files in parent dir {}'.format(file))
    os.remove(file)
    
# удалять посредством FTP оказалось легче, чем TELNET.
# поэтому FTP

print('\nудаление файлов на серверах по ФТП\n')
for host in ['172.31.176.4', '172.31.177.4']:
    print(host,'\n')
    print("1. ftp = ftplib.FTP({}, 'ucsmanager', 'gotalife')".format(host))
    ftp = ftplib.FTP(host, 'ucsmanager', 'gotalife')

    print("2. ftp.delete('SYS$SYSDEVICE:[DC2.UCS.SCRIPT]*-*-*.scr;*'))")
    ftp.delete('SYS$SYSDEVICE:[DC2.UCS.SCRIPT]*-*-*.scr;*')

    print("3. ftp.delete('SYS$SYSDEVICE:[DC2.UCS.BULK]*-*-*.log;*'))")
    ftp.delete('SYS$SYSDEVICE:[DC2.UCS.BULK]*-*-*.log;*')

    print("4. ftp.delete('SYS$SYSDEVICE:[DC2.UCS.BULK]*-*-*.blk;*'))")
    ftp.delete('SYS$SYSDEVICE:[DC2.UCS.BULK]*-*-*.blk;*')
    
    ftp.quit()
    print("5. ftp.quit()\n")
