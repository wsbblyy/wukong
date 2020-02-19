# Import ImageCaptcha class.
from captcha.image import ImageCaptcha
import random

# Create a new ImageCaptcha instance.
img = ImageCaptcha(width=50)

total = 100
numbers = []


def get_random_number():
    # while True:
    #     number = str( random.randint(0,9) )
    #     if number not in numbers:
    #         numbers.append(number)
    #         return number
    return str( random.randint(0,9) )


for i in range(total) :
    number = get_random_number()
    # Generate image with the random number.
    image = img.generate_image(number)
    # Display the image
    # image.show()
    # Save the image to a file.
    name = number+'_'+str(random.randint(100000, 999999))
    image.save(f'/workspace/python/wukong/vcode/samples/{name}.jpg')
