

# Summary


<!-- 
# Introduction 
This chapter is about introducing what Cranelift IR is.
Like `index.md` from the docs in the `cranelift` folder of the `wasmtime` repository.
Construction is not worried about until chapter 1, when you're somewhat familiar with the IR.
This chapter will be somewhat bulky as it needs to convey relevant information.

# What is Cranelift?
This sub-chapter tells the user what Cranelift is and gives an example of it's IR, with an input & output.

# Functions, Basic Blocks, and SSA
This talks about how Cranelift has functions, basic blocks, and is single-static assignment.
This comes before code generation so the user has an idea of what the output of their code will be.
It also mentions you can use libc - this will be VERY important in later chapters, so don't forget.
# Sample Program
Shows a simple program in IR form.
-->

- [Introduction](./introduction/index.md) 
    - [What is Cranelift?](./introduction/what_is_cranelift.md)
    - [Functions, Basic Blocks, and SSA](./introduction/fbbssa.md)
    - [Sample Program](./introduction/sample_program.md)

<!--
# Cranelift Codegen
This chapter talks about how to get started generating Cranelift IR.

# Constructing ISAs
This talks about constructing:
- Flags
- ISA

```
let mut flag_builder = settings::builder();
flag_builder.set("use_colocated_libcalls", "false").unwrap();
flag_builder.set("is_pic", "false").unwrap();
let isa_builder = cranelift_native::builder().unwrap_or_else(|msg| {
    panic!("host machine is not supported: {}", msg);
});
let isa = isa_builder
    .finish(settings::Flags::new(flag_builder))
    .unwrap();
```
This code from the demo will be familiar by the end of this section.

# Modules
This introduces Modules - whether it be object modules or JIT modules.
It will focus on both module types equally.
It introduces these types:
- JITModule
- ObjectModule

# Constructing Functions & Basic Blocks
This chapter introduces these types:
- Function
- FunctionBuilder
- Context
- BasicBlock
- Probably some more akin to these.

-->

- [Chapter 1 - Cranelift Codegen](./chapter1/index.md)
    - [Constructing ISAs](./chapter1/constructing_isas.md)
    - [Modules](./chapter1/modules.md)
    - [Constructing Functions & Basic Blocks](./chapter1/cfbb.md)

<!--
# Basic Instructions
This chapter will introduce basic instructions.
- Arithmetic
- Function & Block Parameters
- Calling functions & switching blocks
- Returning

TODO: document specifics of other chapters
-->
- [Chapter 2 - Essential Instructions](./chapter2/index.md)
    - [Arithmetic](./chapter2/arithmetic.md)
    - [Parameters](./chapter2/parameters.md)
    - [Calling Functions & Basic Blocks](./chapter2/cfbb.md)
    - [Returning Values](./chapter2/returning.md)
    - [libc](./chapter2/libc.md)

- [Chapter 3 - Variable Manipulation](./chapter3/index.md)
    - [Declaring Variables](./chapter3/declaring.md)
    - [Setting & Getting Variables](./chapter3/setting_and_getting.md)
    - [Global Values](./chapter3/global_values.md)

- [Chapter 4 - Memory Manipulation](./chapter4/index.md)
    - [The Stack vs The Heap](./chapter4/stack_vs_heap.md)
    - [Manipulating the Stack](./chapter4/manipulating_stack.md)
    - [Manipulating the Heap](./chapter4/manipulating_heap.md)