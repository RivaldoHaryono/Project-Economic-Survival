import re

b64 = "iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAA81BMVEX7/P4AAAD////tGj36+vrAwMD9//36+vz39/fz8/NoaGjtGjv5+vrAwMD9//36+vz39/fz8/NoaGjtGjv"

c = open('index.html','r',encoding='utf-8').read()
old = "  // Foto QRIS demo (gambar contoh QRIS dari Wikipedia)\n  var QRIS_IMG = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/220px-QR_code_for_mobile_English_Wikipedia.svg.png';"
print("found:", old in c)
