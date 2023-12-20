from PIL import Image, ImageEnhance
from io import BytesIO
import requests
import imageUtils as iu

# ---------------------------- WALPAPER ---------------------------- 

def walpaperPremium(bgn, colorful, sbgn, letters, color, type):
    
    # If bgn isn't a number string, it means it is an URL for a custom background
    if not bgn.isdigit():
        # Replace 'your_url_here' with the actual URL of the image
        imagepath = bgn

        image1 = Image.open(imagepath)
        image1 = image1.resize((1920, 1080))
        image1 = image1.convert("L")
        enhancer = ImageEnhance.Brightness(image1)
        image1 = enhancer.enhance(0.15)
    else:
            image1 = Image.open(f'./Backgrounds/BackGround{bgn}.png')
            image1 = image1.resize((1920, 1080))

    image2 = Image.open(f'./walpaperSub/{sbgn}.png').resize((1920,1080))
    image4 = Image.open(f'./Shadow.png').resize((1920,1080))

    # Create a new blank image with the same size
    result_image = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))

    # Paste the images onto the new image
    result_image.paste(image1, (0, 0))
    if colorful:
        colorful = Image.open(f"./walpaperSub/COLORFUL.png")
        result_image.paste(colorful,(0, 0),colorful)
    result_image.paste(image2, (0, 0), image2)
    result_image.paste(image4, (0, 0), image4)

    total_width = 1500
    num_letters = len(letters)
    
    max_margin = 100
    margin = - min(max_margin, total_width // (2 * num_letters))

    letter_width = (total_width - (num_letters - 1) * margin) // num_letters

    letter_height = letter_width

    starting_x = (1920 - total_width) // 2

    starting_y = (1080 - letter_height) // 2

    for i, letter in enumerate(letters):
        if letter != " ":
            letter_image = Image.open(f'./Letters/{type}/{letter}.png')
        else:
            letter_image = Image.open(f'./Letters/space.png')
        letter_image = letter_image.resize((letter_width, letter_height))
        result_image.paste(letter_image, (starting_x + i * (letter_width + margin), starting_y), letter_image)

    logo = result_image

        
    hue = iu.color2hue(color)
    logo = iu.change_hue(result_image, hue)

    if(color == "#000000" or color == "#ffffff"):
        logo = logo.convert("L")

    logo.save(f'./History/wallpaper{sbgn}{letters}{color}{type}.jpg')

    return f'./History/wallpaper{sbgn}{letters}{color}{type}.jpg'

# ---------------------------- TESTES ---------------------------- 

logo1= "https://img.freepik.com/premium-photo/aesthetic-beach-synthwave-retrowave-wallpaper-with-cool-vibrant-neon-design_398492-5639.jpg"
logo2 = "https://i1.sndcdn.com/artworks-Jyn5TkxFTfX5dD9u-z69zqw-t500x500.jpg"

#animatedLogoPremium("0","5"," ","purple")
#logoPremium("1","11","TEST","green","2")
#walpaperPremium("1", False ,"0","nao pia","#554645","2")