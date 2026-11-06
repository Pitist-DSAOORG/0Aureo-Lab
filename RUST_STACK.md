# 0Aureo Rust Stack — primera integración

## Componentes creados

- aureo-shared: DTO ApiStatus con Serde.
- aureo-backend: API Axum sobre Tokio.
- aureo-frontend: interfaz Leptos CSR para WebAssembly.
- index.html: entrada del frontend.

## API

GET /api/health

Respuesta:

{
  "service": "0Aureo Backend",
  "status": "ok",
  "version": "0.1.0"
}

## Compilación y pruebas nativas

    cargo fmt --all --check
    cargo test --workspace
    cargo check -p aureo-backend

## Compilación WebAssembly

    rustup target add wasm32-unknown-unknown
    cargo check -p aureo-frontend --target wasm32-unknown-unknown

## Ejecución backend

    cargo run -p aureo-backend

El servidor escucha en el puerto 3000.

## Límite actual

Esta primera integración no contiene todavía:
- Parser GGUF.
- Carga de tensores.
- Tokenizador.
- Transformer.
- RoPE, atención o KV-cache.
- Sampler.
- Coordinador ni ejecutor de agentes.
- Memoria persistente de agentes.

CORS permisivo está habilitado solo para desarrollo inicial.
No usar esta configuración directamente en producción.
