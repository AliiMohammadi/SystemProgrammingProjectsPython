file = open('D:\\dog_breeds.txt')

try:
    print(file.readline())
finally:
    file.close()


