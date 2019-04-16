
while True:
    try:
        tuna = int(input('What is your favorite number?\n'))
        print(18 / tuna)
        break
    except ValueError:
        print('Please make sure you enter a number')
    except ZeroDivisionError:
        print('Please enter a non-zero number')
    except:
        break
    finally:
        print('Loop complete.')  # Will print at each run


