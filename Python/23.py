def count_substring(string, sub_string):
    find = string.find(sub_string, 0, len(string))
    if (find == -1):
        return 0
    dem = 0
    while find != -1:
        dem = dem + 1
        string = string[:find] + string[find + 1:]
        print (string)
        find = string.find(sub_string, 0, len(string))
    return dem


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
