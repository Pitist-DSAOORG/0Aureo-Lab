use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ApiStatus {
    pub service: String,
    pub status: String,
    pub version: String,
}

impl ApiStatus {
    pub fn operational() -> Self {
        Self {
            service: "0Aureo Backend".to_string(),
            status: "ok".to_string(),
            version: env!("CARGO_PKG_VERSION").to_string(),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn status_json_roundtrip() {
        let original = ApiStatus::operational();
        let json = serde_json::to_string(&original).unwrap();
        let decoded: ApiStatus = serde_json::from_str(&json).unwrap();
        assert_eq!(original, decoded);
    }

    #[test]
    fn status_has_expected_values() {
        let status = ApiStatus::operational();
        assert_eq!(status.service, "0Aureo Backend");
        assert_eq!(status.status, "ok");
    }
}
