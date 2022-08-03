import requests
import json
import base64

def image(prompt):
    url = "https://backend.craiyon.com/generate"
    
    s = requests.Session()
    payload = {
        "prompt": prompt   
    }
    
    res = s.post(url, json=payload)
    return res.content

def convert_jpg(prompt):
    image_urls = str(image(prompt))
    image_urls = image_urls.replace('\\\\n', '')

    end_index = int(image_urls.index('],"version') - 1)
    
    image_urls = image_urls[14:end_index]
    image_list = image_urls.split('","')
    
    c = 0
    for i in range(9):
        c+=1
        
        chosen_image = image_list[i]
        
        imgdata = base64.b64decode(chosen_image)
        filename = 'output' + str(c) + '.jpg'

        with open(filename, 'wb') as f:
            f.write(imgdata)
    print("success")


#Enter a prompt for the AI
prompt = ""
convert_jpg(prompt)

