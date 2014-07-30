* Abstract inner loop of `can_make_24` to check arbitrary prefix expressions
    * Currently, one loop per expression form is used, which does sufficiently
      exhaust the search space

* Abstract `gen_ops_permutations` to generate permutations of arbitrary length
    * Currently, the implementation is sufficient as the game is played with
      exactly 4 numbers

* Add additional (single character) prefix operators:
    * exponentiate:   ^ x y
    * log base x:     g x y
    * modulation:     % x y
    * root base x:    \ x y

