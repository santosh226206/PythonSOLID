from ConcreteSavingAccount import ConcreteSavingAccount

if __name__ == '__main__':

    a = ConcreteSavingAccount()
    try:
        a.deposit(100)
        a.withdraw(200)

    except Exception as e:
        print(e)

    print(a)