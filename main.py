stock_prices = [298, 305, 320, 301, 292]

print(stock_prices[0])

print(stock_prices[2])

##### Exercice ##### => https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

expenses = [2200, 2350, 2600, 2130, 2190]

#Q1
print(expenses[1] - expenses[0])

#Q2
x = 0 
for i in range(3):  ### u can do this simply => expenses[0] + expenses[1] + expenses[2]
    x += expenses[i] 
print(x)



#Q3
for i in expenses: ### u can do this simply => 2000 in expenses
    if i == 2000:
        print('yes u spent exactly 2000')

#Q4
expenses.append(1980)
print(expenses)

#Q5
expenses[3] -= 200
print(expenses)



heros = ['spider man','thor','hulk','iron man','captain america']

#Q1 
print(len(heros))

#Q2
heros.append('black panther')
print(heros)

#Q3
heros.pop()
heros.insert(3, 'black panther')
print(heros)

#Q4
heros[1:3] = ["doctor strange"]
print(heros)

#Q5
x = sorted(heros)  ### u can simply use .sort() => heros.sort()
print(x)


myList = []
def myFun():
    x = int(input('give me a number plz : '))
    for i in range(x + 1):
        if i % 2 != 0 :
            myList.append(i)

    print(myList)
myFun()