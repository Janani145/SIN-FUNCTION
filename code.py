import numpy as np

import matplotlib.pyplot 


x = np.arange(0, 2*(np.pi), 0.1)
y = np.sin(x)
matplotlib.pyplot.xlabel("x-axis")
matplotlib.pyplot.ylabel("y-axis")
try:
  plt.plot(x, y)
except Exception as e:
  print("Error plotting data:", e)
try:
  plt.show()
except Exception as e:
  print("Error showing plot:", e)
