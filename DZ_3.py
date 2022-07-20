while True:
  num1 = float(input('Введіть перше число: '))
  num2 = float(input('Введіть друге число: '))
  operation = input('Що зробити? (+, -, /, *, %, **): ')

  if operation == '+':
    r = num1 + num2
    print(f'{num1} + {num2} = {r}')
    p = input('Продовжити? y - так. n - ні: ')

    if p == 'n':
      break

    elif p == 'y':
      print('Продовжуемо...')

    else:
      print('Відповіді не існуе (продовжуемо...)')

  elif operation == '-':
    r = num1 - num2
    print(f'{num1} - {num2} = {r}')
    p = input('Продовжити? y - так. n - ні: ')

    if p == 'n':
      break

    elif p == 'y':
      print('Продовжуемо...')

    else:
      print('Відповіді не існуе (продовжуемо...)')

  elif operation == '/':
    r = num1 / num2
    print(f'{num1} / {num2} = {r}')
    p = input('Продовжити? y - так. n - ні: ')

    if p == 'n':
      break

    elif p == 'y':
      print('Продовжуемо...')

    else:
      print('Відповіді не існуе (продовжуемо...)')

  elif operation == '*':
    r = num1 * num2
    print(f'{num1} * {num2} = {r}')
    p = input('Продовжити? y - так. n - ні: ')

    if p == 'n':
      break

    elif p == 'y':
      print('Продовжуемо...')

    else:
      print('Відповіді не існуе (продовжуемо...)')

  elif operation == '**':
    r = num1 ** num2
    print(f'{num1} ** {num2} = {r}')
    p = input('Продовжити? y - так. n - ні: ')

    if p == 'n':
      break

    elif p == 'y':
      print('Продовжуемо...')

    else:
      print('Відповіді не існуе (продовжуемо...)')

  else:
    print('Данної операції не існуе!')
    p = input('Продовжити? y - так. n - ні: ')

    if p == 'n':
      break

    elif p == 'y':
      print('Продовжуемо...')

    else:
      print('Відповіді не існуе (продовжуемо...)')