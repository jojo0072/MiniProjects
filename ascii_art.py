from PIL import Image

img=Image.open(r"D:\Daniel Rabe\Downloads\mrbean.png").convert("L")
img=img.resize((40, int(40*img.size[1]/img.size[0])))
w, h=img.size
ascii_chars="@%#*+=-:. "
print(w, h)
with open ("art.txt", "w") as f:
    for c in range(1, h):
        for r in range(1, w):
            try:
                f.write(ascii_chars[img.getpixel((r, c))//25])   
            except:
                f.write(" ")               
        f.write("\n")    
with open(r"C:\Users\Daniel Rabe\art.txt", "r") as g:
    print(g.read())