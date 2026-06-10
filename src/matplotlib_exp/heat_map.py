import os
from math import ceil

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

sns.set_theme(style='white')
# sns.set_theme(style='dark')

CURR_DIR = os.path.dirname(__file__)

sheet_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
data_dict = {
    "A": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    "B": [25, 14, 0, 0, 4, 0, 0, 0, 0, 0, 0, 71, 0, 0, 114],
    "C": [0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10],
    "D": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    "E": [68, 0, 0, 207, 1, 0, 8, 5, 2, 3, 2, 0, 0, 0, 296],
    "F": [0, 0, 0, 0, 78, 0, 1, 0, 0, 0, 0, 0, 0, 0, 79],
    "G": [0, 0, 0, 0, 0, 0, 0, 0, 174, 0, 0, 0, 41, 0, 215],
}

dict_values = list(data_dict.values())
np_data = np.array(dict_values)
all_data = np.sum(np_data, axis=0)

domains = list(data_dict.keys())
data_props = []
for idx_row, np_line in enumerate(np_data):
    line_data = []
    for idx_col, np_item in enumerate(np_line):
        value = int(ceil(np_item * 100 / all_data[idx_col])) if all_data[idx_col] > 0 else 0
        line_data.append(value)
    data_props.append(line_data)

np_data_props = np.array(data_props)
np_dataprops = np.array(np_data_props).astype(int)

np_domains = np.array([[k] for k in domains])
# np_data_proportions = np.concatenate([np_domains, np_data_props], axis=1)

df = pd.DataFrame(np_data_props, columns=sheet_names)
# df = df.set_index("domain")


colors = [[0, 'white'],
          [1, 'blue']]
cmap = LinearSegmentedColormap.from_list('', colors)

ax = sns.heatmap(df, annot=True, fmt=".0f",  # fmt="d",
                 cmap=cmap,
                 # linecolor="#f6f6f6",  #"'gray',
                 # linewidths=.5,
                 yticklabels=domains, annot_kws={"fontsize": 8})
for i in range(df.shape[1] + 1):
    ax.axvline(i, color='#d9d9d9', lw=.5)
ax.set(xlabel="Proportion of entries per topic (%)",
       ylabel="Domains")
figure = ax.get_figure()
plt.tight_layout()
figure.savefig(
    os.path.join(CURR_DIR, 'heatmap.png'), dpi=400)
