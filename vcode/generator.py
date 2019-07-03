# Import ImageCaptcha class.
from captcha.image import ImageCaptcha
import random

# Create a new ImageCaptcha instance.
img = ImageCaptcha()

total = 100
numbers = []


def get_random_number():
    while True:
        number = str( random.randint(10000, 99999) )
        if number not in numbers:
            numbers.append(number)
            return number

for i in range(total) :
    number = get_random_number()
    # Generate image with the random number.
    image = img.generate_image(number)
    # Display the image
    # image.show()
    # Save the image to a file.
    image.save(f'samples/{number}.jpg')
