from django.db import models

# ==========================================
# 1. TABLA PARA RELACIÓN 1 A MUCHOS (ForeignKey)
# ==========================================
class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre


# ==========================================
# 2. TABLA PRINCIPAL (Conductor)
# ==========================================
class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    # Relación 1 a Muchos: Una Empresa tiene muchos Conductores
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='conductores')

    def __str__(self):
        return f"{self.nombre} - {self.documento}"


# ==========================================
# 3. RELACIÓN 1 A 1 (OneToOneField)
# ==========================================
class Licencia(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=10) # Ej: C1, C2
    # Un Conductor tiene UNA sola Licencia
    conductor = models.OneToOneField(Conductor, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Licencia {self.numero} ({self.categoria})"


# ==========================================
# 4. RELACIÓN MUCHOS A MUCHOS (ManyToManyField)
# ==========================================
class Ruta(models.Model):
    nombre = models.CharField(max_length=100) # Ej: Popayán - Silvia
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    # Muchos Conductores pueden cubrir Muchas Rutas
    conductores = models.ManyToManyField(Conductor, related_name='rutas')

    def __str__(self):
        return f"{self.nombre} ({self.origen} -> {self.destino})"