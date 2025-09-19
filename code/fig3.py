import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from matplotlib import font_manager
import matplotlib as mpl

plt.rcParams['font.family'] = 'Arial'
mpl.rcParams['svg.fonttype'] = 'none'
mpl.rcParams['svg.hashsalt'] = 'hello'

# Set Nature style parameters
plt.style.use('seaborn-v0_8-talk')
plt.rcParams.update({
    'font.family': 'Arial',
    'font.size': 15,
    'axes.titlesize': 15,
    'axes.labelsize': 15,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'legend.fontsize': 14,
    'figure.dpi': 600,
    'figure.figsize': (6, 4),
    'lines.linewidth': 1.0,
    'axes.linewidth': 1.0,
    'axes.spines.left': True,
    'axes.spines.bottom': True,
    'axes.spines.top': True,
    'axes.spines.right': True,
    'axes.edgecolor': '#454545',
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 8,
    'ytick.major.size': 8,
    'xtick.minor.size': 4,
    'ytick.minor.size': 4,
    'xtick.major.width': 1.0,
    'ytick.major.width': 1.0,
    'xtick.minor.width': 1.0,  # 新增：小刻度线宽度
    'ytick.minor.width': 1.0,  # 新增：小刻度线宽度
    'xtick.color': '#454545',  # 新增：x轴刻度线颜色
    'ytick.color': '#454545',  # 新增：y轴刻度线颜色
    'savefig.bbox': 'tight',
    'savefig.transparent': False
})


# 读取数据
df = pd.read_csv('../data/Data for main figures.csv', header=[0,1])

# 提取图3数据
components = ['Ocean P', 'Ocean E', 'Land P', 'Land E', 'Land Q']

# SSP2-4.5数据
ssp245_esm = df.iloc[0:5, 1].values.astype(float)
ssp245_esm_err = df.iloc[0:5, 2].values.astype(float)
ssp245_ec = df.iloc[0:5, 3].values.astype(float)
ssp245_ec_err = df.iloc[0:5, 4].values.astype(float)

# SSP5-8.5数据
ssp585_esm = df.iloc[0:5, 7].values.astype(float)
ssp585_esm_err = df.iloc[0:5, 8].values.astype(float)
ssp585_ec = df.iloc[0:5, 9].values.astype(float)
ssp585_ec_err = df.iloc[0:5, 10].values.astype(float)

# Pannel C数据（per degree）
ssp585_esm_perdeg = df.iloc[0:5, 13].values.astype(float)
ssp585_esm_perdeg_err = df.iloc[0:5, 14].values.astype(float)
ssp585_ec_perdeg = df.iloc[0:5, 15].values.astype(float)
ssp585_ec_perdeg_err = df.iloc[0:5, 16].values.astype(float)

# 创建图形
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 4.7))
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 11

# 设置x轴位置
x = np.arange(len(components))
width = 0.35

# 图3a - SSP2-4.5（修改成和b一样的误差棒格式）
bars1 = ax1.bar(
    x - width/2, ssp245_esm, width, label='ESM', color='#96c6ea',
    yerr=[np.zeros_like(ssp245_esm_err), ssp245_esm_err], capsize=3,
    error_kw={'ecolor': '#96c6ea', 'linewidth': 2.5}
)
bars2 = ax1.bar(
    x + width/2, ssp245_ec, width, label='EC', color='#fdd0a2',
    yerr=[np.zeros_like(ssp245_ec_err), ssp245_ec_err], capsize=3,
    error_kw={'ecolor': '#fdd0a2', 'linewidth': 2.5}
)

ax1.set_ylabel('Change in water cycle components (mm year$^{-1}$)', fontsize=15)
ax1.set_title('a', fontsize=24, fontweight='bold', loc='left')
ax1.set_xticks(x)
ax1.set_xticklabels(components, rotation=0, ha='center')
ax1.legend(loc='upper left', frameon=False)
ax1.set_ylim(0, 100)
ax1.set_yticks(np.arange(0, 101, 20))
ax1.set_xlim(-0.5, 4.5)  # 固定x轴范围
ax1.set_axisbelow(True)

# 添加Land Q的灰色背景，延伸到图框右边
ax1.axvspan(x[4] - width - 0.15, 4.5, alpha=0.1, color='gray', zorder=0)

# 图3b - SSP5-8.5
bars3 = ax2.bar(
    x - width/2, ssp585_esm, width, label='ESM', color='#96c6ea',
    yerr=[np.zeros_like(ssp585_esm_err), ssp585_esm_err], capsize=3,
    error_kw={'ecolor': '#96c6ea', 'linewidth': 2.5}
)
bars4 = ax2.bar(
    x + width/2, ssp585_ec, width, label='EC', color='#fdd0a2',
    yerr=[np.zeros_like(ssp585_ec_err), ssp585_ec_err], capsize=3,
    error_kw={'ecolor': '#fdd0a2', 'linewidth': 2.5}
)

#ax2.set_xlabel('Water cycle component', fontsize=12)
ax2.set_ylabel('Change in water cycle components (mm year$^{-1}$)', fontsize=15)
ax2.set_title('b', fontsize=24, fontweight='bold', loc='left')
ax2.set_xticks(x)
ax2.set_xticklabels(components, rotation=0, ha='center')
#ax2.legend(loc='upper right', frameon=False)
ax2.set_ylim(0, 100)
ax2.set_yticks(np.arange(0, 101, 20))
ax2.set_xlim(-0.5, 4.5)  # 固定x轴范围
ax2.set_axisbelow(True)

# 添加Land Q的灰色背景，延伸到图框右边
ax2.axvspan(x[4] - width - 0.15, 4.5, alpha=0.1, color='gray', zorder=0)

# 图3c - SSP5-8.5 per degree
bars5 = ax3.bar(
    x - width/2, ssp585_esm_perdeg, width, label='ESM', color='#96c6ea',
    yerr=[np.zeros_like(ssp585_esm_perdeg_err), ssp585_esm_perdeg_err], capsize=3,
    error_kw={'ecolor': '#96c6ea', 'linewidth': 2.5}
)
bars6 = ax3.bar(
    x + width/2, ssp585_ec_perdeg, width, label='EC', color='#fdd0a2',
    yerr=[np.zeros_like(ssp585_ec_perdeg_err), ssp585_ec_perdeg_err], capsize=3,
    error_kw={'ecolor': '#fdd0a2', 'linewidth': 2.5}
)

ax3.set_ylabel('Change in water cycle components \nper degree warming (mm year$^{-1}$ K$^{-1}$)', fontsize=15)
ax3.set_title('c', fontsize=24, fontweight='bold', loc='left')
ax3.set_xticks(x)
ax3.set_xticklabels(components, rotation=0, ha='center')
ax3.set_ylim(0, 100)
ax3.set_yticks(np.arange(0, 101, 20))
ax3.set_xlim(-0.5, 4.5)  # 固定x轴范围
ax3.set_axisbelow(True)

# 添加Land Q的灰色背景，延伸到图框右边
ax3.axvspan(x[4] - width - 0.15, 4.5, alpha=0.1, color='gray', zorder=0)

# 调整布局
plt.tight_layout()

# 保存图形
plt.savefig('../figure/fig3.png', dpi=600, bbox_inches='tight')

print("图1已生成并保存到figure文件夹")