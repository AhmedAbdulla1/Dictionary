import difflib
# import colorsys

dictionary = open("dictionary.txt", "r")  # open the dictionary file
dic_to_list = dictionary.read().split()  # set the dictionary in list


def binary_search(item, _list=dic_to_list):
    """
    search for the word in dictionary
    :param item
    :param _list
    :return: true or false
    """
    # if len(_list) == 0:
    #     return False
    # else:
    #     n = len(_list)
    #     mid = n // 2
    #     if _list[mid] == item:
    #         return True
    #     else:
    #         if item < _list[mid]:
    #             binary_search(item, _list[:mid])
    #         else:
    #             binary_search(item, _list[mid+1:])

    # binary search with while lope
    first, last = 0, len(_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if _list[mid] == item:
            return True
        elif item > _list[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return False


def get_suggestions(_word):
    """
    search for the closest word
    :param _word:
    :return:
    """

    index = 0
    _max = 0

    for i in range(0, len(dic_to_list)):
        temp = difflib.SequenceMatcher(None, dic_to_list[i], _word)
        similar = temp.ratio()
        if similar > _max:
            _max = similar
            index = i
    return dic_to_list[index]




# try to change the color for output and underline
word = 'ahmed'
print("\033[38;5;231mType words to check its spelling: \033[Om")
print(f"\033([4;31m{word}\033[Qm", end=' ')
print("word", end=' '),
print("\n"),
#
# word = input("enter the word you want to check for: ")
# list_of_words=word.split()# start program here
# for item in list_of_words:
#     print(binary_search(item))
# else:
#     close = get_suggestions(word)
#     print("the closest word is" + close)

# import colorama
# file = open('dictionary.txt')
# content = file.read()
# dictionary_to_list = content.split()
#
#
# def search_index(item, _list1):
#     if len(_list1) == 0:
#         return
#     else:
#         n = len(_list1)
#         mid = n // 2
#         if _list1[mid] == item:
#             return mid
#         else:
#             if item > _list1[mid]:
#                 search_index(item, _list1[mid + 1:])
#             else:
#                 search_index(item, _list1[:mid])
#
#
# def by(item, _list1):
#     if len(_list1) == 0:
#         return False
#     else:
#         n = len(_list1)
#         mid = n // 2
#         if _list1[mid] == item:
#             return True
#         else:
#             if item > _list1[mid]:
#                 return by(item, _list1[mid + 1:])
#             else:
#                 return by(item, _list1[:mid])
#
#
# print(by('name', dictionary_to_list))
# for i in ascii_:
#     index.append(search_index(i, dictionary_to_list))
#
# print(index)
# a = {
#
# }
#
# print(by("done", _list))
# text = input("enter any text ")
# _listOfText = text.split()
# for word in _listOfText:
#     if by(word, _list):
#         print(word)
#     else:
#         print('error')
# print(by(_listOfText[0], _list))
# print(_list)


# from colorama import Fore
# print('This text is red')
# print('my name is ahmed')
# def underline(text):
# print("\u0332".join(text))


# underline("Hello reader!")
