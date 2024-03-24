import numpy as np
import matplotlib.pyplot as plt


def plot_1dhistos(data, features, bins=100):
    """
    Plot 1D histograms of the features in the data
    plot both linear and log scale on the right

    features: list of features names 
    if features is N_const, use linspace binning
    """
    n_features = len(features)
    fig, axs = plt.subplots(n_features, 2, figsize=(12, 4 * n_features))

    for i, feature in enumerate(features):
        if feature == 'N_const':
            binning = np.linspace(0, 100, 100)
        else:
            binning = bins
        axs[i, 0].hist(data[:, i], bins=binning, histtype='step', lw=2, alpha=0.7)
        axs[i, 0].set_title(feature)
        axs[i, 1].hist(data[:, i], bins=binning, histtype='step', lw=2, alpha=0.7)
        axs[i, 1].set_yscale('log')

    plt.tight_layout()
    plt.show()
    return