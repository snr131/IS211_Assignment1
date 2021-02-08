
def listDivide(numbers,divide=2):
  even_nums = []
  for i in range(0,len(numbers)):
    if numbers[i] % divide == 0:
      even_nums.append(numbers[i])
  return len(even_nums)

class ListDivideException(Exception):
  pass 

def testListDivide():
    try:
        result =  listDivide([1,2,3,4,5], divide=2)
        if result == False:
            print(result)
            raise ListDivideException
    except:
        print("There is a ListDivideException")
    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30, 54, 63,98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5], 1) == 5
    
if __name__ == "__main__":
    testListDivide()
