# Pattern 2

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 2](https://takeuforward.org/practice/dsa/pattern-2)

## Hint
- Use nested `for` loops to control rows and columns.
- The outer loop (`i`) controls the rows.
- The inner loop (`j`) controls the columns.
- Use string multiplication (`"*" * n`) to repeat characters.
- Pay attention to indentation and loop execution order.

## My Approach
1. Used an outer loop to iterate through `n` rows.
2. Used an inner loop to iterate through `n` columns.
3. Incremented `j` using `j += 1`.
4. Used `j * "*"` to generate repeated stars.
5. Printed `i * "*"` after the inner loop to understand outer-loop behavior.
6. Experimented with `\n` and `end=""` to understand print formatting.

## Key Insight
- Nested loops: A loop inside another loop.
- Outer loop: Controls rows.
- Inner loop: Controls columns.
- `range(n)`: Generates numbers from `0` to `n-1`.
- `j += 1`: Increments the variable by 1.
- String repetition: `"*" * 3` produces `***`.
- `print()`: Prints output and adds a newline by default.
- `end=""`: Prevents automatic line breaks.
- Indentation: Determines the execution flow.
- `return`: Terminates function execution and returns a value.

**Important Observations:**
- `i` starts from 0, so `i * "*"` initially produces an empty string.
- `return i, j` is inside the outer loop, so the function terminates after the first outer-loop iteration.
- The inner loop completes all its iterations before the outer loop moves to the next iteration.

## Complexity
- **Time:** O(n²) – Both loops execute approximately n times.
- **Space:** O(n) – The repeated string can contain up to n characters; auxiliary variables use O(1) space.

## Edge Cases
- `n = 0`: Both loops are skipped.
- `n = 1`: Only one iteration occurs in each loop.
- `n = 2`: Useful for understanding nested-loop execution.
- `j = 0`: String repetition produces an empty string.
- `return` inside a loop: Terminates execution earlier than expected.
- Incorrect indentation: Can change the output significantly.

## My Experience

**note:** Date 31-10-2026 at morning i tried again and this time I did whole code by self. It is been while, when I though by mind not AI. SO, the code was written by self.