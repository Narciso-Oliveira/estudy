

class Solution:
     def removeElement(self, nums: list[int], val: int) -> int:
        i=0
        for j in range(len(nums)):
            if nums[j] != val:
                print(nums)
                print("posição j ",nums)
                nums[i]=nums[j]
                i+=1
        return i

solucion = Solution()

# Ejemplo de lista y valor a eliminar
mi_lista = [3, 2, 2, 3]
valor_a_eliminar = 3

# Llamar al método removeElement
nueva_longitud = solucion.removeElement(mi_lista, valor_a_eliminar)

# Imprimir la lista modificada y la nueva longitud
print("Resultado: ",mi_lista[:nueva_longitud])  # Imprime: [2, 2]
print(nueva_longitud) 
