user_name = input('Как вас зовут? ')
while True:
    print('введите 1 чтобы увидеть текст чата или 2 чтобы отправить сообщение: ')
    response = input('введите 1 или 2:  ')
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('служебное сообщение: пока ничего нет\n')
    elif response == '2':
        new_message = input('введите сообщение: ')
        with open('chat.txt', 'a') as file:
            file.write('{name}: {message}\n'.format(name=user_name, message=new_message))
    else:
        print('неизвестная команда\n')
