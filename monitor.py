#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Author   : JasonHung
# Date     : 20221116
# Update   : 20230309
# Version  : 1.2.1
# Function : 大塚製藥 get I6 sensor value

import time , pymysql , platform , os , requests
from pyModbusTCP.client import *
from control.dao import * 
from fpdf import *

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
        self.sensor()

    ######################
    # read sensor value
    ######################
    def sensor(self):
        
        try:
            #########
            # loop
            #########
            #while True:
                
                ##############################
                #
                # 大塚製藥 I6-1 by modbusTCP 
                #
                ##############################
                try:
                    self.i6 = ModbusClient(host=m_i6_tcp_connect['ip'],port=m_i6_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = m_i6_tcp_param['kind']
                    self.s_protocol   = m_i6_tcp_param['protocol']
                    self.s_position   = m_i6_tcp_param['position']
                    self.s_position_n = m_i6_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### s16 temp
                    self.i6_val1 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s16-temp'],16),1)
                    ### s16 rh
                    self.i6_val2 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s16-rh'],16),1)
                    ### s11-1 temp
                    self.i6_val3 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s11-1-temp'],16),1)
                    ### s11-1 rh
                    self.i6_val4 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s11-1-rh'],16),1)
                    ### s11-2 temp
                    self.i6_val5 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s11-2-temp'],16),1)
                    ### s12 temp
                    self.i6_val6 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s12-temp'],16),1)
                    ### s12 rh
                    self.i6_val7 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s12-rh'],16),1)
                    ### s13 temp
                    self.i6_val8 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s13-temp'],16),1)
                    ### s13 rh
                    self.i6_val9 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s13-rh'],16),1)
                    ### s15-1 temp
                    self.i6_val10 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-1-temp'],16),1)
                    ### s15-1 rh
                    self.i6_val11 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-1-rh'],16),1)
                    ### s15-2 temp
                    self.i6_val12 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-2-temp'],16),1)
                    ### s15-2 rh
                    self.i6_val13 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-2-rh'],16),1)
                    ### s15-3 temp
                    self.i6_val14 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-3-temp'],16),1)
                    ### s15-3 rh
                    self.i6_val15 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-3-rh'],16),1)
                    ### s15-4 temp
                    self.i6_val16 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-4-temp'],16),1)
                    ### s15-4 rh
                    self.i6_val17 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-4-rh'],16),1)
                    ### s15-5 temp
                    self.i6_val18 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-5-temp'],16),1)
                    ### s15-5 rh
                    self.i6_val19 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-5-rh'],16),1)
                    ### s15-6 temp
                    self.i6_val20 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-6-temp'],16),1)
                    ### s15-6 rh
                    self.i6_val21 = self.i6.read_input_registers(int(m_i6_tcp_sensor['s15-6-rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position_n + '\n\n'
                          'S16-TEMP : ' + str(self.i6_val1[0]/10) + ' °C , S16-RH : ' + str(self.i6_val2[0]/10) + ' % ' + '\n'
                          'S11-1-TEMP : ' + str(self.i6_val3[0]/10) + ' °C , S11-1-RH : ' + str(self.i6_val4[0]/10) + ' % ' + '\n'
                          'S11-2-TEMP : ' + str(self.i6_val5[0]/10) + ' °C ' + '\n'
                          'S12-TEMP : ' + str(self.i6_val6[0]/10) + ' °C , S12-RH : ' + str(self.i6_val7[0]/10) + ' % ' +'\n'
                          'S13-TEMP : ' + str(self.i6_val8[0]/10) + ' °C , S13-RH : ' + str(self.i6_val9[0]/10) + ' % ' + '\n'
                          'S15-1-TEMP : ' + str(self.i6_val10[0]/10) + ' °C , S15-1-RH : ' + str(self.i6_val11[0]/10) + ' % ' +'\n'
                          'S15-2-TEMP : ' + str(self.i6_val12[0]/10) + ' °C , S15-2-RH : ' + str(self.i6_val13[0]/10) + ' % ' +'\n'
                          'S15-3-TEMP : ' + str(self.i6_val14[0]/10) + ' °C , S15-3-RH : ' + str(self.i6_val15[0]/10) + ' % ' +'\n'
                          'S15-4-TEMP : ' + str(self.i6_val16[0]/10) + ' °C , S15-4-RH : ' + str(self.i6_val17[0]/10) + ' % ' +'\n'
                          'S15-5-TEMP : ' + str(self.i6_val18[0]/10) + ' °C , S15-5-RH : ' + str(self.i6_val19[0]/10) + ' % ' +'\n'
                          'S15-6-TEMP : ' + str(self.i6_val20[0]/10) + ' °C , S15-6-RH : ' + str(self.i6_val21[0]/10) + ' % ' +'\n')
                    
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_protocol + ' , ' + self.s_kind + ' \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , 0 , 0 , 0 , 0 ,  'ok')    

                except Exception as e:
                    print('< Error > I6-1 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()
                
                #######################################
                # 大塚製藥 I6-1 / S-11-1 by modbusTCP 
                #######################################
                try:
                    self.i6 = ModbusClient(host=s_11_tcp_connect_1['ip'],port=s_11_tcp_connect_1['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_11_tcp_param_1['kind']
                    self.s_protocol   = s_11_tcp_param_1['protocol']
                    self.s_position   = s_11_tcp_param_1['position']
                    self.s_position_n = s_11_tcp_param_1['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_11_tcp_sensor_1['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_11_tcp_sensor_1['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(str(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % '))
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-11-1 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                #######################################
                # 大塚製藥 I6-1 / S-11-2 by modbusTCP 
                #######################################
                try:
                    self.i6 = ModbusClient(host=s_11_tcp_connect_2['ip'],port=s_11_tcp_connect_2['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_11_tcp_param_2['kind']
                    self.s_protocol   = s_11_tcp_param_2['protocol']
                    self.s_position   = s_11_tcp_param_2['position']
                    self.s_position_n = s_11_tcp_param_2['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_11_tcp_sensor_2['temp'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time  + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , 0 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-11-2 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ###################################
                # 大塚製藥 I6-1 / S-12 by modbusTCP 
                ###################################
                try:
                    self.i6 = ModbusClient(host=s_12_tcp_connect['ip'],port=s_12_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_12_tcp_param['kind']
                    self.s_protocol   = s_12_tcp_param['protocol']
                    self.s_position   = s_12_tcp_param['position']
                    self.s_position_n = s_12_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_12_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_12_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %\n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-12 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ###################################
                # 大塚製藥 I6-1 / S-13 by modbusTCP 
                ###################################
                try:
                    self.i6 = ModbusClient(host=s_13_tcp_connect['ip'],port=s_13_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_13_tcp_param['kind']
                    self.s_protocol   = s_13_tcp_param['protocol']
                    self.s_position   = s_13_tcp_param['position']
                    self.s_position_n = s_13_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_13_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_13_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %\n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-13 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                #######################################
                # 大塚製藥 I6-1 / S-15-1 by modbusTCP 
                #######################################
                try:
                    self.i6 = ModbusClient(host=s_15_tcp_connect_1['ip'],port=s_15_tcp_connect_1['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_15_tcp_param_1['kind']
                    self.s_protocol   = s_15_tcp_param_1['protocol']
                    self.s_position   = s_15_tcp_param_1['position']
                    self.s_position_n = s_15_tcp_param_1['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_15_tcp_sensor_1['temp1'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_15_tcp_sensor_1['rh1'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-15-1 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                #######################################
                # 大塚製藥 I6-1 / S-15-2 by modbusTCP 
                #######################################
                try:
                    self.i6 = ModbusClient(host=s_15_tcp_connect_2['ip'],port=s_15_tcp_connect_2['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_15_tcp_param_2['kind']
                    self.s_protocol   = s_15_tcp_param_2['protocol']
                    self.s_position   = s_15_tcp_param_2['position']
                    self.s_position_n = s_15_tcp_param_2['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_15_tcp_sensor_2['temp2'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_15_tcp_sensor_2['rh2'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ' )
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-15-2 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()
                
                #######################################
                # 大塚製藥 I6-1 / S-15-3 by modbusTCP 
                #######################################
                try:
                    self.i6 = ModbusClient(host=s_15_tcp_connect_3['ip'],port=s_15_tcp_connect_3['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_15_tcp_param_3['kind']
                    self.s_protocol   = s_15_tcp_param_3['protocol']
                    self.s_position   = s_15_tcp_param_3['position']
                    self.s_position_n = s_15_tcp_param_3['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_15_tcp_sensor_3['temp3'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_15_tcp_sensor_3['rh3'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' ,  ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ' )
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-15-3 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                #######################################
                # 大塚製藥 I6-1 / S-15-4 by modbusTCP 
                #######################################
                try:
                    self.i6 = ModbusClient(host=s_15_tcp_connect_4['ip'],port=s_15_tcp_connect_4['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_15_tcp_param_4['kind']
                    self.s_protocol   = s_15_tcp_param_4['protocol']
                    self.s_position   = s_15_tcp_param_4['position']
                    self.s_position_n = s_15_tcp_param_4['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_15_tcp_sensor_4['temp4'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_15_tcp_sensor_4['rh4'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-15-4 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                #######################################
                # 大塚製藥 I6-1 / S-15-5 by modbusTCP 
                #######################################
                try:
                    self.i6 = ModbusClient(host=s_15_tcp_connect_5['ip'],port=s_15_tcp_connect_5['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_15_tcp_param_5['kind']
                    self.s_protocol   = s_15_tcp_param_5['protocol']
                    self.s_position   = s_15_tcp_param_5['position']
                    self.s_position_n = s_15_tcp_param_5['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_15_tcp_sensor_5['temp5'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_15_tcp_sensor_5['rh5'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , self.i6_val3[0]/10 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-15-5 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                #######################################
                # 大塚製藥 I6-1 / S-15-6 by modbusTCP 
                #######################################
                try:
                    self.i6 = ModbusClient(host=s_15_tcp_connect_6['ip'],port=s_15_tcp_connect_6['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_15_tcp_param_6['kind']
                    self.s_protocol   = s_15_tcp_param_6['protocol']
                    self.s_position   = s_15_tcp_param_6['position']
                    self.s_position_n = s_15_tcp_param_6['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_15_tcp_sensor_6['temp6'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_15_tcp_sensor_6['rh6'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-15-6 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ###################################
                # 大塚製藥 I6-1 / S-16 by modbusTCP 
                ###################################
                try:
                    self.i6 = ModbusClient(host=s_16_tcp_connect['ip'],port=s_16_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_16_tcp_param['kind']
                    self.s_protocol   = s_16_tcp_param['protocol']
                    self.s_position   = s_16_tcp_param['position']
                    self.s_position_n = s_16_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_16_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_16_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-1 / S-16 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()
                
                ##############################
                #
                # 大塚製藥 I6-2 by modbusTCP 
                #
                ##############################
                try:
                    self.i6 = ModbusClient(host=m_i6_tcp_connect_2['ip'],port=m_i6_tcp_connect_2['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = m_i6_tcp_param_2['kind']
                    self.s_protocol   = m_i6_tcp_param_2['protocol']
                    self.s_position   = m_i6_tcp_param_2['position']
                    self.s_position_n = m_i6_tcp_param_2['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### s17 temp
                    self.i6_val1 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s17-temp'],16),1)
                    ### s18 temp
                    self.i6_val2 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s18-temp'],16),1)
                    ### s1 temp
                    self.i6_val3 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s1-temp'],16),1)
                    ### s1 rh
                    self.i6_val4 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s1-rh'],16),1)
                    ### s2 temp
                    self.i6_val5 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s2-temp'],16),1)
                    ### s2 rh
                    self.i6_val6 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s2-rh'],16),1)
                    ### s3 temp
                    self.i6_val7 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s3-temp'],16),1)
                    ### s3 rh
                    self.i6_val8 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s3-rh'],16),1)
                    ### s4 temp
                    self.i6_val9 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s4-temp'],16),1)
                    ### s4 rh
                    self.i6_val10 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s4-rh'],16),1)
                    ### s5 temp
                    self.i6_val11 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s5-temp'],16),1)
                    ### s5 rh
                    self.i6_val12 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s5-rh'],16),1)
                    ### s6 temp
                    self.i6_val13 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s6-temp'],16),1)
                    ### s6 rh
                    self.i6_val14 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s6-rh'],16),1)
                    ### s7 temp
                    self.i6_val15 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s7-temp'],16),1)
                    ### s7 rh
                    self.i6_val16 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s7-rh'],16),1)
                    ### s8 temp
                    self.i6_val17 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s8-temp'],16),1)
                    ### s8 rh
                    self.i6_val18 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s8-rh'],16),1)
                    ### s9 temp
                    self.i6_val19 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s9-temp'],16),1)
                    ### s9 rh
                    self.i6_val20 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s9-rh'],16),1)
                    ### s10 temp
                    self.i6_val21 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s10-temp'],16),1)
                    ### s10 rh
                    self.i6_val22 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s10-rh'],16),1)
                    ### s14 temp
                    self.i6_val23 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s14-temp'],16),1)
                    ### s14 rh
                    self.i6_val24 = self.i6.read_input_registers(int(m_i6_tcp_sensor_2['s14-rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position_n + '\n\n'
                          'S17-TEMP : ' + str(self.i6_val1[0]/10) + ' °C ' + '\n'
                          'S18-TEMP : ' + str(self.i6_val2[0]/10) + ' °C ' + '\n'
                          'S1-TEMP : ' + str(self.i6_val3[0]/10) + ' °C , S1-RH : ' + str(self.i6_val4[0]/10) + ' % ' + '\n'
                          'S2-TEMP : ' + str(self.i6_val5[0]/10) + ' °C , S2-RH : ' + str(self.i6_val6[0]/10) + ' % ' + '\n'
                          'S3-TEMP : ' + str(self.i6_val7[0]/10) + ' °C , S3-RH : ' + str(self.i6_val8[0]/10) + ' % ' + '\n'
                          'S4-TEMP : ' + str(self.i6_val9[0]/10) + ' °C , S4-RH : ' + str(self.i6_val10[0]/10) + ' % ' + '\n'
                          'S5-TEMP : ' + str(self.i6_val11[0]/10) + ' °C , S5-RH : ' + str(self.i6_val12[0]/10) + ' % ' + '\n'
                          'S6-TEMP : ' + str(self.i6_val13[0]/10) + ' °C , S6-RH : ' + str(self.i6_val14[0]/10) + ' % ' + '\n'
                          'S7-TEMP : ' + str(self.i6_val15[0]/10) + ' °C , S7-RH : ' + str(self.i6_val16[0]/10) + ' % ' + '\n'
                          'S8-TEMP : ' + str(self.i6_val17[0]/10) + ' °C , S8-RH : ' + str(self.i6_val18[0]/10) + ' % ' + '\n'
                          'S9-TEMP : ' + str(self.i6_val19[0]/10) + ' °C , S9-RH : ' + str(self.i6_val20[0]/10) + ' % ' + '\n'
                          'S10-TEMP : ' + str(self.i6_val21[0]/10) + ' °C , S10-RH : ' + str(self.i6_val22[0]/10) + ' % ' + '\n'
                          'S14-TEMP : ' + str(self.i6_val23[0]/10) + ' °C , S14-RH : ' + str(self.i6_val24[0]/10) + ' % ' + '\n')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_protocol + ' , ' + self.s_kind + ' \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , 0 , 0 , 0 , 0 ,  'ok')    
                
                except Exception as e:
                    print('< Error > I6-2 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ####################################
                # 大塚製藥 I6-2 / S-1 by modbusTCP 
                ####################################
                try:
                    self.i6 = ModbusClient(host=s_1_tcp_connect['ip'],port=s_1_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_1_tcp_param['kind']
                    self.s_protocol   = s_1_tcp_param['protocol']
                    self.s_position   = s_1_tcp_param['position']
                    self.s_position_n = s_1_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_1_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_1_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-1 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ####################################
                # 大塚製藥 I6-2 / S-2 by modbusTCP 
                ####################################
                try:
                    self.i6 = ModbusClient(host=s_2_tcp_connect['ip'],port=s_2_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_2_tcp_param['kind']
                    self.s_protocol   = s_2_tcp_param['protocol']
                    self.s_position   = s_2_tcp_param['position']
                    self.s_position_n = s_2_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_2_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_2_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  +  ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-2 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ####################################
                # 大塚製藥 I6-2 / S-3 by modbusTCP 
                ####################################
                try:
                    self.i6 = ModbusClient(host=s_3_tcp_connect['ip'],port=s_3_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_3_tcp_param['kind']
                    self.s_protocol   = s_3_tcp_param['protocol']
                    self.s_position   = s_3_tcp_param['position']
                    self.s_position_n = s_3_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_3_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_3_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ' )
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-3 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ####################################
                # 大塚製藥 I6-2 / S-4 by modbusTCP 
                ####################################
                try:
                    self.i6 = ModbusClient(host=s_4_tcp_connect['ip'],port=s_4_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_4_tcp_param['kind']
                    self.s_protocol   = s_4_tcp_param['protocol']
                    self.s_position   = s_4_tcp_param['position']
                    self.s_position_n = s_4_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_4_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_4_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ' )
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-4 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ####################################
                # 大塚製藥 I6-2 / S-5 by modbusTCP 
                ####################################
                try:
                    self.i6 = ModbusClient(host=s_5_tcp_connect['ip'],port=s_5_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_5_tcp_param['kind']
                    self.s_protocol   = s_5_tcp_param['protocol']
                    self.s_position   = s_5_tcp_param['position']
                    self.s_position_n = s_5_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_5_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_5_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  +  ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ' )
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-5 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ####################################
                # 大塚製藥 I6-2 / S-6 by modbusTCP 
                ####################################
                try:
                    self.i6 = ModbusClient(host=s_6_tcp_connect['ip'],port=s_6_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_6_tcp_param['kind']
                    self.s_protocol   = s_6_tcp_param['protocol']
                    self.s_position   = s_6_tcp_param['position']
                    self.s_position_n = s_6_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_6_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_6_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  +  ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ' )
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-6 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ####################################
                # 大塚製藥 I6-2 / S-7 by modbusTCP 
                ####################################
                try:
                    self.i6 = ModbusClient(host=s_7_tcp_connect['ip'],port=s_7_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_7_tcp_param['kind']
                    self.s_protocol   = s_7_tcp_param['protocol']
                    self.s_position   = s_7_tcp_param['position']
                    self.s_position_n = s_7_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_7_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_7_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %' )
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % \n '
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-7 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ##################################
                # 大塚製藥 I6-2 / S-8 by modbusTCP 
                ##################################
                try:
                    self.i6 = ModbusClient(host=s_8_tcp_connect['ip'],port=s_8_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_8_tcp_param['kind']
                    self.s_protocol   = s_8_tcp_param['protocol']
                    self.s_position   = s_8_tcp_param['position']
                    self.s_position_n = s_8_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_8_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_8_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    #print(self.r_time + ' , ' + self.s_kind + ' / ' + self.s_position  + ' , ' + self.s_position_n  +  ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  +  ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    #self.add_content = self.r_time + ' , ' + self.s_protocol + ' , ' + self.s_kind + '/' + self.s_position  + ' , ' + self.s_position_n  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %\n'
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %\n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-8 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()
                
                ##################################
                # 大塚製藥 I6-2 / S-9 by modbusTCP 
                ##################################
                try:
                    self.i6 = ModbusClient(host=s_9_tcp_connect['ip'],port=s_9_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_9_tcp_param['kind']
                    self.s_protocol   = s_9_tcp_param['protocol']
                    self.s_position   = s_9_tcp_param['position']
                    self.s_position_n = s_9_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_9_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_9_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    #print(self.r_time + ' , ' + self.s_kind + ' / ' + self.s_position  + ' , ' + self.s_position_n  +  ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  +  ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    #self.add_content = self.r_time + ' , ' + self.s_protocol + ' , ' + self.s_kind + '/' + self.s_position  + ' , ' + self.s_position_n  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %\n'
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %\n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-9 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                #####################################
                # 大塚製藥 I6-2 / S-10 by modbusTCP 
                #####################################
                try:
                    self.i6 = ModbusClient(host=s_10_tcp_connect['ip'],port=s_10_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_10_tcp_param['kind']
                    self.s_protocol   = s_10_tcp_param['protocol']
                    self.s_position   = s_10_tcp_param['position']
                    self.s_position_n = s_10_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_10_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_10_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %\n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-10 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ##################################
                # 大塚製藥 I6-2 / S-14 by modbusTCP 
                ##################################
                try:
                    self.i6 = ModbusClient(host=s_14_tcp_connect['ip'],port=s_14_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_14_tcp_param['kind']
                    self.s_protocol   = s_14_tcp_param['protocol']
                    self.s_position   = s_14_tcp_param['position']
                    self.s_position_n = s_14_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_14_tcp_sensor['temp'],16),1)
                    ### 濕度 rh
                    self.i6_val2 = self.i6.read_input_registers(int(s_14_tcp_sensor['rh'],16),1)
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' % ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10) + ' °C , Humidity : ' + str(self.i6_val2[0]/10) + ' %\n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10 , self.i6_val2[0]/10 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-14 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ##################################
                # 大塚製藥 I6-2 / S-17 by modbusTCP 
                ##################################
                try:
                    self.i6 = ModbusClient(host=s_17_tcp_connect['ip'],port=s_17_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_17_tcp_param['kind']
                    self.s_protocol   = s_17_tcp_param['protocol']
                    self.s_position   = s_17_tcp_param['position']
                    self.s_position_n = s_17_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_17_tcp_sensor['temp'],16),1)
                    
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10-1) + ' °C ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10-1) + ' °C \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10-1 , 0 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-17 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()

                ##################################
                # 大塚製藥 I6-2 / S-18 by modbusTCP 
                ##################################
                try:
                    self.i6 = ModbusClient(host=s_18_tcp_connect['ip'],port=s_18_tcp_connect['port'],auto_open=True,auto_close=True,debug=False)

                    ### variables
                    self.s_kind       = s_18_tcp_param['kind']
                    self.s_protocol   = s_18_tcp_param['protocol']
                    self.s_position   = s_18_tcp_param['position']
                    self.s_position_n = s_18_tcp_param['position_n']
                    
                    ### record time
                    self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
                    self.r_year  = time.strftime("%Y" , time.localtime())
                    self.r_month = time.strftime("%Y-%m" , time.localtime())
                    self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
                    
                    ### 溫度 temp
                    self.i6_val1 = self.i6.read_input_registers(int(s_18_tcp_sensor['temp'],16),1)
                    
                    
                    ### print msg
                    print('----------------------------------------------------------------------------------------------')
                    print(self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10-1) + ' °C ')
                    
                    ### write to file & write to MySQL
                    self.add_content = self.r_time + ' , ' + self.s_kind + ' , ' + self.s_position  + ' , Temperature : ' + str(self.i6_val1[0]/10-1) + ' °C \n'
                    self.insert_db(self.add_content , self.r_time , self.r_year , self.r_month , self.r_day , self.s_protocol , self.s_kind , self.s_position , self.i6_val1[0]/10-1 , 0 , 0 , 0 , 0 ,  'ok')    
                except Exception as e:
                    print('< Error > I6-2 / S-18 , ' + self.s_position_n + ' : ' + str(e) + '\n')
                finally:
                    self.i6.close()
               
                #################
                # polling time
                #################
                #time.sleep(polling_time['sec'])

        except Exception as e:
            print('< Error > sensor : ' + str(e))
        finally:
            pass
    
    ##############
    # insert_db
    ##############
    def insert_db(self,add_content , r_time , r_year , r_month , r_day , protocol , kind , content , val1 , val2 , val3 , val4 , val5 , status):
        
        try:
            ##################
            # write to file
            ##################
            self.r_time  = time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
            self.r_year  = time.strftime("%Y" , time.localtime())
            self.r_month = time.strftime("%Y-%m" , time.localtime())
            self.r_day   = time.strftime("%Y-%m-%d" , time.localtime()) 
            self.os_sys  = platform.system()
            
            ### save file path - Linux
            if self.os_sys == 'Linux':
                
                self.add = open(txt_path['linux_txt_path'] + self.r_day + '_' + kind + '.txt','a')
                self.add.write(add_content)
                self.add.close()

                ### insert into txt
                print(str(r_time) + ' , insert into ' + str(self.r_day) + '.txt successful.')

            ###################
            # write to MySQL
            ###################
            self.r_time    = r_time
            self.r_year    = r_year
            self.r_month   = r_month
            self.r_day     = r_day
            self.kind      = kind
            self.content   = content 
            self.protocol  = protocol
            self.val1      = val1
            self.val2      = val2
            self.val3      = val3
            self.val4      = val4
            self.val5      = val5
            self.status    = status

            ### create table by month
            self.data = self.r_month.split('-')
            self.b_month = self.data[0]+'_'+self.data[1]

            ### insert into MySQL by this month
            self.conn2 = pymysql.connect(host=db_connect['host'],port=db_connect['port'],user=db_connect['user'],passwd=db_connect['pwd'],database=db_connect['db'],charset=db_connect['charset'])
            self.curr2 = self.conn2.cursor()

            try:
                self.build_sql = "create table {0}(no int not null primary key AUTO_INCREMENT,r_time datetime null,r_year varchar(100) null,r_month varchar(100) null,r_day varchar(100) null,s_kind varchar(200) null,s_content varchar(200) null,s_protocol varchar(200) null,val_1 varchar(200) null,val_2 varchar(200) null,val_3 varchar(200) null,val_4 varchar(200) null,val_5 varchar(200) null,val_6 varchar(200) null,val_7 varchar(200) null,val_8 varchar(200) null,val_9 varchar(200) null,val_10 varchar(200) null,val_11 varchar(200) null,val_12 varchar(200) null,val_13 varchar(200) null,val_14 varchar(200) null,val_15 varchar(200) null,val_16 varchar(200) null,val_17 varchar(200) null,val_18 varchar(200) null,val_19 varchar(200) null,val_20 varchar(200) null,val_21 varchar(200) null,val_22 varchar(200) null,val_23 varchar(200) null,val_24 varchar(200) null,val_25 varchar(200) null,r_status varchar(50) null)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci".format(self.b_month)
                self.curr2.execute(self.build_sql)
                self.conn2.commit()
                self.conn2.close()
            except Exception as e:
                self.sql2 = "insert into {0}(r_time,r_year,r_month,r_day,s_protocol,s_kind,s_content,val_1,val_2,val_3,val_4,val_5,r_status) value('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(self.b_month , self.r_time , self.r_year , self.r_month , self.r_day , self.protocol , self.kind , self.content , self.val1 , self.val2 , self.val3 , self.val4 , self.val5 , self.status)
                self.curr2.execute(self.sql2)
                self.conn2.commit()
                self.conn2.close()
            
            ### insert into database
            print(str(r_time) + ' , insert into ' + str(self.r_day) + ' database successful.')
            print('----------------------------------------------------------------------------------------------\n')

        except Exception as e:
            print('< Error > insert_db : ' + str(e))
        finally:
            pass

################################################################################################################################################
#
# start
#
################################################################################################################################################
if __name__ == '__main__':
    realtime = monitor()