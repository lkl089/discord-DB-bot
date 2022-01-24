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

    if message.content == prefix + "명령어":
        embed = discord.Embed(title="명령어 목록", description="현재 사용할수있는 명령어입니다.", color=0x62c1cc)
        embed.add_field(name=":point_right:!마스크 '주소'", value="입력한 주소지의 공적마스크 판매처를 알려줍니다.", inline=False)
        embed.add_field(name=":point_right:!한국", value="한국의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name=":point_right:!정보출처", value="데이터를 가져오는 사이트를 알려줍니다.", inline=False)
        embed.add_field(name=":point_right:!홍보자료", value="방역수칙 이미지를 불러옵니다", inline=False)
        embed.add_field(name=":point_right:!세계", value="주요 확진국가의 코로나 확진자 정보를 알려줍니다.", inline=False)
        embed.add_field(name=":point_right:!'국가명'", value="각 확진국가들의 확진자 정보를 알려줍니다\n"+
                        "주요 확진국가들을 검색할수있습니다.(19개국)\n"+
                        "입력 예시) :point_right:!미국, !영국, !프랑스, !스페인 ....", inline=False)
        embed.add_field(name=":point_right:!아시아, !유럽, !북아메리카, !남아메리카, !아프리카, !오세아니아", value="각 대륙별 코로나 상황을 알려줍니다.", inline=False)
        await message.channel.send(embed=embed)
        # DM으로 메시지를 보냅니다.
        # await message.author.send("응답")


    if message.content == prefix + "목록":
        embed = discord.Embed(title="명령어 목록", description="명령어 목록입니다.", color=0x62c1cc)
        embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!세계", value="전세계 코로나 확진자 정보를  알려줍니다.", inline=False)
        embed.add_field(name="!마스크 '주소'", value="입력한 주소지의 공적마스크 판매처를 검색합니다", inline=False)
        embed.add_field(name="!국가목록", value="[추가예정]각 국가명 입력시 해당 국가의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!아시아, !유럽, !북아메리카, !남아메리카, !아프리카, !오세아니아", value="각 대륙별 코로나 상황을 알려줍니다.", inline=False)
        # embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.")
        #id = str(710687517275586580)
        #emoji = client.get_emoji(str(id))
        #emoji = 'U+003AU+0066U+006CU+0061U+0067U+005FU+006BU+0072U+003A'
        await message.channel.send(embed=embed)
        await message.add_reaction('a:flag_kr:b57d2718c0f2330c0e06166d4b5fb606')


        async def on_reaction_add(reaction, user):
            if reaction.emoji == ':flag_kr:':
                message.reaction(':flag_kr:')
                message.reaction(':globe_with_meridians:')


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
            cnt = str(row[0])
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
        embed.add_field(name="CNT",value=cnt,inline=False)
        embed.add_field(name="Device",value=device,inline=False)
        embed.add_field(name="Status",value=status,inline=False)
        embed.add_field(name="ip",value=ip,inline=False)
        embed.add_field(name="Time",value=time,inline=False)
        embed.add_field(name="Real",value=real,inline=False)

        await message.channel.send(embed=embed)


client.run(token1)
