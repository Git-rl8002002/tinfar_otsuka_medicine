#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221116
# Update   : 20230307
# Version  : 1.2
# Function : 大塚製藥 get I6 sensor data value and put into NAS

import time , pymysql , platform , os , smtplib , datetime , pysftp as sftp
from pyModbusTCP.client import *
from control.dao import * 
from fpdf import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

##################################################################################################################################################
#
# main content - monitor
#
##################################################################################################################################################
class monitor():
    
    #########
    # init
    #########
    def __init__(self):
        self.conver_pdf()

    ######################
    # read sensor value
    ######################
    def conver_pdf(self):
        
        try:
            ###########################
            #
            # 大塚製藥 TXT conver PDF
            #
            ###########################
            
            ### record time
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime())
            self.conver_pdf_day = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")

            ### print msg
            print('----------------------------------------------------------------------------------------------')

            ##########################
            # conver PDF sensor S-1 
            ##########################
            try:
                ### variables
                self.s_txt = '_S-1.txt'
                self.s_pdf = '_S-1.pdf'
                self.path   = 'S1'
                self.err    = 'S-1'

                ''' diabled 20230306 old path name
                self.s_txt = '_S-1.txt'
                self.s_pdf = '_S-1.pdf'
                self.path   = 'S1'
                self.err    = 'S-1'
                '''

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-2
            ##########################
            try:
                ### variables
                self.s_txt = '_S-2.txt'
                self.s_pdf = '_S-2.pdf'
                self.path   = 'S2'
                self.err    = 'S-2'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-3
            ##########################
            try:
                ### variables
                self.s_txt = '_S-3.txt'
                self.s_pdf = '_S-3.pdf'
                self.path   = 'S3'
                self.err    = 'S-3'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-4
            ##########################
            try:
                ### variables
                self.s_txt = '_S-4.txt'
                self.s_pdf = '_S-4.pdf'
                self.path   = 'S4'
                self.err    = 'S-4'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-5
            ##########################
            try:
                ### variables
                self.s_txt = '_S-5.txt'
                self.s_pdf = '_S-5.pdf'
                self.path   = 'S5'
                self.err    = 'S-5'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-6
            ##########################
            try:
                ### variables
                self.s_txt = '_S-6.txt'
                self.s_pdf = '_S-6.pdf'
                self.path   = 'S6'
                self.err    = 'S-6'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-7
            ##########################
            try:
                ### variables
                self.s_txt = '_S-7.txt'
                self.s_pdf = '_S-7.pdf'
                self.path   = 'S7'
                self.err    = 'S-7'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-8
            ##########################
            try:
                ### variables
                self.s_txt = '_S-8.txt'
                self.s_pdf = '_S-8.pdf'
                self.path   = 'S8'
                self.err    = 'S-8'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-9
            ##########################
            try:
                ### variables
                self.s_txt = '_S-9.txt'
                self.s_pdf = '_S-9.pdf'
                self.path   = 'S9'
                self.err    = 'S-9'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            ##########################
            # conver PDF sensor S-10
            ##########################
            try:
                ### variables
                self.s_txt = '_S-10.txt'
                self.s_pdf = '_S-10.pdf'
                self.path   = 'S10'
                self.err    = 'S-10'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-11-1
            #############################
            try:
                ### variables
                self.s_txt = '_S-11-1.txt'
                self.s_pdf = '_S-11-1.pdf'
                self.path   = 'S11-1'
                self.err    = 'S-11-1'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-11-2
            #############################
            try:
                ### variables
                self.s_txt = '_S-11-2.txt'
                self.s_pdf = '_S-11-2.pdf'
                self.path  = 'S11-2'
                self.err   = 'S-11-2'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-12
            #############################
            try:
                ### variables
                self.s_txt = '_S-12.txt'
                self.s_pdf = '_S-12.pdf'
                self.path  = 'S12'
                self.err   = 'S-12'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-13
            #############################
            try:
                ### variables
                self.s_txt = '_S-13.txt'
                self.s_pdf = '_S-13.pdf'
                self.path  = 'S13'
                self.err   = 'S-13'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-14
            #############################
            try:
                ### variables
                self.s_txt = '_S-14.txt'
                self.s_pdf = '_S-14.pdf'
                self.path  = 'S14'
                self.err   = 'S-14'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-1
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-1.txt'
                self.s_pdf = '_S-15-1.pdf'
                self.path  = 'S15-1'
                self.err   = 'S-15-1'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-2
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-2.txt'
                self.s_pdf = '_S-15-2.pdf'
                self.path  = 'S15-2'
                self.err   = 'S-15-2'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-3
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-3.txt'
                self.s_pdf = '_S-15-3.pdf'
                self.path  = 'S15-3'
                self.err   = 'S-15-3'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-4
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-4.txt'
                self.s_pdf = '_S-15-4.pdf'
                self.path  = 'S15-4'
                self.err   = 'S-15-4'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-5
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-5.txt'
                self.s_pdf = '_S-15-5.pdf'
                self.path  = 'S15-5'
                self.err   = 'S-15-5'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-15-6
            #############################
            try:
                ### variables
                self.s_txt = '_S-15-6.txt'
                self.s_pdf = '_S-15-6.pdf'
                self.path  = 'S15-6'
                self.err   = 'S-15-6'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-16
            #############################
            try:
                ### variables
                self.s_txt = '_S-16.txt'
                self.s_pdf = '_S-16.pdf'
                self.path  = 'S16'
                self.err   = 'S-16'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-17
            #############################
            try:
                ### variables
                self.s_txt = '_S-17.txt'
                self.s_pdf = '_S-17.pdf'
                self.path  = 'S17'
                self.err   = 'S-17'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))
            
            #############################
            # conver PDF sensor S-18
            #############################
            try:
                ### variables
                self.s_txt = '_S-18.txt'
                self.s_pdf = '_S-18.pdf'
                self.path  = 'S18'
                self.err   = 'S-18'

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial' , size=10)

                #for num in range(1,11):
                f =  open("/var/www/html/medicine/txt/" + self.conver_pdf_day + self.s_txt , "r")

                for x in f:
                    ### 中文會顯示亂碼，全部改成英文位置
                    #pdf.cell(200 , 10 , txt = x.encode('utf8').decode('latin1') , ln = 1 , align = 'L')
                    
                    ### 只顯示英文
                    pdf.cell(200 , 10 , txt = x , ln = 1 , align = 'L')

                pdf.output('/var/www/html/medicine/pdf/nas/' + self.path + '/' + self.conver_pdf_day + self.s_pdf)
            
                ### print msg
                print(self.r_time + ' , ' + self.conver_pdf_day + self.s_txt  + ' conver PDF successful.')

            except Exception as e:
                print('< Error >  conver PDF  ' + self.err + ' : ' + str(e))

            print('----------------------------------------------------------------------------------------------')

            ###################
            # put PDF in NAS
            ###################
            try:
                cnopts = sftp.CnOpts()
                cnopts.hostkeys = None
                
                print('----------------------------------------------------------------------------------------------')

                #######
                # S-1
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s1'])
                    self.sftp.put(nas_para['linux_path_s1']+self.conver_pdf_day + '_S-1.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-1-25.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-1-25.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-1.pdf' , self.conver_pdf_day + '_WHFP-1-25.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-1.pdf' , self.conver_pdf_day + '_WHFP-1-25.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-1(WHFP-1-25).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-1(WHFP-1-25)')
                except Exception as e:
                    print('< Error > SFTP S-1(WHFP-1-25) : ' + str(e))
                
                #######
                # S-2
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s2'])
                    self.sftp.put(nas_para['linux_path_s2']+self.conver_pdf_day+'_S-2.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-1-30.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-1-30.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-2.pdf' , self.conver_pdf_day + '_WHFP-1-30.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-2.pdf' , self.conver_pdf_day + '_WHFP-1-30.pdf')
                    
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-2(WHFP-1-30).pdf.pdf sftp put NAS successful.')
                    #self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-2(WHFP-1-30)')
                except Exception as e:
                    print('< Error > SFTP S-2(WHFP-1-30) : ' + str(e))

                #######
                # S-3
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s3'])
                    self.sftp.put(nas_para['linux_path_s3']+self.conver_pdf_day+'_S-3.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHR-1.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHR-1.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-3.pdf' , self.conver_pdf_day + '_WHR-1.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-3.pdf' , self.conver_pdf_day + '_WHR-1.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-3(WHR-1).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-3(WHR-1)')
                except Exception as e:
                    print('< Error > SFTP S-3(WHR-1) : ' + str(e))

                #######
                # S-4
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s4'])
                    self.sftp.put(nas_para['linux_path_s4']+self.conver_pdf_day+'_S-4.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-3-30-C.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-3-30-C.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-4.pdf' , self.conver_pdf_day + '_WHFP-3-30-C.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-4.pdf' , self.conver_pdf_day + '_WHFP-3-30-C.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-4(WHFP-3-30-C).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-4(WHFP-3-30-C)')
                except Exception as e:
                    print('< Error > SFTP S-4(WHFP-3-30-C) : ' + str(e))

                #######
                # S-5
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s5'])
                    self.sftp.put(nas_para['linux_path_s5']+self.conver_pdf_day+'_S-5.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-3-30-B.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-3-30-B.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-5.pdf' , self.conver_pdf_day + '_WHFP-3-30-B.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-5.pdf' , self.conver_pdf_day + '_WHFP-3-30-B.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-5(WHFP-3-30-B).pdf.pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-5(WHFP-3-30-B)')
                except Exception as e:
                    print('< Error > SFTP S-5(WHFP-3-30-B) : ' + str(e))

                #######
                # S-6
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s6'])
                    self.sftp.put(nas_para['linux_path_s6']+self.conver_pdf_day+'_S-6.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-3-25.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-3-25.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-6.pdf' , self.conver_pdf_day + '_WHFP-3-25.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-6.pdf' , self.conver_pdf_day + '_WHFP-3-25.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-6(WHFP-3-25).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-6(WHFP-3-25)')
                except Exception as e:
                    print('< Error > SFTP S-6(WHFP-3-25) : ' + str(e))

                #######
                # S-7
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s7'])
                    self.sftp.put(nas_para['linux_path_s7']+self.conver_pdf_day+'_S-7.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-3-30-A.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-3-30-A.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-7.pdf' , self.conver_pdf_day + '_WHFP-3-30-A.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-7.pdf' , self.conver_pdf_day + '_WHFP-3-30-A.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-7(WHFP-3-30-A).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-7(WHFP-3-30-A)')
                except Exception as e:
                    print('< Error > SFTP S-7(WHFP-3-30-A) : ' + str(e))

                #######
                # S-8
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s8'])
                    self.sftp.put(nas_para['linux_path_s8']+self.conver_pdf_day+'_S-8.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-2.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-2.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-8.pdf' , self.conver_pdf_day + '_WHFP-2.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-8.pdf' , self.conver_pdf_day + '_WHFP-2.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-8(WHFP-2).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-8(WHFP-2)')
                except Exception as e:
                    print('< Error > SFTP S-8(WHFP-2) : ' + str(e))

                #######
                # S-9
                #######
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s9'])
                    self.sftp.put(nas_para['linux_path_s9']+self.conver_pdf_day+'_S-9.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHR-2.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHR-2.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-9.pdf' , self.conver_pdf_day + '_WHR-2.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-9.pdf' , self.conver_pdf_day + '_WHR-2.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-9(WHR-2).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-9(WHR-2)')
                except Exception as e:
                    print('< Error > SFTP S-9(WHR-2) : ' + str(e))

                ########
                # S-10
                ########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s10'])
                    self.sftp.put(nas_para['linux_path_s10']+self.conver_pdf_day+'_S-10.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHM.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHM.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-10.pdf' , self.conver_pdf_day + '_WHM.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-10.pdf' , self.conver_pdf_day + '_WHM.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-10(WHM).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-10(WHM)')
                except Exception as e:
                    print('< Error > SFTP S-10(WHM) : ' + str(e))

                ##########
                # S-11-1
                ##########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s11-1'])
                    self.sftp.put(nas_para['linux_path_s11-1']+self.conver_pdf_day+'_S-11-1.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SR-1.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SR-1.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-11-1.pdf' , self.conver_pdf_day + '_SR-1.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-11-1.pdf' , self.conver_pdf_day + '_SR-1.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-11-1(SR-1).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-11-1(SR-1)')
                except Exception as e:
                    print('< Error > SFTP S-11-1(SR-1) : ' + str(e))

                ##########
                # S-11-2
                ##########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s11-2'])
                    self.sftp.put(nas_para['linux_path_s11-2']+self.conver_pdf_day+'_S-11-2.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SR-1-CS.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SR-1-CS.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-11-2.pdf' , self.conver_pdf_day + '_SR-1-CS.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-11-2.pdf' , self.conver_pdf_day + '_SR-1-CS.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-11-2(SR-1-CS).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-11-2(SR-1-CS)')
                except Exception as e:
                    print('< Error > SFTP S-11-2(SR-1-CS) : ' + str(e))

                ########
                # S-12
                ########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s12'])
                    self.sftp.put(nas_para['linux_path_s12']+self.conver_pdf_day+'_S-12.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SR-2.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SR-2.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-12.pdf' , self.conver_pdf_day + '_SR-2.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-12.pdf' , self.conver_pdf_day + '_SR-2.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-12(SR-2).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-12(SR-2)')
                except Exception as e:
                    print('< Error > SFTP S-12(SR-2) : ' + str(e))

                ########
                # S-13
                ########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s13'])
                    self.sftp.put(nas_para['linux_path_s13']+self.conver_pdf_day+'_S-13.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SR-2-CS.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SR-2-CS.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-13.pdf' , self.conver_pdf_day + '_SR-2-CS.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-13.pdf' , self.conver_pdf_day + '_SR-2-CS.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-13(SR-2-CS).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-13(SR-2-CS)')
                except Exception as e:
                    print('< Error > SFTP S-13(SR-2-CS) : ' + str(e))

                ########
                # S-14
                ########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s14'])
                    self.sftp.put(nas_para['linux_path_s14']+self.conver_pdf_day+'_S-14.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHRE.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHRE.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-14.pdf' , self.conver_pdf_day + '_WHRE.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-14.pdf' , self.conver_pdf_day + '_WHRE.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-14(WHRE).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-14(WHRE)')
                except Exception as e:
                    print('< Error > SFTP S-14(WHRE) : ' + str(e))

                ##########
                # S-15-1
                ##########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s15-1'])
                    self.sftp.put(nas_para['linux_path_s15-1']+self.conver_pdf_day+'_S-15-1.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SB-1.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SB-1.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-15-1.pdf' , self.conver_pdf_day + '_SB-1.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-15-1.pdf' , self.conver_pdf_day + '_SB-1.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-1(SB-1).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-15-1(SB-1)')
                except Exception as e:
                    print('< Error > SFTP S-15-1(SB-1) : ' + str(e))

                ##########
                # S-15-2
                ##########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s15-2'])
                    self.sftp.put(nas_para['linux_path_s15-2']+self.conver_pdf_day+'_S-15-2.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SB-2.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SB-2.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-15-2.pdf' , self.conver_pdf_day + '_SB-2.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-15-2.pdf' , self.conver_pdf_day + '_SB-2.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-2.pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-15-2(SB-2)')
                except Exception as e:
                    print('< Error > SFTP S-15-2(SB-2) : ' + str(e))

                ##########
                # S-15-3
                ##########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s15-3'])
                    self.sftp.put(nas_para['linux_path_s15-3']+self.conver_pdf_day+'_S-15-3.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SB-3.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SB-3.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-15-3.pdf' , self.conver_pdf_day + '_SB-3.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-15-3.pdf' , self.conver_pdf_day + '_SB-3.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-3(SB-3).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-15-3(SB-3)')
                except Exception as e:
                    print('< Error > SFTP S-15-3(SB-3) : ' + str(e))

                ##########
                # S-15-4
                ##########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s15-4'])
                    self.sftp.put(nas_para['linux_path_s15-4']+self.conver_pdf_day+'_S-15-4.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SB-4.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SB-4.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-15-4.pdf' , self.conver_pdf_day + '_SB-4.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-15-4.pdf' , self.conver_pdf_day + '_SB-4.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-4(SB-4).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-15-4(SB-4)')
                except Exception as e:
                    print('< Error > SFTP S-15-4(SB-4) : ' + str(e))

                ##########
                # S-15-5
                ##########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s15-5'])
                    self.sftp.put(nas_para['linux_path_s15-5']+self.conver_pdf_day+'_S-15-5.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SB-5.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SB-5.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-15-5.pdf' , self.conver_pdf_day + '_SB-5.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-15-5.pdf' , self.conver_pdf_day + '_SB-5.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-5(SB-5).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-15-5(SB-5)')
                except Exception as e:
                    print('< Error > SFTP S-15-5(SB-5) : ' + str(e))

                ##########
                # S-15-6
                ##########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s15-6'])
                    self.sftp.put(nas_para['linux_path_s15-6']+self.conver_pdf_day+'_S-15-6.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_SB-6.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_SB-6.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-15-6.pdf' , self.conver_pdf_day + '_SB-6.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-15-6.pdf' , self.conver_pdf_day + '_SB-6.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-15-6(SB-6).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-15-6(SB-6)')
                except Exception as e:
                    print('< Error > SFTP S-15-6(SB-6) : ' + str(e))

                ########
                # S-16
                ########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s16'])
                    self.sftp.put(nas_para['linux_path_s16']+self.conver_pdf_day+'_S-16.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WIP.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WIP.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-16.pdf' , self.conver_pdf_day + '_WIP.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-16.pdf' , self.conver_pdf_day + '_WIP.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-16(WIP).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-16(WIP)')
                except Exception as e:
                    print('< Error > SFTP S-16(WIP) : ' + str(e))

                ########
                # S-17
                ########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s17'])
                    self.sftp.put(nas_para['linux_path_s17']+self.conver_pdf_day+'_S-17.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-2-CS.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-2-CS.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-17.pdf' , self.conver_pdf_day + '_WHFP-2-CS.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-17.pdf' , self.conver_pdf_day + '_WHFP-2-CS.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-17(WHFP-2-CS).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-17(WHFP-2-CS)')
                except Exception as e:
                    print('< Error > SFTP S-17(WHFP-2-CS) : ' + str(e))

                ########
                # S-18
                ########
                try:
                    self.sftp = sftp.Connection(host=nas_para['host'] , username=nas_para['user'] , password=nas_para['pwd'] , port=nas_para['port'] , cnopts=cnopts)
                    self.sftp.chdir(nas_para['nas_path_s18'])
                    self.sftp.put(nas_para['linux_path_s18']+self.conver_pdf_day+'_S-18.pdf')
                    if self.sftp.isfile(self.conver_pdf_day + '_WHFP-3-CS.pdf'):
                        self.sftp.remove(self.conver_pdf_day + '_WHFP-3-CS.pdf')
                        self.sftp.rename(self.conver_pdf_day + '_S-18.pdf' , self.conver_pdf_day + '_WHFP-3-CS.pdf')
                    else:
                        self.sftp.rename(self.conver_pdf_day + '_S-18.pdf' , self.conver_pdf_day + '_WHFP-3-CS.pdf')
                    ### print msg
                    print(self.r_time + ' , ' + self.conver_pdf_day + '_S-18(WHFP-3-CS).pdf sftp put NAS successful.')
                    self.sftp.close()
                    ### backup record
                    self.backup_pdf_nas('S-18(WHFP-3-CS)')
                except Exception as e:
                    print('< Error > SFTP S-18(WHFP-3-CS) : ' + str(e))

            except Exception as e:
                print('< Error > Sftp put NAS Error : ' + str(e))
            
            ### print msg
            print('----------------------------------------------------------------------------------------------')
            
        except Exception as e:
            print('< Error > conver_pdf : ' + str(e))

    ###################
    # backup_pdf_nas
    ###################
    def backup_pdf_nas(self , sensor):
        
        ### variables
        self.sensor  = sensor
        self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
        self.r_year  = time.strftime("%Y" , time.localtime())
        self.r_month = time.strftime("%Y-%m" , time.localtime())
        self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
        self.backup_pdf_day    = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        self.os_sys            = platform.system()
        self.record_backup_nas = self.r_time + ' , ' + self.backup_pdf_day + '_' + self.sensor +'.pdf\n'
        self.pdf               = self.backup_pdf_day + '_' + self.sensor  + '.pdf'
        
        ##################
        # write to file
        ##################
        
        ### save file path - Linux
        try:
            if self.os_sys == 'Linux':
                
                ### check txt document exists
                #self.floderpath = txt_path['linux_txt_path'] + self.r_month
                #try:
                    #os.makedirs(self.floderpath)
                #except FileExistsError:

                self.add = open(txt_path['linux_pdf_path'] ,'a')
                self.add.write(self.record_backup_nas)
                self.add.close()

                ### insert into txt
                print(str(self.r_time) + ' , record backup ' + str(self.pdf) + ' to NAS txt log successful.')
        except Exception as e:
            print('< Error > record backup PDF to NAS txt log : ' + str(e))
        
        try:
            ###################
            # write to MySQL
            ###################

            ### insert into MySQL by this month
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()

            self.sql2 = "insert into backup_record(r_time,backup_time) value('{0}','{1}')".format(self.r_time , self.pdf)
            self.curr2.execute(self.sql2)
            self.conn2.commit()
            self.conn2.close()
            
            ### insert into database
            print(str(self.r_time) + ' , record backup ' + str(self.pdf) + ' to NAS DB log successful.\n')

        except Exception as e:
            print('< Error > record backup PDF to NAS DB log : ' + str(e))
        finally:
            pass

#######################################################################################################################################
#
# start
#
#######################################################################################################################################
if __name__ == '__main__':
    realtime = monitor()
