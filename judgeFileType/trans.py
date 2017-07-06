#encoding=utf-8

content="ab广东松炀再生资源股份有限"
print content
content=content.decode("utf8").encode("gb2312")#写入的文件编码格式为utf-8
print content
with open("gb2312.txt","w") as f:
    f.write(content)

print ""


content="abc广东松炀再生资源股份有限"
print content
#content=content.encode("utf8")#写入的文件编码格式为utf-8
print content
with open("utf8.txt","w") as f:
    f.write(content)



content="abc广东松炀再生资源股份有限"
print content
content=content.decode("utf8")#写入的文件编码格式为utf-8
print content
with open("unicode.txt","w") as f:
    f.write(content)

print ""
