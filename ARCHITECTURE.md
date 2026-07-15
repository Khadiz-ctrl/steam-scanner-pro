# Steam Scanner Pro - Architecture

## Objetivo

Steam Scanner Pro es una herramienta para analizar oportunidades de compra de skins utilizando información histórica del mercado.

El proyecto está diseñado priorizando:

- Simplicidad
- Mantenibilidad
- Escalabilidad

Antes que la cantidad de funcionalidades.

---

# Arquitectura

El proyecto está dividido en módulos con responsabilidades bien definidas.

```
Provider
      │
      ▼
Repository
      │
      ▼
Analyzer
      │
      ▼
Scorer
      │
      ▼
Recommendation
      │
      ▼
ConsoleUI
```

---

# Responsabilidades

## Provider

Obtiene información del mercado.

No conoce la base de datos.

No calcula estadísticas.

---

## Repository

Accede a SQLite.

Es la única capa que conoce cómo se almacenan los datos.

---

## Analyzer

Coordina todo el proceso de análisis.

No implementa reglas de negocio.

Orquesta el flujo entre las demás clases.

---

## Statistics

Realiza cálculos matemáticos.

No conoce skins.

No conoce recomendaciones.

---

## MovingAverage

Calcula la media móvil.

No contiene otra lógica.

---

## Scorer

Calcula el Opportunity Score.

No consulta la base de datos.

No imprime información.

---

## Recommendation

Transforma un score en una recomendación.

Ejemplo:

BUY

WATCH

SKIP

---

## ConsoleUI

Solo muestra información.

Nunca calcula datos.

Nunca modifica análisis.

---

# Principios

El proyecto intenta seguir los siguientes principios.

## Single Responsibility Principle

Cada clase tiene un único motivo para cambiar.

---

## Separation of Concerns

Cada módulo tiene una responsabilidad específica.

---

## Clean Code

Los métodos públicos deben expresar intención.

Los detalles deben vivir en métodos privados.

---

## Repository Pattern

Toda comunicación con la base de datos pasa por PriceRepository.

---

# Roadmap

## v0.2

Arquitectura estable.

## v0.3

Tests.

## v0.4

SkinAnalysis.

## v0.5

PriceRecord.

## v1.0

Primera versión estable.