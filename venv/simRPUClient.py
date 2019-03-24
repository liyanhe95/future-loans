# #-*-coding:utf-8-*-
# # @time      :2019/1/2014:46
# # @Author   :lemon_hehe
# # @Email     :976621712@qq.com
# # @File      :test_login.py
# # @software:PyCharm Community Edition
#
#
# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
#
# __author__  = 'liusi'
# __date__    = "2014-09-18"
#
# import os, struct, threading, time
# from socket import *
# from ctypes import create_string_buffer
#
# # import tyrpu.network.udp_server
#
# local_addr = '192.168.12.143'
# rpu_serv_addr = "192.168.12.201"
# # rpu_serv_port = 9000 # rpu_serv_port = 9800   # IPC连接
# rpu_serv_port = 9000
#
# real_video_rcv_port = 16000
# real_audio_rcv_port = 16100
#
# sid = 1
# seq = 1
# BUFSIZE = 20480
#
# sock = socket(AF_INET, SOCK_STREAM)
#
# def close_RPU():
#     if sock:
#         sock.close()
#
# def login_RPU():
#     global seq
#     addr = (rpu_serv_addr, rpu_serv_port)
#     print('conn to ', rpu_serv_addr, rpu_serv_port)
#     sock.connect(addr)
#
#     s = struct.pack('<bHb4HbbH128s128sHH', 1, 3004, 12, 1, seq, 1, 276, 11, 0, 276-12,
#                     b'admin', b'teamway123456', 0, 0)
#     print('send login info')
#     sock.send(s)
#     seq = seq + 1
#
#     while 1:
#         pg_header = sock.recv(12)
#         l = [hex(int(i)) for i in pg_header]
#         print(" ".join(l))
#
#         version, code, headLen, attrCount, seq, sid, totalLen = struct.unpack('<bHbHHHH', pg_header)
#
#         if code != 3005:
#             if totalLen - 12 > 0:
#                 data = sock.recv(totalLen - 12)
#             continue
#
#         print('recv login rsp, code ', code, ', len ', totalLen)
#         data = sock.recv(totalLen - 12)
#
#         l = [hex(int(i)) for i in data]
#         print(" ".join(l))
#
#         # i = 0
#         #if i < totalLen-12:
#         #    print('%#x' % data(i))
#         #    print(' ')
#         #    if i>0 and i%16==0 :
#         #        print('\n')
#         #       i += 1
#         # attr, r, len, code, datalen = struct.unpack('<bbHii', data)
#         # print 'login return ', code
#         return
#
# def get_record_schedule():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHi', 1, 16005, 12, 1, seq, 1, 20, -86, 0, 8, 1)
#     print('send get record schedule command')
#     sock.send(s)
#     seq = seq + 1
#
#     pg_header = sock.recv(12)
#     version, code, headLen, attrCount, seq, sid, totalLen = struct.unpack('<bHbHHHH', pg_header)
#     data = sock.recv(BUFSIZE)
#     print('return ', len(data))
#
# def system_reboot():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHi', 1, 1127, 12, 0, seq, 1, 20, 1, 0, 8, 1)
#     print('control program reboot')
#     sock.send(s)
#     seq = seq + 1
#
#     # pg_header = sock.recv(12)
#     # version, code, headLen, attrCount, seq, sid, totalLen = struct.unpack('<bHbHHHH', pg_header)
#     # data = sock.recv(BUFSIZE)
#     # print 'return ', len(data)
#
# def system_control():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHi', 1, 1127, 12, 0, seq, 1, 20, 1, 0, 8, 1)
#     print('control program quit')
#     sock.send(s)
#     seq = seq + 1
#
#     # pg_header = sock.recv(12)
#     # version, code, headLen, attrCount, seq, sid, totalLen = struct.unpack('<bHbHHHH', pg_header)
#     # data = sock.recv(BUFSIZE)
#     # print 'return ', len(data)
#
# def door_control():
#     global seq
#     s = struct.pack('<bHbHHHHbbHI', 1, 3008, 12, 1, seq, 1, 20, 120, 0, 8, 'DacpCode')
#     print('门禁控制器')
#     sock.send(s)
#     seq = seq + 1
#
# def videodliagnose():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiiii', 1, 1303, 12, 1, seq, 1, 40, 133, 0, 24, 'iDevId', 'iTime',' iAlmItemNum',
#                     'iIvsType', 0, 2)
#     print('视频质量诊断信息上报')
#     sock.send(s)
#     seq = seq + 1
#
# def get_video_dliagnose():
#     global seq
#     s = struct.pack('<bHbHHHH', 1 ,1310, 12, 0, seq, 1, 12)
#     print('获取视频质量诊断任务')
#     sock.send(s)
#     seq = seq + 1
#
# def get_dliagnose_stop():
#     global seq
#     s = struct.pack('<bHbHHHHbbHii', 1, 1312, 12, 1, seq, 1, 24, 132, 0, 12, 'id', 0)
#     print('控制诊断任务的启停')
#     sock.send(s)
#     seq = seq + 1
#
# def dliagnose_result():
#     global seq
#     s = struct.pack('bHbHHHHbbHi', 1, 1314, 12, 1, seq, 1, 20, 134, 0, 8, '192.168.12.143')
#     print('查询诊断结果')
#     sock.send(s)
#     seq = seq + 1
#
# def viedo_integrity():
#     global seq
#     s = struct.pack('bHbHHHHbbHicc', 1, 1316, 12, 1, seq, 1, 22, 135, 0, 10, '192.168.12.143', '2019-3-21', '2019-3-22')
#     print('查询录像完整性')
#     sock.send(s)
#     seq = seq + 1
#
# def set_viedo_concentration():
#     global seq
#     s = struct.pack('bHbHHHH', 1, 1350, 12, 1, seq, 1, 12)
#     print('设置视频浓缩任务')
#     sock.send(s)
#     seq = seq + 1
#
# def get_viedo_concentration():
#     global seq
#     s = struct.pack('bHbHHHHbbH', 1, 1352, 12, 0, seq, 1, 12)
#     print('获取视频浓缩任务')
#     sock.send(s)
#     seq = seq + 1
#
# def control_viedo_concentration():
#     global seq
#     s = struct.pack('bHbHHHHbbHiii', 1, 1354, 12, 1, seq, 1, 28, 151, 0, 16,' iId', '192.168.12.143', 1)
#     print('控制视频浓缩任务')
#     sock.send(s)
#     seq = seq + 1
#
# def information_change():
#     global seq
#     s = struct.pack('bHbHHHHbbHqiiiiqiiqi', 1, 1361, 12, 0, seq, 1, 68, 66, 0, 56, 'iDevId', ' iAlmType',
#                    1, 'iCameraNum', ' iAlmOutNum', ' iSubCameraId', 'iPresetIndex', 0, ' iSubAlmoutId', 0)
#     print('  布撤防状态更改通知')
#     sock.send(s)
#     seq = seq + 1
#
# def get_once_equipment_message():
#     global seq
#     s = struct.pack('bHbHHHH', 1, 1365, 12, 0, seq, 1, 12)
#     print('获取一次设备信息')
#     sock.send(s)
#     seq = seq + 1
#
# def get_real_time_video():
#     global seq
#     s = struct.pack('bHbHHHHbbHqiii', 1, 1370, 12, 1, seq, 1, 36, 158, 0, 24, ' iDevId', 'X', 'Y', '')
#     print('获取热成像通道实时视频画面任意点的温度')
#     sock.send(s)
#     seq = seq + 1
#
# def get_infrared_():
#     global seq
#     s = struct.pack('bHbHHHHbbHqic', 1, 1372, 12, 1, seq, 1, 29, 159, 0, 17, 'iDevId', 'nlen', '')
#     print('获取热成像通道热图')
#     sock.send(s)
#     seq = seq + 1
#
# def get_patrol_scheme():
#     global seq
#     s = struct.pack('bHbHHHH', 1, 1374, 12, 0, seq, 1, 12)
#     print('获取巡检计划')
#     sock.send(s)
#     seq = seq + 1
#
# def control_patrol_scheme():
#     global seq
#     s = struct.pack('bHbHHHHbbHii', 1, 1376, 12, 1, seq, 1, 24, 156, 12, 'iId', 1)
#     print('控制巡检计划的请求报文')
#     sock.send(s)
#     seq = seq + 1
#
# def get_control_patrol_scheme():
#     global seq
#     s = struct.pack('bHbHHHHbbHii', 1, 1376, 12, 1, seq, 1, 24, )
#     print(' 控制巡检计划')
#     sock.send(s)
#     seq = seq + 1
#
# def send_patrol_result():
#     global seq
#     s = struct.pack('bHbHHHHbbHciciiiiicii', 1, 1378, 12, 1, seq, 1, 59, 157, 0, 47, '2019-3-21',' iElectricDevId', 'szElectricDevName',
#                     'iNum', ' iAnalyseType', ' iValue', 'iIsAlarm', 'iAlmLevel', 'szDes', 'szPicName', '192.168.12.143', ' iPtzId')
#     print('向主站发送巡检结果')
#     sock.send(s)
#     seq =seq + 1
#
# def setIPInfo():
#     global seq
#     s = struct.pack('<bHbHHHHbbHi32s32s128s32s', 1, 1011, 12, 1, seq, 1, 244, 1, 0, 232, 1,
#                     "192.168.12.77", "255.255.255.0", "192.168.12.1 192.168.12.2", "192.168.12.254")
#     print('set IP info')
#     sock.send(s)
#     seq = seq + 1
#
# def getIPInfo():
#     global seq
#     s = struct.pack('<bHbHHHH', 1, 1013, 12, 0, seq, 1, 12)
#     print('get IP info')
#     sock.send(s)
#     seq = seq + 1
#
# def setTime():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiiii', 1, 1071, 12, 1, seq, 1, 12+4+24, 1, 0, 4+24,
#                     2014, 12, 9, 16, 50, 1);
#     print('set Time')
#     sock.send(s)
#     seq = seq + 1
#
# def addUser():
#     global seq
#     i = 0
#     while (i<1):
#         password = "%s%d"%("password", i)
#         s = struct.pack('<bHbHHHHbbH128s128sHH', 1, 1021, 12, 1, seq, 1, 12+4+128+128+4, 11, 0, 4+128+128+4,
#                     "testrpu5", "password5", 2, 4);
#         print('add user')
#         sock.send(s)
#         seq = seq + 1
#         i = i + 1
#         time.sleep(3)
#     pass
#
# def setVideoEncode():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiiiiiii', 1, 1041, 12, 1, seq, 1, 12+4+36, 1, 0, 4+36,
#                     1, 16, 1, 1, 100, 20, 300, 100, 1);
#     print('set video encode info')
#     sock.send(s)
#     seq = seq + 1
#
# def setVideoMask():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiii', 1, 1241, 12, 1, seq, 1, 12+4+20, 1, 0, 4+20,
#                     1, 100, 100, 100, 100);
#     print('set video encode info')
#     sock.send(s)
#     seq = seq + 1
#
# def get_real_audio():
#     global seq
#     global real_audio_rcv_port
#
#     # start udp server
#     us = tyrpu.network.udp_server.UDPServer(real_audio_rcv_port)
#     us.init_server()
#     us.start_recv()
#
#     # send pg command
#     s = struct.pack('<bHbHHHHbbHiii32si32sii', 1, 2203, 12, 1, seq, 1, 104, 37, 0, 92,
#                     0, 1, 1, local_addr, real_audio_rcv_port, '192.168.10.205', 9999, 1)
#     sock.send(s)
#     seq = seq + 1
#     real_audio_rcv_port += 1
#
# def get_real_video(channel):
#     global seq
#     global real_video_rcv_port
#
#     # start udp server
#     us = tyrpu.network.udp_server.UDPServer(real_video_rcv_port)
#     us.init_server()
#     us.start_recv()
#
#     # send pg command
#     s = struct.pack('<bHbHHHHbbHiii32sii', 1, 2105, 12, 1, seq, 1, 68, 44, 0, 56,
#                     channel, 0, 1, bytes(local_addr.encode('utf-8')), real_video_rcv_port, 16)
#     sock.send(s)
#     seq = seq + 1
#     real_video_rcv_port += 1
#
#     while True:
#         time.sleep(1)
#
# def add_sub_device_ipc():
#     global seq
#     port = 20000
#     channel = 999
#     while (port <= 20000) :
#         s = struct.pack('<bHbHHHHbbHHbbii32s32sii128s128s32siiiiiiii', 1, 16001, 12, 1, seq, 1, 12+4+84+320, -48, 0, 4+84+320,
#                     channel, 1, 1, 1, port, "192.168.12.144", "SimIPC", 0, 320,
#                     "admin", "password_144", "192.168.12.144", 8002, 1, 1, 1, 17, 0, 0, 0);
#         print('add sub device ipc')
#         sock.send(s)
#         port += 1
#         channel += 1
#         seq = seq + 1
#         time.sleep(2)
#
# def add_sub_device_rpu():
#     global seq
#     s = struct.pack('<bHbHHHHbbHHbbii32s32sii128s128siii', 1, 16001, 12, 1, seq, 1, 12+4+84+268, -48, 0, 4+84+268,
#                     5, 0, 1, 1, 9802, "192.168.12.147", "SimRVU7", 0, 268,
#                     "admin", "rvu_password", 1, 0, 0);
#     print('add sub device rvu')
#     sock.send(s)
#     seq += 1
#
# def add_sub_device_sensor():
#     global seq
#     s = struct.pack('<bHbHHHHbbHHbbii32s32siiHHHH', 1, 16001, 12, 1, seq, 1, 12+4+84+8, -48, 0, 4+84+8,
#                     208, 2, 2, 1, 9802, "192.168.12.150", "SimSensor_0000000010", 0, 8,
#                     4, 48, 0, 0);
#     print('add sub device env')
#     sock.send(s)
#     seq += 1
#
# ''' def get_sub_device_sensor():
#     global seq
#     s = struct.pack('<bHbHHHHbbHHHHbbbbH32s', 1, 10003, 12, 1, seq, 1, 12+4+44, -48, 0, 4+44,
#                     0, 0, 51, 0, 0, 2, 2, 51, "");
#     print 'add sub device env'
#     sock.send(s)
#     seq += 1 '''
#
# def add_sub_device_env():
#     global seq
#     s = struct.pack('<bHbHHHHbbHHbbii32s32sii128s128sHHHHHHHH', 1, 16001, 12, 1, seq, 1, 12+4+84+272, -48, 0, 4+84+268,
#                     1, 2, 98, 1, 9802, "192.168.12.150", "SimENV", 0, 272,
#                     "admin", "env_password", 1, 11, 0, 0, 0, 0, 0, 0);
#     print('add sub device env')
#     sock.send(s)
#     seq += 1
#
# def del_sub_device_env():
#     global seq
#     s = struct.pack('<bHbHHHHbbHHbbii32s32sii128s128sHHHHHHHH', 1, 16003, 12, 1, seq, 1, 12+4+84+272, -48, 0, 4+84+268,
#                     1, 2, 98, 1, 8000, "192.168.12.188", "", 0, 272,
#                     "admin", "env_password", 1, 1, 0, 0, 0, 0, 0, 0);
#     print('add sub device env')
#     sock.send(s)
#     seq += 1
#
# def time_sync():
#     global seq
#
# def get_record_file():
#     global seq
#     s = struct.pack('<bHbHHHHbbHii32s32s', 1, 1141, 12, 0, seq, 1, 88, 63, 0, 76,
#                     28, 0, '2015-02-10 00:00:00', '2015-02-10 23:00:00')
#     print('get record file list')
#     sock.send(s)
#     seq += 1
#
# def set_configuration_preset():
#     global seq
#     s = struct.pack('<bHbHHHHbbHii16si', 1, 40842, 12, 0, seq, 1, 16+28, -7, 0, 4+28,
#                     2, 1, '1040020920100108', 1)
#     print('get record file list')
#     sock.send(s)
#     seq += 1
#
# def rpu_set_test_mode():
#     global seq
#     s = struct.pack('<bHbHHHHbbHi', 1, 40797, 12, 0, seq, 1, 20, -16, 0, 8, 2)
#     print('set rpu test mode')
#     sock.send(s)
#     seq += 1
#
# def set_alarm_deploy():
#     global seq
#     # to do
#     # s = struct.pack('<bHbHHHHbbHqiiiiqii')
#
# def rpu_restore_default():
#     global seq
#     s = struct.pack('<bHbHHHHbbHi', 1, 40791, 12, 1, seq, 1, 16, 1, 0, 8, 0)
#     print('send restore default command')
#     sock.send(s)
#     seq += 1
#
# def rpu_rollback():
#     global seq
#     s = struct.pack('<bHbHHHH', 1, 40787, 12, 0, seq, 1, 12)
#     print('send rpu rollback command')
#     sock.send(s)
#     seq += 1
#
# def ipc_start_test_mode():
#     global seq
#     s = struct.pack('<bHbHHHH', 1, 30000, 12, 0, seq, 1, 12)
#     print('ipc start tst mode')
#     sock.send(s)
#     seq += 1
#
# def ipc_send_alarm(alarmtype):
#     global seq
#     s = struct.pack('<bHbHHHHbbHi', 1, 30001, 12, 0, seq, 1, 20, 0, 0, 8, alarmtype)
#     print('ipd send alarm')
#     sock.send(s)
#     seq += 1
#
# def get_scada_serv_config():
#     global seq
#     s = struct.pack('<bHbHHHH', 1, 40832, 12, 0, seq, 1, 12)
#     print('get scada serverconfig')
#     sock.send(s)
#     seq += 1
#
# def get_db_clean_config():
#     global seq
#     s = struct.pack('<bHbHHHH', 1, 40822, 12, 0, seq, 1, 12)
#     print('get db clean config')
#     sock.send(s)
#     seq += 1
#
# def set_osd():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiiiii128siiiii128s', 1, 1051, 12, 0, seq, 1, 320, 0, 0, 320-12, 1, 2, 1, 5, 5, 0, 0, '@datetime',
#                     2, 500, 350, 0, 0, 'tieyue')
#     print('set osd')
#     sock.send(s)
#     seq += 1
#
# def ptz_control():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiHHHHHHHH', 1, 1097, 12, 0, seq, 1, 40, 17, 0, 28, 1, 14, 1, 0, 0, 0, 0, 0, 0, 0)
#     print('ptz control')
#     sock.send(s)
#     seq += 1
#
#     time.sleep(6)
#     s = struct.pack('<bHbHHHHbbHiiHHHHHHHH', 1, 1097, 12, 0, seq, 1, 40, 17, 0, 28, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#     sock.send(s)
#     seq += 1
#
# # 动环相关测试
# def getSensorConfig():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHiiii', 1, 1285, 12, 0, seq, 1, 16+16, 84, 0, 4+16, 0, 0, 60, 0)
#     print('获取环境量配置')
#     sock.send(s)
#     seq += 1
#
# def setSensorConfig():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHiiiidddddii', 1, 1283, 12, 0, seq, 1, 16+16, 84, 0, 4+16, 2, 1, 4, 48,
#                     100.0, 0.0, 0.0, 1.0, 1.0, 0, 0)
#     print('设置环境量配置')
#     sock.send(s)
#     seq += 1
#
# def getSensorAlarmConfig():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHiii32sii', 1, 1275, 12, 0, seq, 1, 16+52, 82, 0, 4+52,
#                     2, 0, 60, 'desc', 7, 0)
#     print('获取环境量告警配置')
#     sock.send(s)
#     seq += 1
#
# def setSensorAlarmConfig():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHiii32siidddd', 1, 1273, 12, 0, seq, 1, 16+52+32, 82, 0, 4+52+32,
#                     2, 0, 4, 'desc', 7, 32, 60.0, 1000.0, 0.3, 0.4 )
#     print('设置环境量告警配置')
#     sock.send(s)
#     seq += 1
#
# def getSensorAlarmDeploy():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHqiiii', 1, 1263, 12, 0, seq, 1, 16+24, 66, 0, 24,
#                     0x1030020010200004, 7, 0, 0, 0)
#     print('获取环境量布撤防')
#     sock.send(s)
#     seq += 1
#
# def addSensorAlarmDeploy():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHqiiiiqii', 1, 1261, 12, 0, seq, 1, 16+24+16, 66, 0, 24+16,
#                     0x1030020010200004, 7, 1, 1, 0, 0x1030020010100006, 0, 0)
#     print('设置环境量布撤防')
#     sock.send(s)
#     seq += 1
#
# def delSensorAlarmDeploy():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHqiiii', 1, 1261, 12, 0, seq, 1, 16+24, 66, 0, 4+24,
#                     0x1030020010101992, 4, 0, 0, 0)
#     print('删除环境量布撤防')
#     sock.send(s)
#     seq += 1
#
# def getAlarmRecordFileList():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHii32s32s', 1, 1141, 12, 0, seq, 1, 16+72, 72, 0, 4+72,
#                     115, 2, '2015-03-31 00:35:57', '2015-03-31 23:35:57')
#     print('获取录像列表')
#     sock.send(s)
#     seq += 1
#
# def getRecordFileList():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHii32s32s', 1, 1141, 12, 0, seq, 1, 16+72, 72, 0, 4+72,
#                     115, 0, '2015-05-07 00:00:00', '2015-05-07 23:35:57')
#     print('获取录像列表')
#     sock.send(s)
#     seq += 1
#
# def simNotCompleteData():
#     global seq
#
#     s = struct.pack('<bHbHHHHbbHii32s32s', 1, 1141, 12, 0, seq, 1, 16+99, 72, 0, 4+99,
#                     115, 2, '2015-03-31 00:35:57', '2015-03-31 23:35:57')
#     print('获取录像列表')
#     sock.send(s)
#     seq += 1
#
# def set_db_clean_config():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiii16si64s64s128si128s128s128s128s', 1, 40820, 12, 0, seq, 1, 820, -12, 0, 820-12,
#                     300, 3, 1, '', 0, '', '', '', 2, 'test9', 'tt9', 'test8', 'tt8')
#     print('set db clean config')
#     sock.send(s)
#     seq += 1
#
# def set_sensor_alarm_subscribe():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiii', 1, 1265, 12, 0, seq, 1, 16+16, 67, 0, 20,
#                     2, 4, 123, 1)
#     print('环境量告警订阅')
#     sock.send(s)
#     seq += 1
#
# def external_device_ctrl():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiiii', 1, 1293, 12, 0, seq, 1, 16+24, 85, 0, 28,
#                     1, 1, 5, 1, 4, 0)
#     print('外部设备控制')
#     sock.send(s)
#     seq += 1
#
# def simCameraReport():
#     addr = ('192.168.10.70', 9800)
#     sock.connect(addr)
#
#     sendLen = 12 + 4 + 128 + 8 + 4 + 4 + 32 + 64 + 64 + 4 + 4 + 32 + 4 + 4 + 4 + 128
#     s = struct.pack('<bHbHHHHbbH128sqii32s64s64sibbH32sHHibbH128s', 1, 3002, 12, 3, 1, 1, sendLen,
#                      101, 0, 4 + 128 + 8 + 4 + 4 + 32 + 64 + 64 + 4, "name__2", 0x1040020740107666,
#                      1, 1, "mode", "serial", "version", 0,
#                      102, 0, 32 + 4 + 4 + 4, '192.168.12.144', 8888, 0, 18,
#                      110, 0, 4 + 128, 'teamway123456')
#     print('模拟摄像机接入')
#     sock.send(s)
#
# def start_talk():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiii32si32sii', 1, 2203, 12, 1, seq, 1, 16+88, 37, 0, 4+88,
#                     117, 1, 1, '192.168.10.144', 9999, '192.168.10.120', 0, 1)
#     print('语音对讲')
#     sock.send(s)
#     seq += 1
#
#     while True:
#         time.sleep(1)
#
# def getDeviceAlarmLevel():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiii32s', 1, 41061, 12, 0, seq, 1, 16+20+32, -82, 0, 20+32+4,
#                     1, 7, 666, 0, 0, '')
#     print('获取设备告警级别')
#     sock.send(s)
#     seq += 1
#
# def setDeviceAlarmLevel():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiiibb30sibb30s', 1, 41059, 12, 0, seq, 1, 16+20+32, -82, 0, 20+32+4,
#                     1, 7, 666, 2, 1, 2, 4, '', 2, 8, 9, '')
#     print('设置设备告警级别')
#     sock.send(s)
#     seq += 1
#
# def setScada():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiii16si', 1, 40830, 12, 0, seq, 1, 16+32, -8, 0, 32+4,
#                     6666, 3, 1, '192.168.0.1', 5555)
#     print('获取设备告警级别')
#     sock.send(s)
#     seq += 1
#
# def getRecordFileFrame():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiHH', 1, 41065, 12, 0, seq, 1, 16+8, -78, 0, 12,
#                     1, 0, 0)
#     print('获取历史文件帧率')
#     sock.send(s)
#     seq += 1
#
# def setSMSSerial():
#     global seq
#     s = struct.pack('<bHbHHHHbbHbbibbbbbb24s', 1, 40816, 12, 0, seq, 1, 12+40, -14, 0, 40,
#                     1, 1, 115200, 0, 8, 1, 0, 1, 0, '862129145')
#     print('设置短信猫配置')
#     sock.send(s)
#     seq += 1
#
# def setConfiguration():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiii128s', 1, 40834, 12, 0, seq, 1, 14+128+12, -9, 0, 4+128+12,
#                     900, 7, 7, 'configuration_900')
#     print('设置组态点')
#     sock.send(s)
#     seq += 1
#
# def getSMSSerial():
#     global seq
#     s = struct.pack('<bHbHHHH', 1, 40818, 12, 0, seq, 1, 12)
#     print('设置短信猫配置')
#     sock.send(s)
#     seq += 1
#
# def getSysConfig():
#     global seq
#     s = struct.pack('<bHbHHHH', 1, 1067, 12, 0, seq, 1, 12)
#     print('获取系统配置')
#     sock.send(s)
#     seq += 1
#
# def testPtz():
#     addr = ('192.168.12.32', 7000)
#     sock.connect(addr)
#
#     s = struct.pack('<bbbbbbbbbbbbbbbb252s', 0x24, 0x6b, 0x69, 0x68, -48, -12, -51, 0x07, -24, -14, 0x0d, 0x12, 0x22, -6, -125, 0x77, '<?xml version="1.0" encoding="UTF-8" ?><Request><RPU-ID>1040020740000001</RPU-ID><PTZ-ID>847</PTZ-ID><Priority>1</Priority><User>Web</User><IP>192.168.12.52</IP><PTZControl><command>14</command><action>1</action><speed>4</speed></PTZControl></Request>')
#     print('模拟摄像机接入')
#     sock.send(s)
#
#     time.sleep(5)
#     s = struct.pack('<bbbbbbbbbbbbbbbb252s', 0x24, 0x6b, 0x69, 0x68, -48, -12, -51, 0x07, -24, -14, 0x0d, 0x12, 0x22, -6, -125, 0x77, '<?xml version="1.0" encoding="UTF-8" ?><Request><RPU-ID>1040020740000001</RPU-ID><PTZ-ID>847</PTZ-ID><Priority>1</Priority><User>Web</User><IP>192.168.12.52</IP><PTZControl><command>0</command><action>0</action><speed>0</speed></PTZControl></Request>')
#     print('模拟摄像机接入')
#     sock.send(s)
#
# # def test_door_control():
# #     global seq
# #     s = struct.pack('bHbHHHH', 1, 3008, 12, 0, seq, 1, 12)
#
# def start_simulate():
#     global sock
#
#     sock = socket(AF_INET, SOCK_STREAM)
#
#     # testPtz()
#     # get_record_schedule()
#     login_RPU()
#     time.sleep(1)
#
#     menjincontrol()
#     # getSysConfig()
#
#     # setScada()
#     # getRecordFileFrame()
#
#     # setSMSSerial()
#     # getSMSSerial()
#
#     # simCameraReport()
#     # setDeviceAlarmLevel()
#
#     # simNotCompleteData()
#     # set_sensor_alarm_subscribe()
#     # external_device_ctrl()
#
#     # setSensorConfig()
#     # getSensorConfig()
#     '''while True:
#         getSensorAlarmConfig()
#         time.sleep(1)
#         setSensorAlarmConfig()
#         time.sleep(1)
#         addSensorAlarmDeploy()
#         time.sleep(1)
#         delSensorAlarmDeploy()
#         time.sleep(1)
#         getSensorAlarmDeploy()
#         time.sleep(1)'''
#     # delSensorAlarmDeploy()
#
#     # getAlarmRecordFileList()
#     # getRecordFileList()
#
#     # rpu_set_test_mode()
#     # get_record_schedule()
#     # close_RPU()
#
#     # setConfiguration()
#
#     # get_real_video(992)
#     # start_talk()
#
#     # system_control()
#     # get_real_audio()
#     # setIPInfo()
#     # getIPInfo()
#     # setTime()
#     # setVideoEncode()
#     # setVideoMask()
#     # addUser()
#     # set_configuration_preset()
#     # add_sub_device_ipc()
#     # add_sub_device_rpu()
#     # add_sub_device_env()
#     # del_sub_device_env()
#     # add_sub_device_sensor()
#     # get_sub_device_sensor()
#     # get_record_file()
#     # rpu_restore_default()
#     # rpu_rollback()
#     # ipc_start_test_mode()
#     # get_scada_serv_config()
#     # set_db_clean_config()
#     # get_db_clean_config()
#     # ptz_control()
#     # set_osd()
#     # ipc_send_alarm(2)   # 1 移动侦测  2 视频遮盖
#     # system_reboot()
#
#
#     time.sleep(20)
#     close_RPU()
#     time.sleep(1)
#
# if __name__ == '__main__':
#     # while (1):
#     start_simulate()
