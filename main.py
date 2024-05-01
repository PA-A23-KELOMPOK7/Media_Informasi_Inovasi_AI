from View import auth_view
import os

if __name__ == '__main__':
    os.system('cls')
    main = auth_view.AuthView()
    main.view()
