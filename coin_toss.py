import numpy as np
np.random.rand(123)
coin = np.random.randint(1,3)

print(coin)
if coin == 1:
    print('heads')
else:
    print('tails')
