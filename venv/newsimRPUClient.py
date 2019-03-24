# #-*-coding:utf-8-*-
# # @time      :2019/1/2014:46
# # @Author   :lemon_hehe
# # @Email     :976621712@qq.com
# # @File      :test_login.py
# # @software:PyCharm Community Edition
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
# def door_control():
#     global seq
#     s = struct.pack('<bHbHHHHbbHI', 1, 3008, 12, 1, seq, 1, 20, 120, 0, 8, 1)
#     print('门禁控制器')
#     sock.send(s)
#     seq = seq + 1
#
# def videodliagnose():
#     global seq
#     s = struct.pack('<bHbHHHHbbHiiiiii', 1, 1303, 12, 1, seq, 1, 40, 133, 0, 28, '192.168.12.143',
#                     '2019-3-23', 1, 1, 98, 2)
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
#     s = struct.pack('<bHbHHHHbbHii', 1, 1312, 12, 1, seq, 1, 24, 132, 0, 12, 1, 0)
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
#     s = struct.pack('bHbHHHHbbHiii', 1, 1354, 12, 1, seq, 1, 28, 151, 0, 16, 1, '192.168.12.143', 1)
#     print('控制视频浓缩任务')
#     sock.send(s)
#     seq = seq + 1
#
# def information_change():
#     global seq
#     s = struct.pack('bHbHHHHbbHqiiiiqiiqi', 1, 1361, 12, 0, seq, 1, 68, 66, 0, 56, 1, 1,
#                    1, 2, 2, 1, 1, 0, 1, 0)
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
#     s = struct.pack('bHbHHHHbbHqiii', 1, 1370, 12, 1, seq, 1, 36, 158, 0, 24, 11, 169, 180, '')
#     print('获取热成像通道实时视频画面任意点的温度')
#     sock.send(s)
#     seq = seq + 1
#
# def get_infrared_():
#     global seq
#     s = struct.pack('bHbHHHHbbHqic', 1, 1372, 12, 1, seq, 1, 29, 159, 0, 17, 11, 33, '')
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
#     s = struct.pack('bHbHHHHbbHii', 1, 1376, 12, 1, seq, 1, 24, 156, 12, 1, 1)
#     print('控制巡检计划的请求报文')
#     sock.send(s)
#     seq = seq + 1
#
# def send_patrol_result():
#     global seq
#     s = struct.pack('bHbHHHHbbHciciiiiicii', 1, 1378, 12, 1, seq, 1, 59, 157, 0, 47, '2019-3-21', 1, 'test',
#                     2, 1, 1, 1, 2, 1, '可见光', '192.168.12.143', 1)
#     print('向主站发送巡检结果')
#     sock.send(s)
#     seq =seq + 1
#
# def start_simulate():
#     global sock
#     sock = socket(AF_INET, SOCK_STREAM)
#
#     login_RPU()
#     time.sleep(1)
#     door_control()
#
#     time.sleep(20)
#     close_RPU()
#     time.sleep(1)
#
#
# if __name__ == '__main__':
#     start_simulate()