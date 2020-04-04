f=open("zhushou","r",encoding="utf8")
f_context = f.read()
f_context_list = f_context.split("\n")
f_context_list_len = len(f_context_list)
# print(f.read())
#查看多少行
# print(len(f.read().split("\n")))
qianzui = "new_udd."
houzui = "qs_one."
all_list = []
for i in f_context_list:
    if "edit" in i.lower():
        if "[" in i:
            end = i.split("|")[1]
            # print(end)
            # print(type(end))
            new_end = eval(end)    #将字符串类型转为列表类型
            print(new_end)
            # print(type(new_end))
            for j in new_end:
                all_list.append(j)

print(all_list)



    # if "edit" in str(f).lower:
    #     print(f)
#     gong = i.split(":")[0]
#
#     print("%s" % gong)
# a="ERdsd"
# print(a.lower())





