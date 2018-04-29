from test_code import test_code

if __name__ == "__main__":
    test = test_code()
    test_result = test.get_result()
    print(test_result)
    fo = open("result.txt", "r")
    result1 = fo.read()
    if(result1 == "") or (int(test_result)>=int(result1)):
        print("larger!")
        fo = open("result.txt", "w")
        fo.write(str(test_result))
        fo.close()
        fo = open("model1.py", "r")
        fo2 = open("submit.py","w+")
        fo2.write(fo.read())
        fo.close()
        fo2.close()