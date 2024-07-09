def loginUsuario(perfil):
    match str.lower(perfil):
        case 'administrador' | 'admin':
            print('Bem-vindo, Administrador')
        case _:
            print('Bem-vindo, Usuário')

for perfil in ['Admin', 'admin', 'User', 'usuário', 'etc']:
    loginUsuario(perfil)
