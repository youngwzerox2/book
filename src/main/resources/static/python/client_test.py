# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import requests
import json
import sys
import re

# +
server1_url = "http://118.217.203.44:5100/analyze_emotion"  # 감정 예측
server2_url = "http://118.217.203.44:5200/book_recommend"   # 책 추천

id = sys.argv[1]
msg = sys.argv[2]
# id = 'test15'
# msg = '나 집에 갈래.'
# print("Java에서 온 msg: ({}) {}".format(id, msg))

# 현재 사용자의 id
# id = session.get('id')
# id = 'test2'

# server1에 감정 분석 요청
# sentences = []
# while():  # 추천 버튼 누르기 전까지
#     msg = input()
#     msg = re.sub(r"^\s+|\s+$", "", msg)
#     sentences.append(msg)

# msg = ' '.join(sentences)

# sentences = []  # 초기화

response_server1 = requests.post(server1_url, json={'sentence': msg})

if response_server1.status_code == 200:
    # server1의 응답에서 감정 정보를 가져옴
    emotion_info = response_server1.json()

    # server2에 감정 정보를 전달하여 도서 추천 요청
    response_server2 = requests.post(server2_url, json={
        'id': id,
        'emotion_tag': emotion_info['emotion_tag'],
        'emotion': emotion_info['emotion']
    })

    if response_server2.status_code == 200:
        # server2의 응답을 클라이언트에서 처리
        recommend_info = response_server2.json()
        # print('서버2에서 받은 응답:', recommend_info)
        # print('서버2에서 받은 응답:', recommend_info['emotion'])

        # # 서버2에서 받은 응답에서 추천 도서 정보 추출
        # if 'recommend1' in recommend_info:
        #     print('추천 도서 1: {}'.format(recommend_info["recommend1"]))
        # if 'recommend2' in recommend_info:
        #     print('추천 도서 2: {}'.format(recommend_info["recommend2"]))
        # if 'recommend3' in recommend_info:
        #     print('추천 도서 3: {}'.format(recommend_info["recommend3"]))


        # 실제 데이터 출력
        print(recommend_info['emotion'])
        if 'recommend1' in recommend_info:
            print(recommend_info["recommend1"])
        if 'recommend2' in recommend_info:
            print(recommend_info["recommend2"])
        if 'recommend3' in recommend_info:
            print(recommend_info["recommend3"])
        

    else:
        print('서버2 응답 실패:', response_server2.text)
else:
    print('서버1 응답 실패:', response_server1.text)

