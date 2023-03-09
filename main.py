def devis(x):
    return x % 3 == 0
x=int(input('Введите число'))
print (devis(x))
def zad2():
    def delen(x):
        return 100 / x
    try:
        x = int(input('Введите число'))
        print(int(delen(x)))
    except ZeroDivisionError:
        print( 'На 0 делить нельзя!')
    except ValueError:
        print('Введите число, а не строку!')

def zad3():
    def mag(x):
        x = input('Введите дату')
        dat = x.split('.')
        return int(dat[0]) * int(dat[1]) == int(dat[2][2:4])
    print(mag(x))
def zad4():
    def ticket(x):
        sum1, sum2 = 0, 0
        x=input('Введите номер билета')
        ser= int(len(x)/2)
        for i in range (ser):
            sum1 += int(x[i])
        for i in range (ser, len(x)):
            sum2 += int(x[i])
        return sum1 == sum2
    print(ticket(x))
zad2()
zad3()
zad4()