#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221116
# Update   : 20230307
# Version  : 1.2
# Function : 大塚製藥 check db statistics

import time , pymysql , platform , os , smtplib , datetime , pysftp as sftp , sys
from pyModbusTCP.client import *
from control.dao import * 
from fpdf import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

################################################################################################################################################
#
# main content - monitor
#
################################################################################################################################################
class monitor():
    
    #########
    # init
    #########
    def __init__(self):
        pass
    
    #############
    # check_db
    #############
    def check_db_statistics(self , month):

        ### record time
        r_time    = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        r_year    = time.strftime("%Y" , time.localtime())
        r_month   = time.strftime("%Y_%m" , time.localtime())
        r_day     = time.strftime("%Y-%m-%d" , time.localtime())
        pre_r_day = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        
        conn = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
        curr = conn.cursor()

        try:
            if month == 0:
                ### by day statistics
                sql = "select r_day , count(*) as total from {0} group by r_day order by r_day desc".format(r_month)
                curr.execute(sql)
                res = curr.fetchall()
                
                for val in res:
                    print('Date : ' + str(val[0]) + ' , total : ' + str(val[1]))
                
                print('\n')

                ### by month statistics
                sql = "select r_month , count(*) as total from {0} group by r_month".format(r_month)
                curr.execute(sql)
                res = curr.fetchall()
                
                for val in res:
                    print('Date : ' + str(val[0]) + ' , total : ' + str(val[1]))
                
                print('\n')

            else:
                ### by day statistics
                sql = "select r_day , count(*) as total from {0} group by r_day order by r_day desc".format(month)
                curr.execute(sql)
                res = curr.fetchall()
                
                for val in res:
                    print('Date : ' + str(val[0]) + ' , total : ' + str(val[1]))

                print('\n')

                ### by month statistics
                sql = "select r_month , count(*) as total from {0} group by r_month".format(month)
                curr.execute(sql)
                res = curr.fetchall()
                
                for val in res:
                    print('Date : ' + str(val[0]) + ' , total : ' + str(val[1]))

                print('\n')

        except Exception as e:
            print('< Error > check db : ' + str(e))
        finally:
            conn.commit()
            conn.close()
    

################################################################################################################################################
#
# start
#
################################################################################################################################################
if __name__ == '__main__':

    check_db = monitor()

    if len(sys.argv) < 2:
        print("\n")
        print("#####################################################################################################")
        print("# 大塚製藥")
        print("# usage : (default this month date)")
        print("# \t check_monitor_db.py 2023_03")
        print("#")
        print("#####################################################################################################")
        check_db.check_db_statistics(0)
    else:
        check_db.check_db_statistics(sys.argv[1])
        
