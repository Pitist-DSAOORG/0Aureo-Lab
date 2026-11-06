import Mathlib

namespace Aureo.Regression

theorem add_zero_right (n : Nat) : n + 0 = n := by
  simp

theorem zero_add_left (n : Nat) : 0 + n = n := by
  simp

theorem add_assoc_test (a b c : Nat) :
    (a + b) + c = a + (b + c) := by
  exact Nat.add_assoc a b c

theorem add_comm_test (a b : Nat) :
    a + b = b + a := by
  exact Nat.add_comm a b

theorem mul_zero_right (n : Nat) : n * 0 = 0 := by
  simp

theorem mul_one_right (n : Nat) : n * 1 = n := by
  simp

theorem zero_mul_left (n : Nat) : 0 * n = 0 := by
  simp

end Aureo.Regression
