import datetime

channel_ovveride ='''@UCS

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


dict_month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'}

today_str = str(datetime.date.today().day) + '-' + dict_month[datetime.date.today().month] + '-' + str(datetime.date.today().year)

print('СЕГОДНЯ: ',datetime.datetime.today().replace(microsecond=0),'\n', 'ГРУЗИМ: ')



time = input('ВРЕМЯ (по умочанию: 12:00 - 12:03): ')
if time:
    AT = today_str + ' ' + time[0:5]
    ET = today_str + ' ' + time[8:]
    channel_ovveride = channel_ovveride.replace('DD-MMM-YYYY 12:00:00', AT)
    channel_ovveride = channel_ovveride.replace('DD-MMM-YYYY 12:03:00', ET)

else: channel_ovveride = channel_ovveride.replace('DD-MMM-YYYY', today_str)

with open(today_str + '_GO-ChS.SCR;1', 'w') as newfile:
    
    for string in channel_ovveride: newfile.write(string)
