#  Importación de clases
from modelos.producto import Producto 
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante ("Restaurante la Monica")

# Creación de productos 
producto1 = Producto("Encebollado:", 3.50, "Comida")
producto2 = Producto("Bolones de verde", 2.50, "Comida")
producto3 = Producto("Jugo de Piña", 2.00, "Bebida")

# Creación de Clientes
cliente1 = Cliente("Ana Lopez", "0984532156")
cliente2 = Cliente("Alex Pérez", "0987432597")

# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostar información resgistrada
print("=== SISTEMA DE GESTIÓN DEL RESTAURANTE ===")
print(f"Nombre del restaurante: {restaurante.nombre}")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()