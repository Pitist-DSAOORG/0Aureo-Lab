# 0Aureo — Arquitectura objetivo

Version: 1.0
Status: SPECIFICATION_ONLY
Implementation: NOT_IMPLEMENTED
Integration: NOT_INTEGRATED
Verification: NOT_VERIFIED

## 1. Principio de verdad

Definir una arquitectura no implica que exista su implementación.

Ningún componente puede declararse implementado, integrado u operativo
sin código fuente verificable y pruebas reproducibles.

## 2. Arquitectura objetivo

0Aureo
├── Frontend
│   ├── Leptos
│   └── WebAssembly
├── Backend
│   ├── Axum
│   └── Tokio
├── Shared
│   ├── Serde
│   └── DTO
├── AI Runtime
│   ├── GGUF parser
│   ├── Tensor loader
│   ├── Tokenizer
│   ├── Transformer
│   ├── RoPE
│   ├── Attention
│   ├── KV cache
│   ├── MLP
│   └── Sampler
├── Agent System
│   ├── Coordinator
│   ├── Task queue
│   ├── Bounded executor
│   ├── Persistent memory
│   └── Result verifier
└── Verification
    ├── Unit tests
    ├── Integration tests
    ├── Security tests
    ├── Reproducible benchmarks
    └── CI

## 3. Estados obligatorios

DESIGNED:
La especificación existe.

IMPLEMENTED:
Existe código fuente del componente y compila.

INTEGRATED:
El componente está conectado a los demás mediante interfaces
definidas y supera pruebas de integración.

VERIFIED:
Existen pruebas reproducibles, resultados y hashes de los artefactos.

BLOCKED:
No se cumplen los requisitos de la siguiente fase.

## 4. Registro inicial

Todos los componentes comienzan como DESIGNED.

Ningún componente se considera implementado por aparecer en este documento.

## 5. Contratos de integración

Frontend:
- Comunicación HTTP o WebSocket con backend.
- DTO compartidos y serialización validada.

Backend:
- API Axum.
- Ejecución asíncrona Tokio.
- Límites de concurrencia y recursos.

AI Runtime:
- Entrada GGUF validada.
- Comprobación de dimensiones y tipos.
- Gestión explícita de memoria.
- Inferencia reproducible.

Agent System:
- Cola de tareas.
- Concurrencia limitada.
- Memoria persistente con integridad.
- Verificación de resultados.

Verification:
- Tests unitarios.
- Tests de integración.
- Tests de seguridad.
- Benchmarks con entorno, versiones y SHA-256.
- CI con resultados conservados.

## 6. Criterios de aceptación

Un componente no puede pasar a IMPLEMENTED sin:
1. Código fuente identificable.
2. Compilación satisfactoria.
3. Tests propios.

No puede pasar a INTEGRATED sin:
1. Contrato de interfaz.
2. Conexión funcional.
3. Prueba de integración.

No puede pasar a VERIFIED sin:
1. Comandos reproducibles.
2. Resultado de ejecución.
3. Versiones del entorno.
4. Hashes de entradas y artefactos.
5. Registro de fallos.

## 7. Restricciones

- No declarar pruebas PASS sin ejecutarlas.
- No confundir compilación con corrección matemática.
- No confundir benchmarks de compilación con benchmarks de inferencia.
- No presentar agentes lógicos como procesos ejecutores reales.
- No presentar interfaces definidas como servicios operativos.
- No sustituir pruebas por documentación.

## 8. Estado inicial

La arquitectura completa permanece en SPECIFICATION_ONLY.

La implementación y la integración deben demostrarse por separado.
