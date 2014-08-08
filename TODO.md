* Abstract inner loop of `can_make_24` to check arbitrary prefix expressions
    * Currently, one loop per expression form is used, which does sufficiently
      exhaust the search space
    * Or does it?
    * Do we need to check expressions of the form: `op d op op d d d`?
        * We don't need to consider `+` and `*`, because they are commutative
        * Example `/ 2 / / 3 5 7`, infix `(2 / ((3 / 5) / 7))`, how else can this be written in prefix form?
            * It can be written as `(2 / (7 * (3/5))`, i.e. `/ 2 * 7 / 3 5`
            * So `op d / / d d d` can always be written as `op d * d / d d`
            * The first `op` can be any `op`
        * Example `/ 4 / - 3 5 7`, infix `(4 / ((3 - 5) / 7))`, how else can this be written in prefix form?
            * It can be written as `(4 * (7 / (3 - 5))`, i.e. `* 4 / 7 - 3 5`
            * So `/ d / - d d` can always be written as `* d / d - d d`
            * The first `/` had to be changed to `*`
        * Example `- 4 / - 3 5 7`, infix `(4 - ((3 - 5) / 7))`, how else can this be written in prefix form?
            * Could not find another way to write this expression using a different prefix form.
            * We may need to evaluate expressions of the form `op d op op d d d`
    * How many different infix forms are there with 4 digits and 3 binary operations?
        * ((a op b) op c) op d
        * (a op b) op (c op d)
        * (a op (b op c)) op d
        * a op ((b op c) op d)
        * a op (b op (c op d))
    * What are the prefix equivalents of these forms?
        * op op op a b c d
        * op op a b op c d
        * op op a op b c d
        * op a op op b c d
        * op a op a op c d
    * Do we need to evaluate all of these forms?

* Abstract `gen_ops_permutations` to generate permutations of arbitrary length
    * Currently, the implementation is sufficient as the game is played with
      exactly 4 numbers

* Add additional (single character) prefix operators:
    * exponentiate:   ^ x y
    * log base x:     g x y
    * modulation:     % x y
    * root base x:    \ x y

