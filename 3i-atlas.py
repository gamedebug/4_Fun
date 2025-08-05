from astroquery.jplhorizons import Horizons
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D)
import pandas as pd
# 设置查询参数：3I/ATLAS，查询为期 100 天的位置数据
obj = Horizons(
    id='C/2025 N1',
    location='500@10',  # 太阳系质心
    epochs={'start': '2025-07-01', 'stop': '2025-08-05', 'step': '1d'},
    id_type='smallbody'  # 明确是小天体
)
# 获取状态向量
vectors = obj.vectors()
df = vectors.to_pandas()
# 提取空间坐标
x = df['x'].astype(float)
y = df['y'].astype(float)
z = df['z'].astype(float)
# 可视化轨道轨迹
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='3I/ATLAS Trajectory', color='blue')
# 绘制太阳位置
ax.scatter(0, 0, 0, color='orange', s=100, label='Sun')
# 设置标签和图例
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.set_title('3I/ATLAS Trajectory (2025-07 to 2025-11)')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()
