def main():
    intList = []
    while(True):
      number = int(input())
      if(number==0):
        break
      intList.append(number)
    print(intList[0])

if __name__ == '__main__':
    main()
