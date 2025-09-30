from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, RFC, apellidos, nombres):
        self.RFC = RFC
        self.apellidos = apellidos
        self.nombres = nombres

    def mostrar_info(self):
        return f"{self.nombres} {self.apellidos}, RFC: {self.RFC}"

    @abstractmethod
    def ingresos(self):
        pass

    @abstractmethod
    def sueldo_neto(self):
        pass


class EmpleadoVendedor(Empleado):
    def __init__(self, RFC, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(RFC, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision

    def ingresos(self):
        return self.monto_vendido * self.tasa_comision

    def bonificacion(self):
        if self.monto_vendido < 1000:
            return 0
        elif self.monto_vendido <= 5000:
            return self.ingresos() * 0.05
        else:
            return self.ingresos() * 0.10

    def descuento(self):
        if self.ingresos() < 1000:
            return self.ingresos() * 0.11
        else:
            return self.ingresos() * 0.15

    def sueldo_neto(self):
        return self.ingresos() + self.bonificacion() - self.descuento()


class EmpleadoPermanente(Empleado):
    def __init__(self, RFC, apellidos, nombres, sueldo_base, num_seguro):
        super().__init__(RFC, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.num_seguro = num_seguro

    def ingresos(self):
        return self.sueldo_base

    def descuento(self):
        return self.sueldo_base * 0.11

    def sueldo_neto(self):
        return self.ingresos() - self.descuento()



vendedor = EmpleadoVendedor("SEGJ060531", "Segundo Esquivel", "Jazmín", 2000, 0.10)
permanente = EmpleadoPermanente("SEGJ060531", "Segundo Esquivel", "Jazmín", 3000, "SS123")

print(vendedor.mostrar_info(), "-> Neto:", vendedor.sueldo_neto())
print(permanente.mostrar_info(), "-> Neto:", permanente.sueldo_neto())
