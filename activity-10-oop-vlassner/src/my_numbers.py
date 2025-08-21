'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: A simple model to understand iterators
'''

class MyNumbers:

  def __init__(self):
    self.__a = 1

  #def __iter__(self):
  #  return self

  def __next__(self):
    if self.__a < 10:
      x = self.__a
      self.__a += 1
      return x
    raise StopIteration
  
  def __iter__(self):
    if self.__a < 10:
      yield self.__a
      self.__a += 2
      yield from iter(self)

  # yield pauses execution of program and pauses the function and continues from that place
  
# TODO demonstrate an iteration process using MyNumbers
  myNumbers = MyNumbers()
  for number in myNumbers:
    print(number)

  gen = iter(myNumbers)
  print(next(gen))
  print(next(gen))
  