class empleado :
    #aqui va el codigo del empleado 
    nombre = " " 
    apellido = " "
    """ 
    #1 = Masculino y 2 = Femenino 
    """
    sexo = " "
    salario = 0 

    def CambiarSalario(self, nuevoSalario) :
        # Aqui va el codigo 
        return 0 
    

    def CambiarEmpleado(self, nNombre, nApellido, nsexo, nsalario) :
        # Aqui va el codigo 
        return None 
    
    def ConsultarSalario(self): 
        # Aqui va el codigo
        return self.salario 
    
    def ConsultarNombre(self):
        # Aqui va el codigo 
        return self.nombre 
    
    def ConsultarApellido(self):
        # Aqui va el codigo 
        return self.apellido 
    
    def ConsultarNombreCompleto(self, Nombre, Apellido) :
        # Aqui va el codigo 
        return self.nombre + " " + self.apellido 
    
    def AumentoSalarial(self):
        nSalario = self.salario * 0.05
        nSalario = nSalario + self.salario 
        self.salario = nSalario

        return "El nuevo salario es de : " + self.salario 
