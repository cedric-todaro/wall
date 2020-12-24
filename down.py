for i in range(1000):
    print("wget https://picsum.photos/1920/1080/?image=", i," -O image", str(i).zfill(3),".jpg",sep="")
    print("ping 127.0.0.1 -n 2 >NUL")
