import random

xinglist = "王李张刘陈杨赵黄周吴徐孙胡朱高林何郭马罗梁宋郑谢韩唐冯于董萧程曹袁邓许傅沈曾彭吕苏卢蒋蔡贾丁魏薛叶阎余潘杜戴夏钟汪田任姜范方石姚谭廖"

minglist = "大学之道在明明德在亲民定定而后能静静而后能安安而后能虑虑而后能得物有本末事有终始知所先后欲其心欲其心者先诚其意欲诚其意者先致其知致知"


def name():
    for i in range(1):
        xing = random.choice(xinglist)
        ming = "".join(random.choice(minglist) for i in range(random.randint(1,2)))   
    return xing + ming
xingming = name()
print(xingming)

#def address():
    