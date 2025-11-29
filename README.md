# KBE: Simple configuration language

**KBE** is a lightweight, human-friendly configuration (like ini, json, toml) language for data structuring and configuration. It is designed to be highly readable, minimalistic, and easy to parse and generate. KBE is ideal for config files, data exchange between programs, and describing complex structures in a simple way.

## KBE Example

```kbe
title="Example"
version=1

# This is a comment

name="Ivan"
email='ivan@example.com'

enabled=True
lua=False
pi=3.14
```

## Main Features

- **Readable:** kbe focuses on human readability compared to traditional serialization languages.
- **Simple:** Minimal syntax, easy to edit manually.
- **Primitive Types:** Supports strings, numbers, booleans, floats.
- **No Excessive Brackets/Tags:** Cleaner than formats like XML or JSON.

## kbe vs Other Formats

| Format   | Syntax                  | Readability | Overhead         | Type Support                | Comments      | Parsing     |
|----------|-------------------------|-------------|------------------|-----------------------------|---------------|-------------|
| **KBE**  | Light, key=value | +++         | Low              | strings, numbers, booleans, floats | Yes          | Easy        |
| **TOML** | key=value, sections     | ++          | Low              | strings, numbers, bools, arrays, sections | Yes          | Easy        |
| **JSON** | Brackets {}, keys with ""| +           | Medium           | strings, numbers, bools, arrays, objects  | No           | Easy        |
| **XML**  | Tags <tag>...</tag>     | -           | High             | strings, numbers (rare), trees            | Yes          | Complex     |

- **KBE:** Even more minimal and human-readable than TOML; extremely simple for manual editing and automatic parsing.
- **TOML:** Shares the philosophy of simplicity, slightly more formalized.
- **JSON:** Widely used for web data exchange; requires strict use of quotes and braces, lacks comments.
- **XML:** Very powerful and flexible, supports attributes and nested trees, but verbose and complex for configs.

## Why Use kbe?

- **Maximum Conciseness:** Configure quickly without being distracted by complex syntax.
- **Open and Extensible:** Easy to implement in any programming language.
- **Perfect for settings, data structures, and information sharing.**
 
 ## Limitations

- Only supports flat key=value pairs
- No nested objects or arrays
- Comments must start with #

## Installation & Usage

#### Python

```bash
pip install kbe
```
```python
import kbe

name = kbe.get("example.kbe", "name")
print(name)

kbe.set("example.kbe", "name", "Python")

name = kbe.get("example.kbe", "name")
print(name)
```

---

**KBE** — "Structure simply, read easily!"
**Current Version** — KBE 1
