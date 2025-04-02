# Question 2: https://cs50.harvard.edu/python/2022/psets/0/playback/

# Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

# In a file called playback_speed.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

slowed_input = input('Say something, anything: ').replace(' ', '...')
print(slowed_input)
