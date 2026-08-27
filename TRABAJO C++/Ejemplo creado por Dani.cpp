#include <iostream>
#include <string>
using namespace std;

class CuentaBancaria {
private:
    string titular;
    double saldo;

public:
    
    CuentaBancaria(string _titular, double _saldoInicial) {
        titular = _titular;
        saldo = _saldoInicial;
    }

    void depositar(double monto) {
        if (monto > 0) saldo += monto;
    }
    void mostrarEstado() {
        cout << "Titular: " << titular << " | Saldo: $" << saldo << endl;
    }
};

int main() {
    CuentaBancaria cuenta1("Maria", 500.0);
    cuenta1.depositar(150.0);
    cuenta1.mostrarEstado();

    return 0;
}