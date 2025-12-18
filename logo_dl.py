import requests
from pathlib import Path

out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

image_url = "https://4.bp.blogspot.com/-2-Ny23XgrF0/Ws69gszw2jI/AAAAAAABLdU/unbzWD_U8foWBwPKWQdGP1vEDoQoYjgZwCLcBGAs/s1600/top_banner.jpg"

imgdata = requests.get(image_url)

filename = image_url.split("/")[-1]
out_path = out_folder.joinpath(filename)

f = open(out_path, "wb")
f.write(imgdata.content)
f.close()