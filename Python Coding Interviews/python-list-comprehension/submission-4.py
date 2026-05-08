from typing import List


def create_list_of_odds(n: int) -> List[int]:
    my_list = [i for i in range(1, n + 1)]
    #result = [i for i in my_list if i % 2 != 0] -- using list comprehension 

    result = []
    for i in range(len(my_list)): # using for loop 
        if(my_list[i] % 2 != 0):
            result.append(my_list[i])
        
    return result




# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
