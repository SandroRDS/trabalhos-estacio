from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa('João', '1239819238', '2003-05-21', False)
pessoa.mostrarDados()

pessoaFisica = PessoaFisica('João', '1239819238', '2003-05-21', False, '1980-03-21', '000.111.222-33', '123654789-0')
pessoaFisica.mostrarDados()

pessoaJuridica = PessoaJuridica('João', '1239819238', '2003-05-21', False, '2010-03-01', '32.324.356/0001-09')
pessoaJuridica.mostrarDados()

pessoa.nome = 'Maria'
pessoa.numeroConta = '8192381239'
pessoa.dataAberturaConta = '2005-06-11'
pessoa.status = True
pessoa.mostrarDados()

pessoaFisica.nome = 'Maria'
pessoaFisica.numeroConta = '8192381239'
pessoaFisica.dataAberturaConta = '2005-06-11'
pessoaFisica.status = True
pessoaFisica.dataNascimento = '2002-06-07'
pessoaFisica.cpf = '819.937.483-23'
pessoaFisica.rg = '18274637-9'
pessoaFisica.mostrarDados()

pessoaJuridica.nome = 'Maria'
pessoaJuridica.numeroConta = '8192381239'
pessoaJuridica.dataAberturaConta = '2005-06-11'
pessoaJuridica.status = True
pessoaJuridica.dataAberturaEmpresa = '2002-06-07'
pessoaJuridica.cnpj = '12.335.243/2001-00'
pessoaJuridica.mostrarDados()

