# Changelog

## 0.1.0 (2025-05-11)


### Features

* add 'all' target to Makefile for running tasks in order ([8d17afa](https://github.com/JonesH/mcp-reflect/commit/8d17afa124279f03a1536093ff610ed305f7fc6e))
* Add field validator to set focus_dimensions to None if empty ([5cd8e66](https://github.com/JonesH/mcp-reflect/commit/5cd8e66c0b474b51799ed80739bacd626daaca9f))
* add fix target to automatically resolve lint issues with ruff ([9030d3f](https://github.com/JonesH/mcp-reflect/commit/9030d3fc681c18c8af35039d0904d0ac6b6c4f6d))
* add poetry commands for linting, formatting, and type checking ([31dd868](https://github.com/JonesH/mcp-reflect/commit/31dd868df45f660944b1dd3882874a74ea2699cc))
* add return type annotation and docstring to set_focus_dimensions method ([7c879c6](https://github.com/JonesH/mcp-reflect/commit/7c879c64ad2dbf00c87d4a0d4d9004a98b3c6deb))
* add structured meta-reflection tools with storage, summary, and reset functionality ([5fee061](https://github.com/JonesH/mcp-reflect/commit/5fee061233d1c93b885363e7d9b51d26f6b86ee4))
* add UVX HTTP server support, update publish workflow, and enhance README with UV usage instructions ([5ebb0ab](https://github.com/JonesH/mcp-reflect/commit/5ebb0abf328d803be8a26759bca651cb5f5f0d31))
* **ci:** implementiere Trusted Publishing für TestPyPI-Workflow ([83c3e60](https://github.com/JonesH/mcp-reflect/commit/83c3e60b8ff7af18b55431744895bcd27582616f))
* **ci:** migriere PyPI-Release-Workflow zu Trusted Publishing ([d66e068](https://github.com/JonesH/mcp-reflect/commit/d66e06823cebddc11d737f089368dc816a4d431b))
* enforce non-empty response and change focus_dimensions default to None ([e2885f6](https://github.com/JonesH/mcp-reflect/commit/e2885f632eeff694ade829b5c1be920d474b58ab))
* Implementiere MCP-Reflect Tool mit FastMCP ([5996187](https://github.com/JonesH/mcp-reflect/commit/599618719f85e088cae6c2a8a383b3e0f8ff0953))


### Bug Fixes

* add [@classmethod](https://github.com/classmethod) decorator to resolve N805 lint error ([3a89c49](https://github.com/JonesH/mcp-reflect/commit/3a89c49dc073eefe6161441debfac50dc8dff227))
* Add default factory for focus_dimensions in ReflectionInput model ([ebe4839](https://github.com/JonesH/mcp-reflect/commit/ebe4839e073d85c399b651964d0bdc92a65c9ac5))
* add type annotation for `cls` in classmethod `set_focus_dimensions` ([e5769a8](https://github.com/JonesH/mcp-reflect/commit/e5769a81d6c3d726250a267dea0e08b27c1c2c30))
* **ci:** aktualisiere version-bump workflow für Trusted Publishing ([28c32e6](https://github.com/JonesH/mcp-reflect/commit/28c32e6688a95e4667bd646077006691a4c82167))
* **ci:** korrigiere YAML-Einrückungsfehler im Release-Please workflow ([cbbd2bc](https://github.com/JonesH/mcp-reflect/commit/cbbd2bcfcdcae7a78c13326ab802b13fc2849c45))
* **ci:** korrigiere YAML-Einrückungsfehler in PyPI-Release-Workflow ([10310a2](https://github.com/JonesH/mcp-reflect/commit/10310a2996175b4c1818a25d6783070daa7fd440))
* **ci:** wechsle zu Token-basierter Authentifizierung für offizielles PyPI ([8896421](https://github.com/JonesH/mcp-reflect/commit/88964213b9563b339b0ffc74bc6faf1954079c5c))
* correct structure of ruff configuration in pyproject.toml ([1723c68](https://github.com/JonesH/mcp-reflect/commit/1723c68932a68c457bcc96b7d1476e2e4f3c0ef2))
* **dependencies:** mache fastmcp zur optionalen Abhängigkeit für bessere Kompatibilität ([9a5309e](https://github.com/JonesH/mcp-reflect/commit/9a5309e49b160432be047d88058f7977206720f9))
* handle None type for focus_dimensions in ReflectionInput ([132b892](https://github.com/JonesH/mcp-reflect/commit/132b89251be14dfb3ee7497d3ab044193d490e27))
* resolve deprecation warnings by using Annotated for parameters ([4083401](https://github.com/JonesH/mcp-reflect/commit/40834016a9552dd6534acb69b9b1542ef63149ce))
* update focus_dimensions default to None for minimal input test pass ([f8aa8ef](https://github.com/JonesH/mcp-reflect/commit/f8aa8ef23a076e355b0395c2fcf8f24718cdd2b1))
* Update line lengths and linter settings in models and server files ([ca08f8e](https://github.com/JonesH/mcp-reflect/commit/ca08f8ec8e8a0d2d00d66ba54e93a5a902773cc6))
* Update ReflectionInput fields and add type annotations for mcp ([a6c6cce](https://github.com/JonesH/mcp-reflect/commit/a6c6cce8676a1c3f9f2fe5db97b60b3e3ff9706a))


### Documentation

* **install:** aktualisiere Installationsanweisungen für optionale Abhängigkeiten ([94df26a](https://github.com/JonesH/mcp-reflect/commit/94df26aed96522e6db0c288af49afdd380c1c357))
* **release:** füge Dokumentation zum Release-Prozess hinzu ([a281b3b](https://github.com/JonesH/mcp-reflect/commit/a281b3b44f3ecd2c3b872e3d0eee6d4ad20e491b))
