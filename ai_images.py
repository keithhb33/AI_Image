import requests
import shutil
import base64

def image(prompt):
    url = "https://backend.craiyon.com/generate"
    
    s = requests.Session()
    payload = {
        "prompt": prompt   
    }
    
    res = s.post(url, json=payload)
    return res.content

def generate_images(prompt, directory="", number_of_outputs=9):
    image_urls = str(image(prompt))
    image_urls = image_urls.replace('\\\\n', '')

    end_index = int(image_urls.index('],"version') - 1)
    
    image_urls = image_urls[14:end_index]
    image_list = image_urls.split('","')
    
    c = 0
    for i in range(number_of_outputs):
        c+=1
        chosen_image = image_list[i]
        
        imgdata = base64.b64decode(chosen_image)
        filename = 'output' + str(c) + '.jpg'

        if directory != "":
            filename = directory + "/output" + str(c) + '.jpg'

        with open(filename, 'wb') as f:
            f.write(imgdata)

    print("success")


