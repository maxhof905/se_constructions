import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#%%
number_of_loops= 10
accuracies = [0.5, 0.55, 0.6, 0.6, 0.7, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]

#%%
# plot learning curve
with plt.style.context('bmh'):
    plt.figure(figsize=(12, 8))
    plt.title('Active learning loop')
    plt.plot(range(number_of_loops+1), accuracies)
    plt.scatter(range(number_of_loops+1), accuracies)
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.xticks(np.arange(0, 11, 1))
    plt.xlabel('loop number')
    plt.ylabel('accuracy')
    plt.tight_layout()
    plt.show()