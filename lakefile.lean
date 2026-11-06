import Lake
open Lake DSL

package «aureo-9-9» where
  leanOptions := #[
    ⟨`autoImplicit, false⟩
  ]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.33.1"

lean_lib Aureo
