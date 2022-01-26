# -*- coding:utf-8 -*-
import os
import sys
import discord, asyncio
from data import token

import platform
import pymssql
import datetime
import dbaccount as dba
import socket as soc

client_id = token.client_id
client_secret = token.client_secret

client = discord.Client()
token1 = token.token

prefix = "!"  # 접두어

ch = 0
for message in client.guilds:
    ch += len(message.channels)

# DB Access Start

# DB 서버 주소
server = dba.server
# 데이터 베이스 이름
database = dba.database
# 접속 유저명
username = dba.username
# 접속 유저 패스워드
password = dba.password

# MSSQL 접속
cnxn = pymssql.connect(server, username, password, database)
cursor = cnxn.cursor()

#cursor.execute('SELECT * FROM Test_table;')
cursor.execute('SELECT * FROM Test_table ORDER BY CAST(CNT AS int) ASC;')

row = cursor.fetchone()

while row:
    # 0=CNT, 1=DeviceType, 2=PC_Status, 3=IP, 4=PC_Time, 5=isReal
    print(row[0], row[1], row[2], row[3], row[4],row[5])
    cnt = str(row[0])
    device = str(row[1])
    status = str(row[2])
    ip = str(row[3])
    time = str(row[4])
    real = str(row[5])
    row = cursor.fetchone()

cnxn.close()

# DB Access END!

@client.event
async def on_ready():
    print("봇 시작")
    #
    await bt(['DB TEST'])
    # print(client.user.name) # 봇의 이름을 출력합니다.
    # print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.


async def bt(zz):
    #    await client.wait_until_ready()

    while not client.is_closed():
        for message in zz:
            await client.change_presence(status=discord.Status.online, activity=discord.Game(message))
            await asyncio.sleep(10)  # 5초마다 메세지 변경
            print(message)


