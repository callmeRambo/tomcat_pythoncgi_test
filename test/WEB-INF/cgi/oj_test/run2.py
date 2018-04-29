from test_code import test_code

if __name__ == "__main__":
    test = test_code()
    test_result = test.get_result()
    print(test_result)
    fo = open("result.txt", "w+")
    fo.write(str(test_result))
    fo.close()