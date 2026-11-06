use aureo_shared::ApiStatus;
use axum::{routing::get, Json, Router};
use tower_http::cors::CorsLayer;

async fn health() -> Json<ApiStatus> {
    Json(ApiStatus::operational())
}

fn app() -> Router {
    Router::new()
        .route("/api/health", get(health))
        // CORS permisivo solo para desarrollo inicial.
        .layer(CorsLayer::permissive())
}

#[tokio::main]
async fn main() {
    let address = "0.0.0.0:3000";

    let listener = tokio::net::TcpListener::bind(address)
        .await
        .expect("No se pudo abrir el puerto 3000");

    println!("0Aureo API escuchando en http://{address}");
    axum::serve(listener, app())
        .await
        .expect("Error del servidor Axum");
}

#[cfg(test)]
mod tests {
    use super::*;

    #[tokio::test]
    async fn health_returns_operational_status() {
        let Json(status) = health().await;
        assert_eq!(status.service, "0Aureo Backend");
        assert_eq!(status.status, "ok");
    }
}