@client.event
async def on_message(message, maskinfo=[],
                     mark=[],stop=[],stop_c=[],stop_sell=''):  # 메시지가 들어 올 때마다 가동되는 구문입니다.
    if message.author.bot:  # 채팅을 친 사람이 봇일 경우
        return None  # 반응하지 않고 구문을 종료합니다.

    if message.content == prefix + "테스트":
        # DB Access Start

        # DB 서버 주소
        server = dba.server
        # 데이터 베이스 이름
        database = dba.database
        # 접속 유저명
        username = dba.username
        # 접속 유저 패스워드
        password = dba.password

        # MSSQL 접속
        cnxn = pymssql.connect(server, username, password, database)
        cursor = cnxn.cursor()

        # cursor.execute('SELECT * FROM Test_table;')
        cursor.execute('SELECT * FROM Test_table ORDER BY CAST(CNT AS int) ASC;')

        row = cursor.fetchone()

        while row:
            # 0=CNT, 1=DeviceType, 2=PC_Status, 3=IP, 4=PC_Time, 5=isReal
            print(row[0], row[1], row[2], row[3], row[4], row[5])
            allow_id = str(row[0])
            device = str(row[1])
            status = str(row[2])
            ip = str(row[3])
            time = str(row[4])
            real = str(row[5])
            row = cursor.fetchone()

        print('Read DB!!')
        cnxn.close()

        # DB Access END!

        embed = discord.Embed(title="DB 데이터 테스트", color=0xa83232)
        embed.add_field(name="CNT", value=allow_id, inline=True)
        embed.add_field(name="Device",value=device,inline=True)
        embed.add_field(name="Status",value=status,inline=False)
        embed.add_field(name="ip",value=ip,inline=False)
        embed.add_field(name="Time",value=time,inline=False)
        embed.add_field(name="Real",value=real,inline=False)

        await message.channel.send(embed=embed)

    if message.content == prefix + "명령어":
        # DB Access Start

        # DB 서버 주소
        server = dba.server
        # 데이터 베이스 이름
        database = dba.database
        # 접속 유저명
        username = dba.username
        # 접속 유저 패스워드
        password = dba.password

        # MSSQL 접속
        cnxn = pymssql.connect(server, username, password, database)
        cursor = cnxn.cursor()

        # cursor.execute('SELECT * FROM Test_table;')
        cursor.execute('SELECT * FROM Test_table ORDER BY CAST(CNT AS int) ASC;')

        row = cursor.fetchone()

        while row:
            # 0=CNT, 1=DeviceType, 2=PC_Status, 3=IP, 4=PC_Time, 5=isReal
            print(row[0], row[1], row[2], row[3], row[4], row[5])
            allow_id = str(row[0])
            device = str(row[1])
            status = str(row[2])
            ip = str(row[3])
            time = str(row[4])
            real = str(row[5])
            row = cursor.fetchone()

        print('Read DB!!')
        cnxn.close()

        # DB Access END!

        embed = discord.Embed(title="VRCHAT 명령어", color=0xa83232)
        embed.add_field(name="!아바타",value='아바타 목록을 표시합니다.',inline=False)
        embed.add_field(name="!옷",value='아바타별 옷 목록을 표시합니다.',inline=False)
        embed.add_field(name="!악세사리",value='악세사리 목록을 표시합니다.',inline=False)
        embed.add_field(name="!SDK",value='VRCSDK 버전을 표시합니다.',inline=False)

        await message.channel.send(embed=embed)

    if message.content == prefix + "아바타":
        # DB Access Start

        # DB 서버 주소
        server = dba.server
        # 데이터 베이스 이름
        database = dba.database
        # 접속 유저명
        username = dba.username
        # 접속 유저 패스워드
        password = dba.password

        # MSSQL 접속
        cnxn = pymssql.connect(server, username, password, database)
        cursor = cnxn.cursor()

        # cursor.execute('SELECT * FROM Test_table;')
        cursor.execute('SELECT VRCHAT FROM avatar;')

        row = cursor.fetchone()

        while row:
            # 0=Number, 1=Avatar_Name, 2=Avatar_Version, 3=Avatar_SDK, 4=Avatar_Image, 5=Avatar_URL
            print(row[0], row[1], row[2], row[3], row[4], row[5])
            number = str(row[0])
            A_name = str(row[1])
            A_version = str(row[2])
            A_SDK = str(row[3])
            A_img = str(row[4])
            A_url = str(row[5])
            row = cursor.fetchone()

        print('Read DB!!')
        cnxn.close()

        # DB Access END!

        embed = discord.Embed(title="VRCHAT 명령어", color=0xa83232)
        embed.add_field(name="!아바타",value='아바타 목록을 표시합니다.',inline=False)
        embed.add_field(name="!옷",value='아바타별 옷 목록을 표시합니다.',inline=False)
        embed.add_field(name="!악세사리",value='악세사리 목록을 표시합니다.',inline=False)
        embed.add_field(name="!SDK",value='VRCSDK 버전을 표시합니다.',inline=False)

        await message.channel.send(embed=embed)

    if message.content == prefix + "옷":
        # DB Access Start

        # DB 서버 주소
        server = dba.server
        # 데이터 베이스 이름
        database = dba.database
        # 접속 유저명
        username = dba.username
        # 접속 유저 패스워드
        password = dba.password

        # MSSQL 접속
        cnxn = pymssql.connect(server, username, password, database)
        cursor = cnxn.cursor()

        # cursor.execute('SELECT * FROM Test_table;')
        cursor.execute('SELECT * FROM Test_table ORDER BY CAST(CNT AS int) ASC;')

        row = cursor.fetchone()

        while row:
            # 0=CNT, 1=DeviceType, 2=PC_Status, 3=IP, 4=PC_Time, 5=isReal
            print(row[0], row[1], row[2], row[3], row[4], row[5])
            allow_id = str(row[0])
            device = str(row[1])
            status = str(row[2])
            ip = str(row[3])
            time = str(row[4])
            real = str(row[5])
            row = cursor.fetchone()

        print('Read DB!!')
        cnxn.close()

        # DB Access END!

        embed = discord.Embed(title="VRCHAT 명령어", color=0xa83232)
        embed.add_field(name="!아바타",value='아바타 목록을 표시합니다.',inline=False)
        embed.add_field(name="!옷",value='아바타별 옷 목록을 표시합니다.',inline=False)
        embed.add_field(name="!악세사리",value='악세사리 목록을 표시합니다.',inline=False)
        embed.add_field(name="!SDK",value='VRCSDK 버전을 표시합니다.',inline=False)

        await message.channel.send(embed=embed)


    if message.content == prefix + "악세사리":
        # DB Access Start

        # DB 서버 주소
        server = dba.server
        # 데이터 베이스 이름
        database = dba.database
        # 접속 유저명
        username = dba.username
        # 접속 유저 패스워드
        password = dba.password

        # MSSQL 접속
        cnxn = pymssql.connect(server, username, password, database)
        cursor = cnxn.cursor()

        # cursor.execute('SELECT * FROM Test_table;')
        cursor.execute('SELECT * FROM Test_table ORDER BY CAST(CNT AS int) ASC;')

        row = cursor.fetchone()

        while row:
            # 0=CNT, 1=DeviceType, 2=PC_Status, 3=IP, 4=PC_Time, 5=isReal
            print(row[0], row[1], row[2], row[3], row[4], row[5])
            allow_id = str(row[0])
            device = str(row[1])
            status = str(row[2])
            ip = str(row[3])
            time = str(row[4])
            real = str(row[5])
            row = cursor.fetchone()

        print('Read DB!!')
        cnxn.close()

        # DB Access END!

        embed = discord.Embed(title="VRCHAT 명령어", color=0xa83232)
        embed.add_field(name="!아바타",value='아바타 목록을 표시합니다.',inline=False)
        embed.add_field(name="!옷",value='아바타별 옷 목록을 표시합니다.',inline=False)
        embed.add_field(name="!악세사리",value='악세사리 목록을 표시합니다.',inline=False)
        embed.add_field(name="!SDK",value='VRCSDK 버전을 표시합니다.',inline=False)

        await message.channel.send(embed=embed)

    if message.content == prefix + "SDK":
        # DB Access Start

        # DB 서버 주소
        server = dba.server
        # 데이터 베이스 이름
        database = dba.database
        # 접속 유저명
        username = dba.username
        # 접속 유저 패스워드
        password = dba.password

        # MSSQL 접속
        cnxn = pymssql.connect(server, username, password, database)
        cursor = cnxn.cursor()

        # cursor.execute('SELECT * FROM Test_table;')
        cursor.execute('SELECT * FROM Test_table ORDER BY CAST(CNT AS int) ASC;')

        row = cursor.fetchone()

        while row:
            # 0=CNT, 1=DeviceType, 2=PC_Status, 3=IP, 4=PC_Time, 5=isReal
            print(row[0], row[1], row[2], row[3], row[4], row[5])
            allow_id = str(row[0])
            device = str(row[1])
            status = str(row[2])
            ip = str(row[3])
            time = str(row[4])
            real = str(row[5])
            row = cursor.fetchone()

        print('Read DB!!')
        cnxn.close()

        # DB Access END!

        embed = discord.Embed(title="VRCHAT 명령어", color=0xa83232)
        embed.add_field(name="!아바타",value='아바타 목록을 표시합니다.',inline=False)
        embed.add_field(name="!옷",value='아바타별 옷 목록을 표시합니다.',inline=False)
        embed.add_field(name="!악세사리",value='악세사리 목록을 표시합니다.',inline=False)
        embed.add_field(name="!SDK",value='VRCSDK 버전을 표시합니다.',inline=False)

        await message.channel.send(embed=embed)

    if message.content == prefix + "다운로드":
        # DB Access Start

        # DB 서버 주소
        server = dba.server
        # 데이터 베이스 이름
        database = dba.database
        # 접속 유저명
        username = dba.username
        # 접속 유저 패스워드
        password = dba.password

        # MSSQL 접속
        cnxn = pymssql.connect(server, username, password, database)
        cursor = cnxn.cursor()

        # cursor.execute('SELECT * FROM Test_table;')
        cursor.execute('SELECT * FROM VRCHAT.dbo.avatar;')

        row = cursor.fetchone()

        while row:
            # 0=Number, 1=Avatar_Name, 2=Avatar_Version, 3=Avatar_SDK, 4=Avatar_Image, 5=Avatar_URL
            print(row[0], row[1], row[2], row[3], row[4], row[5])
            number = str(row[0])
            A_name = str(row[1])
            print(A_name)
            A_version = str(row[2])
            A_SDK = str(row[3])
            A_img = str(row[4])
            A_url = str(row[5])
            row = cursor.fetchone()

        print('Read DB!!')

        cursor.execute('SELECT Access_ID FROM [VRCHAT].[dbo].[access];')

        row2 = cursor.fetchone()
        print('---')
        print(A_name[0])
        print(A_name[1])

        allow_id = []
        while row2:
            # 0=Number, 1=Avatar_Name, 2=Avatar_Version, 3=Avatar_SDK, 4=Avatar_Image, 5=Avatar_URL
            print(row2[0])
            allow_id.append(str(row2[0]))
            row2 = cursor.fetchone()

        print(allow_id)
        print('Read DB!!')
        cnxn.close()

        # DB Access END!

        your_id = str(message.author)
        print(your_id)
        print(allow_id)
        print("비교시작")
        compare_id = your_id in allow_id
        print(compare_id)
        print("비교완료")
        
        #if str(your_id) == str(compare_id):
        if compare_id==True:
            embed = discord.Embed(title="다운로드 링크", color=0xa83232)
            embed.set_image(url=A_img)
            embed.add_field(name="아바타 이름", value=A_name, inline=True)
            embed.add_field(name="아바타 버전", value=A_version, inline=False)
            embed.add_field(name="아바타 SDK", value=A_SDK, inline=False)
            embed.add_field(name="다운로드 링크", value=A_url, inline=False)

            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title=":x:권한 없음!:x:",description="권한이 없는 디스코드 계정입니다.", color=0xCD1039)
            embed.add_field(name="권한이 부여된 계정", value=allow_id, inline=False)

            await message.channel.send(embed=embed)

client.run(token1)
