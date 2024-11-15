def main():
   user_input = int(input("enter list of numbers"))
   num = [int(nums) for nums in str(user_input)]
   num.sort()

   print(num)
main()
