import random
import sys

while True:
    nums = [1200,800,600,200]
    food = ['jablka','švestky','pomeranče','banány']

    for i in range(4):
        counter = 1
        for item in nums:
            while True:
                random.shuffle(nums)

                if counter == 4:
                    print(nums)

                elif item != nums[counter]:
                    break
                    counter += 1
