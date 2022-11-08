f = open('Dictionary.txt', 'r')
content = f.read()
dic_to_list = content.split()


def search_index(item, _list1):
    if len(_list1) == 0:
        return
    else:
        n = len(_list1)
        mid = n // 2
        if _list1[mid] == item:
            return mid
        else:
            if item > _list1[mid]:
                search_index(item, _list1[mid + 1:])
            else:
                search_index(item, _list1[:mid])


def by(item, _list1):
    if len(_list1) == 0:
        return False
    else:
        n = len(_list1)
        mid = n // 2
        if _list1[mid] == item:
            return True
        else:
            if item > _list1[mid]:
                return by(item, _list1[mid + 1:])
            else:
                return by(item, _list1[:mid])


print(search_index('b', dic_to_list))
# ascii_ = "abcdefghijklmnopqrstuvwxvz"
# for i in ascii_:
#     index.append(search_index(i, dic_to_list))
#
# print(index)
# a = {
#
# }
#
# print(by("done", _list))
# # text = input("enter any text ")
# # _listOfText = text.split()
# # for word in _listOfText:
# #     if by(word, _list):
# #         print(word)
# #     else:
# #         print('error')
# # print(by(_listOfText[0], _list))
# # print(_list)
