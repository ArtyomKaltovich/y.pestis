import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

os.environ['XDG_SESSION_TYPE'] = 'wayland'
os.environ['QT_QPA_PLATFORM'] = 'wayland'
DATA = {length: f"parebrick_{length}/preprocessed_data/blocks_coords.csv" for length in (1000, 5000)}


def unite_dfs(united_data, df):
    if united_data is None:
        united_data = df
    else:
        united_data = united_data.append(df)
    return united_data


def hist(data, plot_path):
    united_data = None
    for length, df in data.items():
        df = df.groupby("block").aggregate(dict(length="mean"))
        df["param"] = length
        united_data = unite_dfs(united_data, df)
    sns.histplot(data=united_data, x="length", hue="param", palette="pastel")
    plt.savefig(plot_path)
    plt.clf()


def u_curve(data, plot_path):
    united_data = None
    for length, df in data.items():
        df = pd.DataFrame(df.groupby("block")["species"].nunique().sort_values().value_counts())
        df["param"] = length
        united_data = unite_dfs(united_data, df)
    sns.lineplot(data=united_data, x=united_data.index, y="species", hue="param", palette="pastel", linewidth=2.5)
    plt.savefig(plot_path)
    plt.clf()


def len_freq_plot(data, plot_path):
    united_data = None
    for length, df in data.items():
        df = df.groupby("block").aggregate(dict(length="mean", species="nunique"))
        df["param"] = length
        united_data = unite_dfs(united_data, df)
    sns.scatterplot(data=united_data, x="species", y="length", hue="param", palette="pastel")
    plt.savefig(plot_path)
    plt.clf()


if __name__ == '__main__':
    data = {}
    for length, path in DATA.items():
        df = pd.read_csv(path)
        df["length"] = df["chr_end"] - df["chr_beg"]
        data[length] = df
    hist(data, "plot/block_hist.png")
    u_curve(data, "plot/u_curve_block.png")
    len_freq_plot(data, "plot/len_freq_plot.png")
