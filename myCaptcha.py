from PIL import Image , ImageDraw , ImageFont , ImageFilter
from random import randint, randrange
from time import sleep

# generate random string from given characters
def randomGenerator():
    key = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    randomCode = ''
    for i in range(randint(4,6)):
        randomCode += key[randrange(0,71)]
    
    return randomCode

def captcha(string = randomGenerator(), x=230, y=80, blurRange=2, effect=None):
    """
    Create a captcha and save it in the current directory
    string : by default the string will be a count of random characters
    between 4 and 6  
    
    x = an int for width of the image (default 230)
    y = an int for height of the image (default 80)

    effect = available effect are: EDGE_ENHANCE, EMBOSS, FIND_EDGES, MinFilter, CONTOUR
    """

    # create the image
    img = Image.new('RGB', (x,y),(255,255,255))

    # create a draw object
    draw = ImageDraw.Draw(img)

    # define font
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 50)


    # draw random pixels
    for i in range(x):
        for j in range(y):
            ImageDraw.Draw(img).point((i,j),fill=(randint(150,255),randint(150,255),randint(150,255)))

            # uncomment this codes to show the pixels drawing steps
            # sleep(0.005)
            # img.save('name.jpg', 'jpeg')


    # daraw random lines
    for i in range(randint(9,15)):
        start = (randint(0,x),randint(0,y))
        end = (randint(0,x),randint(0,y))
        draw.line([start,end],fill=(randint(0,150),randint(0,150),randint(0,150)))
        
        # uncomment this to show line drawing steps
        # sleep(1)
        # img.save('name.jpg', 'jpeg')

    # draw characters
    for i in range(len(string)):
        draw.text((randint(30,50) + i*30, randint(5,30)), string[i],  font=font,fill=(randint(0,100),randint(0,100),randint(0,100)))
        
        # uncomment this lines to show characters drawing steps
        # img.save('name.jpg', 'jpeg')
        # sleep(1)


    if effect == 'EDGE_ENHANCE':
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif effect == 'EMBOSS':
        img = img.filter(ImageFilter.EMBOSS)
    elif effect == 'FIND_EDGES':
        img = img.filter(ImageFilter.FIND_EDGES)
    elif effect == 'MinFilter':
        img = img.filter(ImageFilter.MinFilter(3))
    elif effect == 'CONTOUR':
        img = img.filter(ImageFilter.CONTOUR)


    img = img.filter(ImageFilter.BoxBlur(blurRange))

# antihistamin
# abnamak

    # save created captcha in a file
    img.save('captcha.jpg', 'jpeg')

    return string

if __name__ == "__main__":
    captcha()
