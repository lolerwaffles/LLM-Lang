**LLM-IR Language Design Goals**

1. **Token Efficiency**
   - Minimize the number of LLM tokens required to express complex logic.
   - Favor compact syntax over human readability.

2. **Logic Density**
   - Maximize the amount of executable logic per line.
   - Eliminate redundant syntax and boilerplate.

3. **Execution Efficiency**
   - Compile directly to LLVM IR for optimized performance.
   - Minimal runtime overhead.

4. **Memory Safety**
   - Rust-style ownership and borrowing model.
   - No nulls, dangling pointers, or data races.

5. **Concurrency**
   - First-class support for threads, message passing, and parallel execution.
   - Actor-style and shared-memory concurrency models supported.

6. **Interoperability**
   - Interop with C, C++, and Rust via FFI.
   - Can import LLVM-IR-compatible modules.

7. **Modular Architecture**
   - Functions and modules are first-class.
   - Module importing using single-token aliases.

8. **Determinism**
   - Deterministic evaluation unless explicitly declared nondeterministic.

9. **Debuggability**
   - Provide optional metadata for debugging.
   - Step-through support in interpreter mode.

10. **Multicore Awareness**
    - Built-in scheduler for distributing tasks across cores.
    - Support for CPU affinity and thread pools.

11. **Minimalist Syntax**
    - Inspired by APL/J: expression-based, array-first, tersely symbolic.

12. **Domain Extensibility**
    - Primitive extensions for arrays, tensors, bitstreams, and packed structs.

