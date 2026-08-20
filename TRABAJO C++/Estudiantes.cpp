#include <iostream>
using namespace std;

int main () {
    int n, aprobados = 0;
    double nota, suma = 0;
    cout << "Cantidad de estudiantes: ";
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Nota estudiante " << i<< ": ";
        cin >> nota;
        if (nota >= 70) {
            suma += nota;
            aprobados++;
        }
    }
    if (aprobados > 0) {
        cout << "promedio de aprobados: " << suma / aprobados <<
        
        endl;
    }else {
        cout << "No hubo estudiantes aprobados" << endl;

    }
    return 0;
}
