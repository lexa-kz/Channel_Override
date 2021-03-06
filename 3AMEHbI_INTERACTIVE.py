#!/usr/bin/env python3

# for Unix systems make executable: chmod +x filename

import datetime, time, sys
import ftplib, telnetlib

print('\nПРОГРАММА ЗАМЕЩЕНИЯ ДЛЯ ОБЛАСТНОГО ОДНОЧАСОВОГО ВЕЩАНИЯ\n','- '*25,'\n')

#-- стандартный шаблон:
channel_ovveride ='''@UCS

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 0;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 331;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 341;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 16:00:00;                    ! Activation Time
ET = DD-MMM-YYYY 16:20:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 211;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 1;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 331;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 343;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:00:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 213;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 2;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 302;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 303;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 3;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 326;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 301;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 4;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 327;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 304;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 5;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 329;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 306;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 6;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 355;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 311;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 7;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 360;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 302;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 8;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 389;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 300;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 9;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 403;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 17:15:00;                    ! Activation Time
ET = DD-MMM-YYYY 18:00:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 312;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 10;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 327;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 14:30:00;                    ! Activation Time
ET = DD-MMM-YYYY 14:31:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 1;                    ! Tier
}
'''

#-- субботняя добавка к пятнице:
channel_ovveride_SATURDAY ='''
CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 11;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 327;                    ! Destination channel channel number
}
AT = DD-SAT-YYYY 14:30:00;                    ! Activation Time
ET = DD-SAT-YYYY 14:31:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 1;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 12;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 331;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 341;                    ! Destination channel channel number
}
AT = DD-SAT-YYYY 16:00:00;                    ! Activation Time
ET = DD-SAT-YYYY 16:20:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 211;                    ! Tier
}
'''

#-- файл-шпаргалка для ручной загрузки
ch_ov_file='''
telnet 172.31.176.4
telnet 172.31.177.4


login: ucsmanager
password: gotalife



ucs_bulktxt


Log message contents (y or n)? y



г============================================¬
¦    !!!  И З М Е Н И Т Ь   Д А Т У  !!!   	                 ¦
L============================================-

sys$sysdevice:[dc2.ucs.bulk]DD-MMM-YYYY.blk
sys$sysdevice:[dc2.ucs.script]DD-MMM-YYYY.scr


Another file (y or n)? n



ucs_offbulk


File name (64 char max) :

sys$sysdevice:[dc2.ucs.bulk]DD-MMM-YYYY.blk

Y


- Проверить, лог-файл в директории [BULK].
	Если он пустой (размер - 0 kB), значит, что все ОК!



logout
'''

#-- шаблон для ГО ЧС
go_ch_s = '''@UCS

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 21;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 301;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 352;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 12:00:00;                    ! Activation Time
ET = DD-MMM-YYYY 12:03:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 610;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 22;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 303;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 352;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 12:00:00;                    ! Activation Time
ET = DD-MMM-YYYY 12:03:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 610;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 23;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 307;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 352;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 12:00:00;                    ! Activation Time
ET = DD-MMM-YYYY 12:03:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 610;                    ! Tier
}

CRC                    ! Create Retune/Channel Override Event
{
EVTNUM = 24;                    ! RCO Event Number
CNCL = 0;                    ! Cancel event
CHOVR
{
  ORGVCM = 311;                    ! Original channel VCM
  ORGVCN = 309;                    ! Original channel channel number
  DESTVCM = 311;                    ! Destination channel VCM
  DESTVCN = 352;                    ! Destination channel channel number
}
AT = DD-MMM-YYYY 12:00:00;                    ! Activation Time
ET = DD-MMM-YYYY 12:03:00;                    ! End Time
ERR = 0x0;                    ! Error timeout
GRPID = 0;                    ! Group ID
AIUSE = 1;                    ! Addressing Info usage
TIERS [0] = 610;                    ! Tier
}
'''

work_variant = int(input('\nВыберите вариант для замещения:\n1. Ежедневная программа замещений (в том числе ПТ+СБ)\n2. Будний день\n3. С редактированием шаблоноа\n4. ГО ЧС\n\n: '))

dict_month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'}

today_str = str(datetime.date.today().day) + '-' + dict_month[datetime.date.today().month] + '-' + str(datetime.date.today().year)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
tomorrow_str = str(tomorrow.day) + '-' + dict_month[tomorrow.month] + '-' + str(tomorrow.year)

#-- Выбор источника (ежедневный шаблон (внутр.,), внешний файл, шаблон ГО ЧС(внутр.))
to_work = ''

if work_variant == 4: to_work = go_ch_s

elif work_variant == 3:
    ent = input('\nотредактируйте файл ШАБЛОН_ДЛЯ_ПИТОН.SCR;1, сохраните, закройте, нажмите Enter')
    with open('ШАБЛОН_ДЛЯ_ПИТОН.SCR;1','r') as template:
        for lines in template:
            to_work = to_work + lines

elif work_variant == 2: to_work = channel_ovveride
    
else:
    if datetime.datetime.today().weekday() == 4:
        to_work = channel_ovveride + channel_ovveride_SATURDAY
    elif datetime.datetime.today().weekday() == 5 or datetime.datetime.today().weekday() == 6:
        print ('\nСЕГОДНЯ, ОДНАКО, ВЫХОДНЫЕ!!!')
        sys.exit()          
    else:
        to_work = channel_ovveride

print('\nСЕГОДНЯ: ',datetime.datetime.today().replace(microsecond=0),'\n'*2)

to_work = to_work.replace('DD-MMM-YYYY', today_str)
to_work = to_work.replace('DD-SAT-YYYY', tomorrow_str)

scr_file = today_str + '.SCR;1'
blk_file = today_str + '.BLK;1'
log_file = blk_file.replace('BLK','LOG')

