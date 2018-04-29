if __name__ == "__main__":
    print("Content-type: text/html\n\n")
    fo = open("C:/Program Files/Apache Software Foundation/Tomcat 6.0/webapps/test/upl/Model1.py","r")
    f1 = open("model.py","w+")
    f1.write(fo.read())
    fo.close()
    f1.close()

    fo = open("C:/Program Files/Apache Software Foundation/Tomcat 6.0/webapps/test/upl/test_code.py","r")
    f1 = open("test_code.py","w+")
    f1.write(fo.read())
    fo.close()
    f1.close()