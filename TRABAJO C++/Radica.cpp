#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x, radicando;
    cout << "Ingrese el valor de x: ";
    cin >> x;
    radicando = pow(x, 3) - 4;
    if (radicando >= 0) {
        cout << "f(x) = " << sqrt(radicando) << endl;
    } else {
        cout << "Error: Resultado fuera del dominio real." << endl;
    }
    return 0;
}

