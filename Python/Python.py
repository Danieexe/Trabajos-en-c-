#Banco Popular

Cuentas_Bancarias = {
    "Cuenta_Ahorros": { 100101754: {"Nombre": "Juan Perez", "Saldo": 1500.75},
                         100101755: {"Nombre": "Maria Lopez", "Saldo": 2500.00},
                         100101756: {"Nombre": "Carlos Sanchez", "Saldo": 500.50} },
    "Cuenta_Corriente": { 200202854: {"Nombre": "Ana Torres", "Saldo": 3000.00},
                           200202855: {"Nombre": "Luis Ramirez", "Saldo": 1200.25},
                            200202856: {"Nombre": "Sofia Martinez", "Saldo": 800.00} }
    }   

if __name__ == "__main__":
    print("Bienvenido al Banco Popular")
    print("Cuentas de Ahorros:")
    for cuenta, datos in Cuentas_Bancarias["Cuenta_Ahorros"].items():
        print(f"Cuenta: {cuenta}, Nombre: {datos['Nombre']}, Saldo: ${datos['Saldo']:.2f}")
    
    print("\nCuentas Corrientes:")
    for cuenta, datos in Cuentas_Bancarias["Cuenta_Corriente"].items():
        print(f"Cuenta: {cuenta}, Nombre: {datos['Nombre']}, Saldo: ${datos['Saldo']:.2f}")