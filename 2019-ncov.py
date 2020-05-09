# -*- coding: UTF-8 -*-

'''
对此次武汉新型冠状病毒传播的简单模拟,地区固定为15个城市，无限制条件下传播速度为指数增长，
患病者每天最多可传染个同地区的一个人，若未发生传染则可认为免疫抵抗，人类行为对传染速度的影响
简化为一次春节返乡，即所在地变化一次，对比项为所有人都返乡和四分之一人返乡
'''

from random import randint
from collections import defaultdict


'''建立可被感染的人类模型'''
class Person():
	
	'''属性初始化'''
	def __init__(self,id,location,destination,statu='h'):
		'''id 每个对象的唯一标识，区分人与人'''
		self.id=id
		'''location 对象当前所在地'''
		self.location=location
		'''destination 对象返乡目的地'''
		self.destination=destination
		'''status 对象身体状况，h代表健康，uh代表被感染'''
		self.statu=statu
	
	'''模拟春节返乡行为'''
	def action(self):
		self.location=self.destination
	
	'''模拟被感染'''
	def infected(self):
		self.statu='uh'


if __name__=='__main__':

	'''模型参数设置'''
	area=('武汉','杭州','广州','北京','芜湖','上海','深圳','香港',
		'长沙','南昌','南京','合肥','成都','长春','南宁')#模拟全国地区
	population=int(input('总人数为：'))#设置全国人口
	days=int(input('模拟传染的总天数:'))#模拟传染的总天数
	festival=int(input('春节回乡在第n天:'))#假设春节回乡在第n天
	model=int(input('请输入传播的方式(1/2),1代表所有人回家过年，2代表四分之一的人回家过年:'))

	'''详细内容写入文件'''
	filename='report.txt'
	with open(filename,'a') as file_object:
		file_object.write('\n'*2+'*'*50+'\n条件设置'+'\n全国人口为:'+
			str(population)+'\n模拟天数为:'+str(days)+'\n第'+str(festival)
			+'天为春节回乡日'+'\n'+'地区为:'+str(area)+'\n')

	'''生成人类群体'''
	people=[]
	for id in range(population):
		person=Person(id,area[randint(0,len(area)-1)],area[randint(0,len(area)-1)])
		people.append(person)
	for id in range(population):
		with open(filename,'a') as file_object:
			file_object.write('第'+str(people[id].id)+'位，'+'当前所在地'+
				people[id].location+',春节要回'+people[id].destination+'\n')

	'''生成地区索引，将人按当前所在地分类'''
	index_location=[]
	for id in range(population):
		index_location.append(people[id].location)
	location_dict=defaultdict(list)
	for key,value in [(l,i) for i,l in enumerate(index_location)]:
		location_dict[key].append(value)
	with open(filename,'a') as file_object:
		file_object.write(str(location_dict)+'\n')

	'''建立病人名单'''
	patients=[]

	'''产生首位病人'''
	lucky_num=randint(0,population-1)#天选
	people[lucky_num].statu='uh'#天选之人吃蝙蝠
	with open(filename,'a') as file_object:
		file_object.write(str(people[lucky_num].id)+'号首例感染病毒'+'\n')
	print(str(people[lucky_num].id)+'号首例感染病毒')
	patients.append(people[lucky_num])#将病人加入病人名单

	'''模拟传播感染过程'''
	count=0#计数器，表示当前天数
	while True:
		patients_copy=patients[:]#建立病人名单的副本
		with open(filename,'a') as file_object:
			file_object.write('======第'+str(count+1)+'天======\n')
		print('======第'+str(count+1)+'天======')
		'''每位病人感染当前所在地区的某1个人'''
		for patient in patients_copy:
			infected_area=location_dict[patient.location]#确定病人所在的地区有哪些人
			with open(filename,'a') as file_object:
				file_object.write('被感染的地区有'+str(infected_area)+'号。\n')
			'''随机传染，如果随机到自己，则病人这一天没有传染给别人'''
			random_num=randint(0,len(infected_area)-1)
			infected_person=people[infected_area[random_num]]
			if infected_person in patients:
				pass
			else:
				infected_person.statu='uh'
				with open(filename,'a') as file_object:
					file_object.write(str(infected_person.id)+'号被感染\n')
				print(str(infected_person.id)+'号被感染')
				patients.append(infected_person)
				
		count+=1#一天结束
		
		if count==festival:#到春节这一天有人返乡
			if model==1:
				for person in people:
					person.action()
				print('所有人回家过春节')
			else:
				for person in people[:int(len(people)/4)]:
					person.action()
				print('部分人回家过春节')

		if count==days:#循环结束，模拟传染过程完成
			break

'''数据统计'''
print('总共被感染人数为：'+str(len(patients)))

infected_area_name=[]
for patient in patients:
	infected_area_name.append(patient.location)
print('被感染的地区有：'+str(set(infected_area_name)))

with open(filename,'a') as file_object:
	file_object.write('总共被感染人数为：'+str(len(patients))+'\n'
		'被感染的地区有：'+str(set(infected_area_name))+'\n')
