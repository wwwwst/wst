import json
import time

import requests


class Card:
    def __init__(self, f, n):
        self.flower = f
        self.num = n
poker_1 = [Card(0, 0) for i in range(14)]
poker_2 = [Card(0, 0) for j in range(14)]
poker_3 = [Card(0, 0) for k in range(14)]
ans_1 = [Card(0, 0) for l in range(20)]
ans_2 = [Card(0, 0) for m in range(20)]
ans_3 = [Card(0, 0) for n in range(20)]
temp_1 = [Card(0, 0) for o in range(20)]
temp_2 = [Card(0, 0) for p in range(20)]
temp_3 = [Card(0, 0) for q in range(20)]
end_1 = [Card(0, 0) for r in range(20)]
end_2 = [Card(0, 0) for s in range(20)]
end_3 = [Card(0, 0) for t in range(20)]
s1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
r1 = 5
r2 = 5
r3 = 3
end_ans = 0

hua = [0, 0, 0, 0, 0, 0]
number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
score = 0.0
cnt = 0
global e1, e2, e3
global a1, a2, a3

def init_cnt():
    for i in range(0, 6):
        hua[i] = 0
    for i in range(0, 20):
        number[i] = 0


def bubble_sort(nums, a, b):
    for i in range(b - a):
        for j in range(b - a - 1):
            if nums[a + j].num > nums[a + j + 1].num:
                nums[a + j], nums[a + j + 1] = nums[a + j + 1], nums[a + j]
    return nums


def shunof3(start):
    for i in range(start, start + 3):
        if number[i] < 1:
            return 0
    else:
        return 1


def shunof5(start):
    for i in range(start, start + 5):
        if number[i] < 1:
            return 0
    else:
        return 1


def tou():
    global score
    init_cnt()
    bubble_sort(ans_3, 1, 3)
    for i in range(1, 4):
        hua[ans_3[i].flower] = hua[ans_3[i].flower] + 1
        number[ans_3[i].num] = number[ans_3[i].num] + 1
    x = 1
    for i in range(1, 5):
        if hua[i] == 3:
            if shunof3(ans_3[1].num) == 1:
                k = (9.0 + 0.9 / 11.0 * (ans_3[1].num - 1))
                score += k
                return k  # 3张同花顺
    x = 1
    for i in range(1, 5):
        if hua[i] == 3:
            k = (6.0 + 0.9 / (1300 + 130 + 13)
                 * ((ans_3[3].num - 1) * 100 + (ans_3[2].num - 1) * 10 + (ans_3[1].num - 1)) * 1.0)
            score += k
            return k  # 3张同花
    x = 1
    if shunof3(ans_3[1].num) == 1:
        k = (5.0 + 0.9 / 11.0 * (ans_3[1].num - 1) * 1.0)
        score += k
        return k  # 3张顺子
    x = 1
    for i in range(3, 0, -1):
        if number[ans_3[i].num] == 3:
            k = (4.0 + 0.9 / 13.0 * (ans_3[1].num - 1) * 1.0)
            score += k
            return k  # 三条
    x = 1
    for i in range(3, 0, -1):
        if number[ans_3[i].num] == 1:
            x = ans_3[i].num
        if number[ans_3[i].num] == 2:
            k = (1.0 + 0.9 / (130 + 13) * ((ans_3[i].num - 1) * 10 + x - 1) * 1.0)
            score += k
            return k  # 单对
    x = 1
    k = 0.9 / (1300.0 + 130.0 + 13.0) * (
                (ans_3[3].num - 1) * 100 + (ans_3[2].num - 1) * 10 + (ans_3[1].num - 1))
    score += k
    return k  # 散牌


