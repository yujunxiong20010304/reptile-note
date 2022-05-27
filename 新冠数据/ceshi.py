from urllib import parse

star='数据分析'
#编码
star1=parse.quote(parse.quote(star))
print(star1)

#解码可以用这个
star2=parse.quote(parse.unquote(star1))
print(star2)
