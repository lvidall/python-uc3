from conta import ContaCorrente

contas = {
    '123':ContaCorrente('Luis', '123', 'deb123', 100.0),
    '456':ContaCorrente('Monique', '456', 'nik123', 5000.0)
}

#login

ContaCorrente.mostrar_saldo(contas['123'])