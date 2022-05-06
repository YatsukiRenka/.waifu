from itertools import count
import time
import numpy as np
import matplotlib.pyplot as plt

# 输入random次数
times = input(".coc7 ")
times = int(times)

# 开始计时
timer_start = time.time()

# 建卡

def rd6():
    return np.random.randint(1, 7)

class COC:
    def __init__(self, str, con, siz, dex, app, int, pow, edu, sum):
        self.str = str
        self.con = con
        self.siz = siz
        self.dex = dex
        self.app = app
        self.int = int
        self.pow = pow
        self.edu = edu
        self.sum = self.str + self.con + self.siz + self.dex + self.app + self.int + self.pow + self.edu
        
    def STR(self):
        return self.str
    def CON(self):
        return self.con
    def SIZ(self):
        return self.siz
    def DEX(self):
        return self.dex
    def APP(self):
        return self.app
    def INT(self):
        return self.int
    def POW(self):
        return self.pow
    def EDU(self):
        return self.edu
    def SUM(self):
        return self.sum
    
# 掷骰方法

def COC7():
    str = (rd6() + rd6() + rd6()) * 5
    con = (rd6() + rd6() + rd6()) * 5
    siz = (rd6() + rd6() + 6) * 5
    dex = (rd6() + rd6() + rd6()) * 5
    app = (rd6() + rd6() + rd6()) * 5
    int = (rd6() + rd6() + 6) * 5
    pow = (rd6() + rd6() + rd6()) * 5
    edu = (rd6() + rd6() + 6) * 5
    player = COC(str, con, siz, dex, app, int, pow, edu, sum)
    return player

#Analyze

def plot(sum_list):
    num_bins = 131
    n, bins, patches = plt.hist(sum_list, num_bins, facecolor='blue', alpha=0.5)
    plt.xlabel('SUM') 
    plt.ylabel('COUNT') 
    plt.title(r'.coc7')
    plt.show()

# 掷骰

def roll():
    i = 0
    sum = []
    waifucount = 0
    over600count = 0
    while i < times:
        player = COC7()
        sum.append(player.SUM())
        if (player.SUM() >= 600):#总属性>=600
            over600count += 1
            if (player.SIZ() <= 60):#体型<=60
                if (player.APP() >= 85):#外貌>=85
                    waifucount += 1
                    if (waifucount == 1):
                        print("STR"+"\t"+"CON"+"\t"+"SIZ"+"\t"+"DEX"+"\t"+"APP"+"\t"+"INT"+"\t"+"POW"+"\t"+"EDU"+"\t"+"SUM")
                        print(str(player.STR())+"\t"+str(player.CON())+"\t"+str(player.SIZ())+"\t"+str(player.DEX())+"\t"+str(player.APP())+"\t"+str(player.INT())+"\t"+str(player.POW())+"\t"+str(player.EDU())+"\t"+str(player.SUM()))
                    if (waifucount > 1):
                        print(str(player.STR())+"\t"+str(player.CON())+"\t"+str(player.SIZ())+"\t"+str(player.DEX())+"\t"+str(player.APP())+"\t"+str(player.INT())+"\t"+str(player.POW())+"\t"+str(player.EDU())+"\t"+str(player.SUM()))
        i += 1
    if (waifucount == 0):
        print("!!! NO WAIFU !!!")
    print("OVER 600: " + str(over600count))
    plot(sum)# 绘制直方图

# run
roll()

# 结束计时
timer_end = time.time()
print("Running Time: " + str(timer_end - timer_start) + "s")