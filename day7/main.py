# Iteration: Assignment

#1. For Loop Basics: Write a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

#2. String Iteration: Write a program that counts vowels in a string.
def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in 'aeiou':
            count += 1
            return count
        
#3. Accumulator Pattern: Calculate the sum of squares from 1 to 100.
sum_squares = 0
for i in range(1, 101):
    sum_squares += i ** 2
    print(sum_squares)

#4. Nested Loops: Create a multiplication table up to 10x10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')

#5. Image Processing: Use PIL to invert the colors of an image.
from PIL import Image
# Open the image file
img = Image.open('image.jpg')
# Invert the colors of the image
img = img.point(lambda x: 255 - x)
# Save the inverted image
img.save('inverted_image.jpg')