def zhong():
    global score
    init_cnt()
    bubble_sort(ans_2, 1, 5)
    x = 1
    for i in range(1, 6):
        hua[ans_2[i].flower] = hua[ans_2[i].flower] + 1
        number[ans_2[i].num] = number[ans_2[i].num] + 1
    x = 1
    for i in range(1, 6):
        if hua[i] == 5:
            if shunof5(ans_2[1].num) == 1:
                k = (9.0 + 0.9 / 9 * (ans_2[1].num - 1)) * 1.0
                score += k  # 14 13 12 11 10
                return k  # 同花顺
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 4:
            k = (8.0 + 0.9 / (130 + 13) * ((ans_2[i].num - 1) * 10)) * 1.0
            score += k
            return k  # 炸弹
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5, 0, -1):
                if number[ans_2[j].num] == 2:
                    k = (7.0 + 0.9 / (130 + 13) * ((x - 1) * 10 + ans_2[j].num - 1)) * 1.0
                    score += k
                    return k  # 葫芦
    x = 1
    for i in range(1, 6):
        if hua[i] == 5:
            k = (6.0 + 0.9 / (130000 + 13000 + 1300 + 130 + 13) * (
                        (ans_2[5].num - 1) * 10000 + (ans_2[4].num - 1) * 1000 + (ans_2[3].num - 1) * 100 + (
                            ans_2[2].num - 1) * 10 + (ans_2[1].num - 1))) * 1.0
            score += k
            return k  # 同花
    x = 1
    if shunof5(ans_2[1].num) == 1:
        k = (5.0 + 0.9 / 9 * (ans_2[1].num - 1) * 1.0)
        score += k
        return k  # 5张顺子
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5, 0, -1):
                if number[ans_2[j].num] == 1:
                    k = (4.0 + 0.9 / (1300 + 130 + 13) * ((x - 1) * 100))
                    score += k
                    return k  # 三条
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 2:
            for j in range(5, 0, -1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 and abs(
                        ans_2[i].num - ans_2[j].num) == 1:
                    k = (3.0 + 0.9 / 10 * (ans_2[j].num - 1 - 1)) * 1.0
                    score += k
                    return k  # 连对2对
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 2:
            for j in range(5, 0, -1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2:
                    k = (2.0 + 0.9 / (130 + 13) * ((ans_2[i].num - 1) * 10 + ans_2[j].num - 1)) * 1.0
                    score += k
                    return k  # 普通2对
    x = 1
    for i in range(5, 0, -1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 2:
            k = (1.0 + 0.9 / (130 + 13) * ((ans_2[i].num - 1) * 10 + x - 1)) * 1.0
            score += k
            return k  # 单对+3张散

    k = (0.9 / (130000 + 13000 + 1300 + 130 + 13) * (
                (ans_2[5].num - 1) * 10000 + (ans_2[4].num - 1) * 1000 + (ans_2[3].num - 1) * 100 + (
                    ans_2[2].num - 1) * 10 + ans_2[1].num - 1)) * 1.0
    score += k
    return k

def wei():
    global score
    init_cnt()
    bubble_sort(ans_1, 1, 5)
    x = 1
    for i in range(1, 6):
        hua[ans_1[i].flower] = hua[ans_1[i].flower] + 1
        number[ans_1[i].num] = number[ans_1[i].num] + 1
    x = 1
    for i in range(1, 6):
        if hua[i] == 5:
            if shunof5(ans_1[1].num) == 1:
                k = (9.0 + 0.9 / 9 * (ans_1[1].num - 1)) * 1.0  # 14 13 12 11 10
                score += k
                return k  # 同花顺
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 4:
            x = ans_1[i].num
        if number[ans_1[i].num] == 4:
            k = (8.0 + 0.9 / (130 + 13) * ((ans_1[i].num - 1) * 10)) * 1.0
            score += k
            return k  # 炸弹
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5, 0, -1):
                if number[ans_1[j].num] == 2:
                    k = (7.0 + 0.9 / (130 + 13) * ((x - 1) * 10 + ans_1[j].num - 1)) * 1.0
                    score += k
                    return k  # 葫芦
    x = 1
    for i in range(1, 6):
        if hua[i] == 5:
            k = (6.0 + 0.9 / (130000 + 13000 + 1300 + 130 + 13) * (
                        (ans_1[5].num - 1) * 10000 + (ans_1[4].num - 1) * 1000 + (ans_1[3].num - 1) * 100 + (
                            ans_1[2].num - 1) * 10 + (ans_1[1].num - 1))) * 1.0
            score += k
            return k  # 同花
    x = 1
    if shunof5(ans_1[1].num) == 1:
        k = (5.0 + 0.9 / 9 * (ans_1[1].num - 1) * 1.0)
        score += k
        return k  # 5张顺子
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5, 0, -1):
                if number[ans_1[j].num] == 1:
                    k = (4.0 + 0.9 / (1300 + 130 + 13) * ((x - 1) * 100))
                    score += k
                    return k  # 三条
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 2:
            for j in range(5, 0, -1):
                if (ans_1[i].num != ans_1[j].num) and \
                        number[ans_1[j].num] == 2 and abs(ans_1[i].num - ans_1[j].num) == 1:
                    k = (3.0 + 0.9 / 10 * (ans_1[j].num - 1 - 1)) * 1.0
                    score += k
                    return k  # 连对2对
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 2:
            for j in range(5, 0, -1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2:
                    k = (2.0 + 0.9 / (130 + 13) * ((ans_1[i].num - 1) * 10 + ans_1[j].num - 1)) * 1.0
                    score += k
                    return k  # 普通2对
    x = 1
    for i in range(5, 0, -1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 2:
            k = (1.0 + 0.9 / (130 + 13) * ((ans_1[i].num - 1) * 10 + x - 1)) * 1.0
            score += k
            return k  # 单对+3张散

    k = (0.9 / (130000 + 13000 + 1300 + 130 + 13) * (
                (ans_1[5].num - 1) * 10000 + (ans_1[4].num - 1) * 1000 + (ans_1[3].num - 1) * 100 + (
                    ans_1[2].num - 1) * 10 + ans_1[1].num - 1)) * 1.0
    score += k
    return k

def StandOf():
    for i in range(1, 4):
        end_3[i] = ans_3[i]
    for i in range(1, 6):
        end_2[i] = ans_2[i]
    for i in range(1, 6):
        end_1[i] = ans_1[i]


def TempoF():
    for i in range(1, 4):
        ans_3[i] = temp_3[i]
    for i in range(1, 6):
        ans_2[i] = temp_2[i]
    for i in range(1, 6):
        ans_1[i] = temp_1[i]


def Print():
    for i in range(1, 4):
        if i == 3:
            print(ans_3[i].num)
        else:
            print(ans_3[i].num, end=" ")
    for i in range(1, 6):
        if i == 5:
            print(ans_2[i].num)
        else:
            print(ans_2[i].num, end=" ")
    for i in range(1, 6):
        if i == 5:
            print(ans_1[i].num)
        else:
            print(ans_1[i].num, end=" ")


def contrast_ans():
    global score, end_ans, cnt
    global e1, e2, e3
    global a1, a2, a3
    TempoF()
    k1 = tou()
    e1 = score
    k2 = zhong()
    e2 = score - e1
    k3 = wei()
    e3 = score - (e1+e2)
    score = k1 + k2 + k3
    if k1 > k2 or k2 > k3 or k1 > k3:
        score = 0
    if score > end_ans:
        end_ans = score
        a1 = e1;
        a2 = e2;
        a3 = e3;
        StandOf()
    cnt += 1

def init_2():
    index = 0
    for i in range(1, 9):
        if s2[i] == 0:
            index = index + 1
            temp_3[index] = poker_2[i]

def dfs_2(d, index_2):
    for i in range(d, 9):
        temp_2[index_2] = poker_2[i]
        s2[i] = 1
        if index_2 == r2:
            init_2()
            contrast_ans()
        else:
            dfs_2(i + 1, index_2 + 1)
        s2[i] = 0

def init_1():
    index = 0
    for i in range(1, 14):
        if s1[i] == 0:
            index = index+1
            poker_2[index] = poker_1[i]


def dfs_1(d, index_1):
    for i in range(d, 14):
        s1[i] = 1
        temp_1[index_1] = poker_1[i]
        if index_1 == r1:
            init_1()
            dfs_2(1, 1)
        else:
            dfs_1(i + 1, index_1 + 1)
        s1[i] = 0


def number_to_hua(x):
    if x == 1:
        return '&'
    if x == 2:
        return '$'
    if x == 3:
        return '#'
    if x == 4:
        return '*'

def hua_to_number(x):
    if x == '&':
        return 1
    if x == '$':
        return 2
    if x == '#':
        return 3
    if x == '*':
        return 4

def num_stand(x):
    if x<=10:
        return str(x)
    else:
        if x==11:
            return 'J'
        if x==12:
            return 'Q'
        if x==13:
            return 'K'
        if x==14:
            return 'A'

def main():
    tic = time.time()
    urllogin = "https://api.shisanshui.rtxux.xyz/auth/login"
    payload = "{\"username\":\"test\",\"password\":\"test\"}"
    headers = {'content-type': 'application/json'}
    response1 = requests.request("POST", urllogin, data=payload, headers=headers)
    s = json.loads(response1.text)
    # print(s)
    # print(s["data"]["token"])
    token = s["data"]["token"]
    # print(token)
    urlopen = "https://api.shisanshui.rtxux.xyz/game/open"
    headers = {'x-auth-token': token}
    count = 2
    cardcount = 0
    for i in range(1, count):
        response2 = requests.request("POST", urlopen, headers=headers)
        r = json.loads(response2.text)
        # print(r)
        card = r["data"]["card"]
        # print(card)
        # print(id)
        id = r["data"]["id"]
        for j in range(0, len(card)):
            if card[j] == ' ':
                continue
            else:
                if card[j] in '#$&*':
                    huase = card[j]
                    continue
                else:
                    if cardcount == 13:
                        break
                    cardcount = cardcount + 1
                    if card[j] in '23456789':
                        num = int(card[j])
                    if card[j] in '1':
                        num = 10
                        j = j + 1
                    if card[j] == 'J':
                        num = 11
                    if card[j] == 'Q':
                        num = 12
                    if card[j] == 'K':
                        num = 13
                    if card[j] == 'A':
                        num = 14
                    # print(hua_to_number(huase), num)
                    poker_1[cardcount] = Card(hua_to_number(huase), num)
            # print(hua, num)
    dfs_1(1, 1)
    qiandun =''
    zhongdun=''
    weidun=''
    for i in range(1, 4):
        end_3[i].num=num_stand(end_3[i].num)
        if i != 3:
            # print(number_to_hua(end_3[i].flower), end="")
            # print(end_3[i].num, end=" ")
            qiandun = qiandun + number_to_hua(end_3[i].flower) + str(end_3[i].num) + ' '
        else:
            # print(number_to_hua(end_3[i].flower), end="")
            # print(end_3[i].num)
            qiandun = qiandun + number_to_hua(end_3[i].flower) + str(end_3[i].num)
    qiandun=str(qiandun)
    print(qiandun)
    for i in range(1, 6):
        end_2[i].num=num_stand(end_2[i].num)
        if i != 5:
            # print(number_to_hua(end_2[i].flower), end="")
            # print(end_2[i].num, end=" ")
            zhongdun = zhongdun + number_to_hua(end_2[i].flower) + str(end_2[i].num) + ' '
        else:
            # print(number_to_hua(end_2[i].flower), end="")
            # print(end_2[i].num)
            zhongdun = zhongdun + number_to_hua(end_2[i].flower) + str(end_2[i].num)
    zhongdun=str(zhongdun)
    print(zhongdun)
    for i in range(1, 6):
        end_1[i].num=num_stand(end_1[i].num)
        if i != 5:
            # print(number_to_hua(end_1[i].flower), end="")
            # print(end_1[i].num, end=" ")
            weidun = weidun + number_to_hua(end_1[i].flower) + str(end_1[i].num) + ' '
        else:
            # print(number_to_hua(end_1[i].flower), end="")
            # print(end_1[i].num)
            weidun = weidun + number_to_hua(end_1[i].flower) + str(end_1[i].num)
    weidun=str(weidun)
    print(weidun)
    id=str(id)
    # print(id)
    urlchupai = "https://api.shisanshui.rtxux.xyz/game/submit"
    payload = "{\"id\":"+id+",\"card\":[\""+qiandun+"\",\""+zhongdun+"\",\""+weidun+"\"]}"
    headers = {
        'content-type': "application/json",
        'x-auth-token': token
    }
    responsechupai = requests.request("POST", urlchupai, data=payload, headers=headers)
    print(responsechupai.text)
    # toc = time.time()
    # print(toc-tic)


if __name__ == '__main__':
    main()






