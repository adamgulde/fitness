import base64

def decode(dataURL, mode:int, num=0):
    if mode==1:
        with open("data/image_decoded.png", "wb") as save:
            save.write(base64.b64decode(dataURL))
    if mode==2: 
        with open(f"data/image_decoded{num}.png", "wb") as save:
            save.write(base64.b64decode(dataURL))
    else: 
        print('\nDECODE:\nUnhandled exception- bad "mode" input\n\n')


###Lower code used if text is manually saved to file
# img_data = ''
# with open('data.txt', 'r') as data: ### Gets base64 string from data.txt in directory
#     img_data = data.readline() 
# with open("imageToSave.png", "wb") as save:
#     save.write(base64.b64decode(img_data)) ### decodes and saves into imageToSave.png

### If you want to manually input b64 (but copy+paste has limits)
#   if __name__=="__main__":
#      decode(input())
