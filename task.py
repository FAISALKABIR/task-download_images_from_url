####################################################
# Coded by Faisal Kabir                           #
# All right reserved to the respective owner     #
#################################################


# downloading images from text file
path_text = "url.txt"

o = open(path_text,"r")
ur = o.read()
o.close()

# list, containing downloaded files 
urls = ur.split()
print("The number of urls: {}".format(len(urls)))
print("____________________________")
for url in urls:
    print(url)
    
    
# download the images from each of the URL     
import requests,os

loc_data = "./data/"
try:
    os.makedirs(loc_data)
except:
    pass
iimage = 0
for url in urls:
    try:
        f = open(loc_data + 'image{:05.0f}.jpg'.format(iimage),'wb')
        f.write(requests.get(url).content)
        f.close()
        iimage += 1
    except Exception as e:
        print("\n{} {}".format(e,url))
        pass

