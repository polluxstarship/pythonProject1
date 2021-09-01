from card import *
import copy
import datetime


time = datetime.datetime.now().replace(microsecond=0)
card = card() # 셔플한 카드 생성
bet = betting() # 배팅 킆래스 생성
members1 = members() # 멤버객체 생성

sql1 = "select id, money from poka.id_info where id = \'odin\'or id = \'sakara\'"
card.carddb.exe(sql1)
result = card.carddb.show()
numk = 1
for re in result:
    globals()['player'+str(numk)] = player(card, members1, re['id'], re['money'], time)  # 플레이어 객체 생성(카드객체, 멤버객체, 이름, 시작 자금, 시간)
    numk = numk + 1

members1.winner(player1) # 순위산정을 위해 플레이어 객체를 멤버 위너리 리스트에 넣는다
members1.winner(player2)

bet.regist(player1) # 베팅을 위해 베팅객체에 플레이어를 등록한다
bet.regist(player2)

bet.start(100) # 베팅 참가비 100을 걷는다

members1.given(player1.hcard) # 멤버 클래스에 플레이어 추가
members1.given(player2.hcard)

card1 = [['card1','card1n'],['card2','card2n'],['card3','card3n'],['card4','card4n']]
for i,j in card1:
    give(card, player1, i, j, members1.names[0], time)   # give는 플레이어에 카드를 주는 함수다
for i,j in card1:
    give(card, player2, i, j, members1.names[1], time)

print('player1:{}'.format(player1.hcard))
ar = player1.deletes() # 버릴카드 선택하기
print('player2:{}'.format(player2.hcard))
ar2 = player2.deletes()
sql = 'update poka.card set del = \'{}\' where name = \'{}\' and time = \'{}\''.format(ar[0][0], members1.names[0], time) #결과 db에 넣기
sql1 = 'update poka.card set del = \'{}\' where name = \'{}\' and time = \'{}\''.format(ar2[0][0], members1.names[1], time)
card.carddb.exe(sql)
card.carddb.exe(sql1)
sql = 'update poka.card set del1 = \'{}\' where name = \'{}\' and time = \'{}\''.format(ar[1][0], members1.names[0], time) #결과 db에 넣기
sql1 = 'update poka.card set del1 = \'{}\' where name = \'{}\' and time = \'{}\''.format(ar2[1][0], members1.names[1], time)
card.carddb.exe(sql)
card.carddb.exe(sql1)
card.carddb.commit()

card2 = [['card5','card5n'],['card6','card6n'],['card7','card7n'],['card8','card8n']]
for i,j in card2:
    give(card, player1, i, j, members1.names[0], time)   # give는 플레이어에 카드를 주는 함수다
for i,j in card2:
    give(card, player1, i, j, members1.names[1], time)

ppr(card, bet, player1, player2, time, 'card5', 'card5n')
ppr(card, bet, player1, player2, time, 'card6', 'card6n')
ppr(card, bet, player1, player2, time, 'card7', 'card7n')
ppr(card, bet, player1, player2, time, 'card8', 'card8n')

cal1 = calculation(player1)  # 주어진 패의 랭크를 계산하는 클래스이다
cal2 = calculation(player2)

ranks = [] # 랭크라는 리스트에 각 플레이어들의 카드 랭크를 추가한다
ranks.append(cal1.rank())
ranks.append(cal2.rank())
print(ranks)

sql = 'update poka.card set result = \'{}\' where name = \'{}\' and time = \'{}\''.format(ranks[0][0], members1.names[0], time) #결과 db에 넣기
sql1 = 'update poka.card set result = \'{}\' where name = \'{}\' and time = \'{}\''.format(ranks[1][0], members1.names[1], time)
card.carddb.exe(sql)
card.carddb.exe(sql1)
sql = 'update poka.card set result1 = \'{}\' where name = \'{}\' and time = \'{}\''.format(ranks[0][1], members1.names[0], time) #결과 db에 넣기
sql1 = 'update poka.card set result1 = \'{}\' where name = \'{}\' and time = \'{}\''.format(ranks[1][1], members1.names[1], time)
card.carddb.exe(sql)
card.carddb.exe(sql1)
card.carddb.commit()

ranklist = copy.deepcopy(ranks) # copy를 import 해와서 랭크 리스트를 딬카피 하고
wincard = pick(ranks)   # pick 함수는 ranks 리스트에서 가장 위너의 랭크를 반환한다.
winindex = ranklist.index(wincard)   # 딥카피한 리스트에서 pick 함수의 반환값의 인덱스를 구한다.
winner = members1.winary[winindex]
winner_name = members1.names[winindex]
sql1 = 'update poka.card set winner = \'winner\' where name = \'{}\' and time = \'{}\''.format(winner_name, time)
card.carddb.exe(sql1)
card.carddb.commit()
print('승자는 '+winner_name+'입니다.')  # 멤버에 등록된 플레이어 인덱스를 찾아서 반환한다.
bet.finish(winner) # 위너에게 베팅 토탈값을 준다
print(player1.money)
print(player2.money)



