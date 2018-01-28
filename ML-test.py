import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_hight = 28 + 4 * np.random.randn(greyhounds)
labs_hight = 24 + 4 * np.random.randn(labs)

plt.hist ([grey_hight, labs_hight], stacked=True, color=['r','b'])
plt.show()

