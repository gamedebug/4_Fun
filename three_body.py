import numpy as np
import matplotlib.pyplot as plt
import xlrd
from mpl_toolkits.mplot3d import Axes3D

#初始条件
dataSource=xlrd.open_workbook('/Users/louis/tmp/DataInput.xlsx')
data=dataSource.sheets()[0]

m1=data.cell(1,1).value
r1=np.array([data.cell(1,2).value,data.cell(1,3).value,data.cell(1,4).value])
v1=np.array([data.cell(1,5).value,data.cell(1,6).value,data.cell(1,7).value])

m2=data.cell(2,1).value
r2=np.array([data.cell(2,2).value,data.cell(2,3).value,data.cell(2,4).value])
v2=np.array([data.cell(2,5).value,data.cell(2,6).value,data.cell(2,7).value])

m3=data.cell(3,1).value
r3=np.array([data.cell(3,2).value,data.cell(3,3).value,data.cell(3,4).value])
v3=np.array([data.cell(3,5).value,data.cell(3,6).value,data.cell(3,7).value])

x1,y1,z1,x2,y2,z2,x3,y3,z3=[],[],[],[],[],[],[],[],[]

dt=0.005
N=2000

#创建三维图。
fig=plt.figure()
ax=plt.axes(projection='3d')

#两点间距
def distance_square(R1,R2):
    return np.dot(R2-R1,R2-R1)

#两点引力的大小
def force_magnitude(M1,R1,M2,R2):
    return M1*M2/(distance_square(R1, R2))

#由1指向2的单位矢量
def unit_vector(R1,R2): 
    return (R2-R1)/np.sqrt(distance_square(R1, R2))

#2对1的施力
def Force(M1,R1,M2,R2):
    return unit_vector(R1, R2) * force_magnitude(M1, R1, M2, R2)


#将食量R以速度v改变dt时间
def move(R,v): 
    R+=dt*v
    return

#矢量v受力改变dt时间
def accelerate(F,m,v):
    v+=F*dt/m
    return

for i in range(N):
    move(r1, v1)		#调用前面定义的move函数，改变各质点位置
    move(r2, v2)
    move(r3, v3)
    F21=Force(m1, r1, m2, r2)		#调用前面定义的Force函数，求得质点两两之间作用力
    F32=Force(m2, r2, m3, r3)
    F13=Force(m3, r3, m1, r1)
    accelerate(F21-F13, m1, v1)		#调用前面定义的accelerate函数，改变速度
    accelerate(F32-F21, m2, v2)
    accelerate(F13-F32, m3, v3)

    x1.append(r1[0])			#这一时刻新位置放入记录结果的列表中
    y1.append(r1[1])
    z1.append(r1[2])
    x2.append(r2[0])
    y2.append(r2[1])
    z2.append(r2[2])
    x3.append(r3[0])
    y3.append(r3[1])
    z3.append(r3[2])

ax.plot3D(x1,y1,z1, color='blue')
ax.plot3D(x2,y2,z2, color='red')
ax.plot3D(x3,y3,z3, color='green')

plt.show()