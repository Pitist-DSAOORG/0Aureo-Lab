use aureo_shared::ApiStatus;
use gloo_net::http::Request;
use leptos::prelude::*;

#[component]
pub fn App() -> impl IntoView {
    let (message, set_message) = signal("Backend sin consultar".to_string());
    let (details, set_details) = signal(String::new());

    let check_backend = move |_| {
        let set_message = set_message;
        let set_details = set_details;

        leptos::task::spawn_local(async move {
            set_message.set("Consultando backend...".to_string());

            let result = Request::get("/api/health").send().await;

            match result {
                Ok(response) if response.ok() => match response.json::<ApiStatus>().await {
                    Ok(status) => {
                        set_message.set(format!("Estado: {}", status.status));
                        set_details.set(format!("{} — versión {}", status.service, status.version));
                    }
                    Err(error) => {
                        set_message.set("Respuesta JSON inválida".to_string());
                        set_details.set(error.to_string());
                    }
                },
                Ok(response) => {
                    set_message.set(format!("HTTP {}", response.status()));
                    set_details.set("El backend respondió con error".to_string());
                }
                Err(error) => {
                    set_message.set("Backend no accesible".to_string());
                    set_details.set(error.to_string());
                }
            }
        });
    };

    view! {
        <main>
            <h1>"0Aureo"</h1>
            <p>"Frontend Leptos + WebAssembly"</p>
            <button on:click=check_backend>
                "Comprobar conexión con backend"
            </button>
            <p>{move || message.get()}</p>
            <p>{move || details.get()}</p>
        </main>
    }
}

#[cfg(target_arch = "wasm32")]
#[cfg(target_arch = "wasm32")]
#[wasm_bindgen::prelude::wasm_bindgen(start)]
pub fn start() {
    leptos::mount::mount_to_body(App);
}
