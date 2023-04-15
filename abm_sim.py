import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置Matplotlib字体
plt.rcParams['font.family'] = ['Arial Unicode MS']

# 定义虚拟世界中的人类
class Person:
    def __init__(self, id):
        self.id = id
        self.ability = np.random.normal(loc=5, scale=2) # 设定能力值，符合正态分布
        self.wealth = 10 # 设定初始财富值为10

# 定义幸运与不幸事件
class Event:
    def __init__(self, id):
        self.id = id
        self.type = random.choice(['luck', 'misfortune']) # 50%概率的幸运或不幸事件

# 定义虚拟世界
class VirtualWorld:
    def __init__(self, num_people, num_events):
        self.people = [Person(i) for i in range(num_people)] # 创建人类
        self.events = [Event(i) for i in range(num_events)] # 创建事件
        self.luck_events_count = 0 # 幸运事件发生次数
        self.luck_events_affected = 0 # 幸运事件影响人数
        self.misfortune_events_count = 0 # 不幸事件发生次数
        self.misfortune_events_affected = 0 # 不幸事件影响人数

    # 模拟幸运事件
    def simulate_luck_event(self, person):
        wealth_increase = person.ability / 10 # 根据能力值计算财富增长百分比
        person.wealth *= (1 + wealth_increase) # 增加财富
        self.luck_events_affected += 1 # 增加影响人数

    # 模拟不幸事件
    def simulate_misfortune_event(self, person):
        person.wealth /= 2 # 减少财富
        self.misfortune_events_affected += 1 # 增加影响人数

    # 运行模拟程序
    def run_simulation(self, num_iterations):
        for i in range(num_iterations):
            # 随机运动幸运与不幸事件
            for event in self.events:
                event.type = random.choice(['luck', 'misfortune'])

            # 对于每个人，检查它是否与幸运或不幸事件相遇
            for person in self.people:
                event = random.choice(self.events)
                if event.type == 'luck':
                    self.simulate_luck_event(person)
                    self.luck_events_count += 1 # 增加幸运事件发生次数
                else:
                    self.simulate_misfortune_event(person)
                    self.misfortune_events_count += 1 # 增加不幸事件发生次数

        # 统计数据
        wealth_distribution = pd.DataFrame([person.wealth for person in self.people], columns=['wealth'])
        print("财富分布统计：\n", wealth_distribution.describe())

        # 绘制财富分布直方图
        plt.hist(wealth_distribution.wealth, bins=20)
        plt.title("财富分布")
        plt.xlabel("财富")
        plt.ylabel("人数")
        plt.show()

        # 输出事件统计数据
        print("幸运事件发生次数：", self.luck_events_count)
        print("幸运事件影响人数：", self.luck_events_affected)
        print("不幸事件发生次数：", self.misfortune_events_count)
        print("不幸事件影响人数：", self.misfortune_events_affected)


num_people = 10000 # 人数
num_events = 100 # 事件数
num_iterations = 2000 # 模拟次数
world = VirtualWorld(num_people, num_events)
world.run_simulation(num_iterations)

