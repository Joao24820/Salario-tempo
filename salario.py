print('SEJA BEM VINDO(A)')
nf = str(input('Informe o nome do funcionario(a): '))
sa = float(input('Informe o salario atua do funcionario(a) {}\nR$ '.format(nf)))
a = float(input('Informe quantos anos o senhor(a) tem de empresa: '))
m = int(input('Informe quantos meses voce trabalha na empresa: '))

if sa <= 500.00 and a < 1.0:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, (sa*0.25)+sa))
    print('O funcionario {}  não terá bonus '.format(nf))

elif sa <= 500.00 and a >= 1.0:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, ((sa*0.25)+sa) + 50.00))
    print('O funcionario {} terá um bonus de R$ 50.00 '.format(nf))

elif sa >= 500.01 < 1000.00:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, (sa*0.20)+sa))

elif sa >= 500.01 <= 1000.00 and a >= 1.1 < 3.0:
    print('O senhor(a) {} recebe um salario de R$ {} e pássara receber um salario de R$ {:.2f}'
          .format(nf, sa, ((sa*0.20)+sa) + 100.00))
    print('O funcionario {} terá um bonus de R$ 100.00 '.format(nf))

elif sa >= 1000.01 < 1500.00:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, (sa*0.15)+sa))

elif sa >= 1000.01 <= 1500.00 and a >= 4.0 < 6:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, ((sa*0.15)+sa)+200.00))
    print('O funcionario {} terá um bonus de R$ 200.00 '.format(nf))

elif sa >= 1500.01 < 2000.00:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, (sa*0.10)+sa))

elif sa >= 1500.01 < 2000.00 and a >= 7.00 < 10:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, ((sa*0.10)+sa) + 300.00))
    print('O funcionario {} terá um bonus de R$ 200.00 '.format(nf))

elif sa > 2000.0:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, sa))

elif sa > 2000.0 and a > 10:
    print('O senhor(a) {} recebe um salario de R$ {} e passará receber um salário de R$ {:.2f}'
          .format(nf, sa, (sa+500)))
    print('O funcionario {} terá um bonus de R$ 200.00 '.format(nf))
else:
    print('Opção Invalida !!')
