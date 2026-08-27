#include <iostream>
#include <cmath>

using namespace std;

int main () {
    double a, b, c, x, y;
    cout << "Ingrese a, b, c, y, x separados por espacio:";
    cin >> a >> b >> c >> x;
    y = a * pow (x, 2) + b * x + c;
    cout << "El resultado de r es: " << y << endl;

    return 0;
}