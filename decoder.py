import base64

def decode(dataURL):
    with open("image_decoded.png", "wb") as save:
        save.write(base64.b64decode(dataURL))

    ##Lower code used if text is manually saved to file
    # img_data = ''
    # with open('data.txt', 'r') as data: ### Gets base64 string from data.txt in directory
    #     img_data = data.readline() 
    # with open("imageToSave.png", "wb") as save:
    #     save.write(base64.b64decode(img_data)) ### decodes and saves into imageToSave.png

decode(input())
