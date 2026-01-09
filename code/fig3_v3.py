import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import matplotlib as mpl
from matplotlib.colors import to_rgba

# =========================
# Color palette (easy to edit)
# =========================
color1 = '#0080FE'            # Primary color (ESM)
color1_alpha = to_rgba(color1, 0.5)

color2 = '#CD6600'            # Secondary color (EC)
color2_alpha = to_rgba(color2, 0.5)

color_span = '#a0a0a0'        # Background span (Land Q)
color_span_alpha = to_rgba(color_span, 0.1)

color_axis = '#454545'        # Axes, ticks, etc.

# =========================
# Matplotlib global settings
# =========================
# SVG文字可编辑设置
mpl.rcParams['svg.fonttype'] = 'none'
mpl.rcParams['svg.hashsalt'] = 'hello'

# EPS/PDF字体设置（确保兼容性）
mpl.rcParams['pdf.fonttype'] = 42  # TrueType字体
mpl.rcParams['ps.fonttype'] = 42   # EPS使用TrueType字体

# 全局字体设置为Arial
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.sans-serif'] = ['Arial']
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.rm'] = 'Arial'
mpl.rcParams['mathtext.it'] = 'Arial:italic'
mpl.rcParams['mathtext.bf'] = 'Arial:bold'

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
    'axes.edgecolor': color_axis,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 8,
    'ytick.major.size': 8,
    'xtick.minor.size': 4,
    'ytick.minor.size': 4,
    'xtick.major.width': 1.0,
    'ytick.major.width': 1.0,
    'xtick.minor.width': 1.0,
    'ytick.minor.width': 1.0,
    'xtick.color': color_axis,
    'ytick.color': color_axis,
    'savefig.bbox': 'tight',
    'savefig.transparent': False
})

# 读取数据
df = pd.read_csv('../data/Data for main figures.csv', header=[0, 1])

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
cap_width = 0.08  # 折线端点的宽度

# 辅助函数：绘制圆点和区间折线
def plot_interval_with_caps(ax, x_positions, y_values, y_errors, color, label, offset=0):
    """
    绘制加粗圆点和上下折线表示区间
    """
    x_pos = x_positions + offset
    
    for xi, yi, yerri in zip(x_pos, y_values, y_errors):
        # 绘制中心圆点（加粗，无黑色外框）
        ax.plot(xi, yi, 'o', color=color, markersize=10, 
               markeredgecolor='none', zorder=3)
        
        # 计算上下界
        y_lower = yi - yerri
        y_upper = yi + yerri
        
        # 绘制垂直线（连接上下界，加粗）
        ax.plot([xi, xi], [y_lower, y_upper], color=color, 
               linewidth=3.0, alpha=0.7, zorder=2)

# 图3a - SSP2-4.5
plot_interval_with_caps(ax1, x, ssp245_esm, ssp245_esm_err, color1, 'ESM', offset=-width/2)
plot_interval_with_caps(ax1, x, ssp245_ec, ssp245_ec_err, color2, 'EC', offset=width/2)

# 手动创建图例
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color=color1, linewidth=3, 
           markersize=8, markeredgecolor='none', label='ESM'),
    Line2D([0], [0], marker='o', color=color2, linewidth=3, 
           markersize=8, markeredgecolor='none', label='EC')
]
ax1.legend(handles=legend_elements, loc='upper left', frameon=False, title='Mean $\pm$ 1 std')

ax1.set_ylabel('Change in water cycle components (mm year$^{-1}$)', fontsize=15)
ax1.set_title('a', fontsize=24, fontweight='bold', loc='left')
ax1.set_xticks(x)
ax1.set_xticklabels(components, rotation=0, ha='center')
ax1.set_ylim(0, 100)
ax1.set_yticks(np.arange(0, 101, 20))
ax1.set_xlim(-0.5, 4.5)
ax1.set_axisbelow(True)
ax1.axvspan(x[4] - width - 0.15, 4.5, facecolor=color_span, alpha=color_span_alpha[-1], zorder=0)

# 图3b - SSP5-8.5
plot_interval_with_caps(ax2, x, ssp585_esm, ssp585_esm_err, color1, 'ESM', offset=-width/2)
plot_interval_with_caps(ax2, x, ssp585_ec, ssp585_ec_err, color2, 'EC', offset=width/2)

ax2.set_ylabel('Change in water cycle components (mm year$^{-1}$)', fontsize=15)
ax2.set_title('b', fontsize=24, fontweight='bold', loc='left')
ax2.set_xticks(x)
ax2.set_xticklabels(components, rotation=0, ha='center')
ax2.set_ylim(0, 120)
ax2.set_yticks(np.arange(0, 121, 20))
ax2.set_xlim(-0.5, 4.5)
ax2.set_axisbelow(True)
ax2.axvspan(x[4] - width - 0.15, 4.5, facecolor=color_span, alpha=color_span_alpha[-1], zorder=0)

# 图3c - SSP5-8.5 per degree
plot_interval_with_caps(ax3, x, ssp585_esm_perdeg, ssp585_esm_perdeg_err, color1, 'ESM', offset=-width/2)
plot_interval_with_caps(ax3, x, ssp585_ec_perdeg, ssp585_ec_perdeg_err, color2, 'EC', offset=width/2)

ax3.set_ylabel('Change in water cycle components \nper degree warming (mm year$^{-1}$ K$^{-1}$)', fontsize=15)
ax3.set_title('c', fontsize=24, fontweight='bold', loc='left')
ax3.set_xticks(x)
ax3.set_xticklabels(components, rotation=0, ha='center')
ax3.set_ylim(-20, 80)
ax3.set_yticks(np.arange(-20, 81, 20))
ax3.set_xlim(-0.5, 4.5)
ax3.set_axisbelow(True)
ax3.axvspan(x[4] - width - 0.15, 4.5, facecolor=color_span, alpha=color_span_alpha[-1], zorder=0)

# 调整布局
plt.tight_layout()

# 保存图形
plt.savefig('../figure/fig3_v3.png', dpi=600, bbox_inches='tight')
plt.savefig('../figure/fig3_v3.pdf', dpi=600, bbox_inches='tight')

print("图3 v3已生成并保存到figure文件夹（PNG和PDF格式，600dpi）")
print("v3版本特点：")
print("- 使用加粗圆点表示均值")
print("- 使用上下折线表示标准差区间")
print("- 简洁清晰的区间图风格")