with open(scr_file, 'w') as newfile:
    
    for string in to_work: newfile.write(string)


# Загрузка .SCR файла по FTP на KATEL2 и KATEL3
# - - - - - - - - - - - - - - - - - - - - - - - 
print('ГРУЗИМ ФАЙЛ: ', scr_file, ' по FTP на KATEL2 и KATEL3','\n')
KATEL2 = '172.31.176.4'
KATEL3 = '172.31.177.4'

path = 'sys$sysdevice:[dc2.ucs.script]'

ftp = ftplib.FTP(KATEL2, 'ucsmanager', 'gotalife')
ftp.cwd(path)
with open(scr_file, 'rb') as file:
    ftp.storbinary('STOR ' + scr_file, file)
ftp.close()


ftp = ftplib.FTP(KATEL3, 'ucsmanager', 'gotalife')
ftp.cwd(path)
with open(scr_file, 'rb') as file:
    ftp.storbinary('STOR ' + scr_file, file)
ftp.close()
print('... DONE!\n')

# ФАЙЛ-ШПАРГАЛКА ДЛЯ ЗАПУСКА СКРИПТОВ ПО TELNET 
# - - - - - - - - - - - - - - - - - - - - - - -  
ch_ov_file = ch_ov_file.replace('DD-MMM-YYYY', today_str)

with open('CHANNEL OVERRIDE.txt', 'w') as co_file:
    for string in ch_ov_file: co_file.write(string)



# TELNET
# - - - - - - - - - - - - - - -
print('\n','УДАЛЕННО ПО ТЕЛНЕТ ЗАПУСКАЕМ СКРИПТЫ','\n')
def telnet_script(host, hostname):
    print('\n на ', hostname, ':\n')
    rmt_scr_file = bytes(path + scr_file, 'utf-8')
    rmt_blk_file = bytes('sys$sysdevice:[dc2.ucs.bulk]' + blk_file, 'utf-8')
    rmt_log_file = bytes('dir ' + 'sys$sysdevice:[dc2.ucs.bulk]' + log_file + ' /size', 'utf-8')


    print('1. telnet({})'.format(host))
    telnet = telnetlib.Telnet(host)

    print('2. Username:')
    telnet.read_until(b'Username:')

    print('3. ucsmanager')
    telnet.write(b'ucsmanager\r\n')

    print('4. Password:')
    telnet.read_until(b'Password:')

    print('5. gotalife')
    telnet.write(b'gotalife\r\n')

    print('6. time.sleep(3)')
    time.sleep(3)

    print('7. (UCSMANAGER)$')
    telnet.read_until(b'(UCSMANAGER)$')

    #-- ucs_bulktxt
    print('8. ucs_bulktxt')
    telnet.write(b'ucs_bulktxt\r\n')
    print('9. time.sleep(1)')
    time.sleep(1)

    #-- Log message contents (y or n)? y
    print('10. Log message contents (y or n)?')
    telnet.read_until(b'?')
    print('11. y')
    telnet.write(b'y\r\n')
    print('12. time.sleep(1)')
    time.sleep(1)

    #-- Enter bulk file specification:
    print('13. Enter bulk file specification:')
    telnet.read_until(b'specification:')
    print('14. {}'.format(rmt_blk_file))
    telnet.write(rmt_blk_file + b'\r\n')
    print('15. time.sleep(3)')
    time.sleep(3)

    #-- Enter text file specification:
    print('16. Enter text file specification:')
    #telnet.read_until(b'specification:')
    print('17. {}'.format(rmt_scr_file))
    telnet.write(rmt_scr_file + b'\r\n')
    print('18. time.sleep(1)')
    time.sleep(1)

    #-- Another file (y or n)? n
    print('19. Another file (y or n)?')
    telnet.read_until(b'?')
    print('20. n')
    telnet.write(b'n\r\n')
    print('21. time.sleep(1)')
    time.sleep(1)

    #-- ucs_offbulk
    print('22. $')
    telnet.read_until(b'$')
    print('23. ucs_offbulk')
    telnet.write(b'ucs_offbulk\r\n')
    print('24. time.sleep(1)')
    time.sleep(1)

    #-- bulk-файл для обрабокти
    print('25. File name (64 char max) :')
    telnet.read_until(b':')
    print('26. {}'.format(rmt_blk_file))
    telnet.write(rmt_blk_file + b'\r\n')
    print('27. time.sleep(1)')
    time.sleep(1)

    #-- Y - для подтверждения
    print('28. Y')
    telnet.write(b'Y\r\n')
    print('29. (UCSMANAGER)$')
    telnet.read_until(b'(UCSMANAGER)$')
    print('30. time.sleep(1)')
    time.sleep(1)

    #-- проверка лог-файла на ошибки (если 0 - нет ошибок)
    #- - - - - - - - - - - - - - - - - - - - - - - - - - -
    print('31. {}'.format(rmt_log_file))
    telnet.write(rmt_log_file + b'\r\n')
    print('32. time.sleep(3)')
    time.sleep(3)

    print('33. ...проверка... \n')
    check_log = telnet.read_until(b'(UCSMANAGER)$')
    print(check_log, '\n')
    print(check_log.split()[-4] + b' ' + check_log.split()[-3], '\n', '`'*20)
    if check_log.split()[-4] == b'0': print('\n', hostname, ' (', host,')\n','БЕЗ ОШИБОК!!! \n ВСЁ ОТЛИЧНО!!! \n ЗАПИШИТЕ ВСЁ В ЖУРНАЛ!!!')
    else: print('ЕСТЬ ОШИБКИ!!! \n НУЖНА ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА!!!\n')

telnet_script(KATEL2, 'KATEL2')
telnet_script(KATEL3, 'KATEL3')

time.sleep(15)
