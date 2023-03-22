# import atexit

index=1
least = [None,0]
answers = []

while 1:
    squares = [int(n)**int(n) for n in str(index)]
    sums = sum(squares)
    # print(index, squares, sum(squares))
    
    diff = abs(sums-index)
    
    if diff == 0:
        answers.append(index)
        print(f"NEW MATCH = {index}\n{answers}")
        # break
    elif diff<=2:
        print("Small diff!!!", index, sums, diff)
        # print(index, sums, diff)
    index+=1
        
# def goodbye():
#     print(answers)

# atexit.register(goodbye)
# uhh()

