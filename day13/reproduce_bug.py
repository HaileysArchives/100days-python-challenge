# Reproduce the Bug

from random import randint

dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6) # => so we need to change randint(0, 6)

print(dice_imgs[dice_num])

# That case is occasionally you will get an error. so these types of bugs are really difficult because you might test you code only once or twice, and it looks all fine. 


