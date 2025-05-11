# CHANGELOG


## v0.1.0 (2025-05-11)

### Bug Fixes

- Add @classmethod decorator to resolve N805 lint error
  ([`3a89c49`](https://github.com/JonesH/mcp-reflect/commit/3a89c49dc073eefe6161441debfac50dc8dff227))

- Add default factory for focus_dimensions in ReflectionInput model
  ([`ebe4839`](https://github.com/JonesH/mcp-reflect/commit/ebe4839e073d85c399b651964d0bdc92a65c9ac5))

- Add type annotation for `cls` in classmethod `set_focus_dimensions`
  ([`e5769a8`](https://github.com/JonesH/mcp-reflect/commit/e5769a81d6c3d726250a267dea0e08b27c1c2c30))

- Correct structure of ruff configuration in pyproject.toml
  ([`1723c68`](https://github.com/JonesH/mcp-reflect/commit/1723c68932a68c457bcc96b7d1476e2e4f3c0ef2))

- Handle None type for focus_dimensions in ReflectionInput
  ([`132b892`](https://github.com/JonesH/mcp-reflect/commit/132b89251be14dfb3ee7497d3ab044193d490e27))

- Resolve deprecation warnings by using Annotated for parameters
  ([`4083401`](https://github.com/JonesH/mcp-reflect/commit/40834016a9552dd6534acb69b9b1542ef63149ce))

- Update focus_dimensions default to None for minimal input test pass
  ([`f8aa8ef`](https://github.com/JonesH/mcp-reflect/commit/f8aa8ef23a076e355b0395c2fcf8f24718cdd2b1))

- Update line lengths and linter settings in models and server files
  ([`ca08f8e`](https://github.com/JonesH/mcp-reflect/commit/ca08f8ec8e8a0d2d00d66ba54e93a5a902773cc6))

- Update ReflectionInput fields and add type annotations for mcp
  ([`a6c6cce`](https://github.com/JonesH/mcp-reflect/commit/a6c6cce8676a1c3f9f2fe5db97b60b3e3ff9706a))

- **ci**: Aktualisiere version-bump workflow für Trusted Publishing
  ([`28c32e6`](https://github.com/JonesH/mcp-reflect/commit/28c32e6688a95e4667bd646077006691a4c82167))

- **ci**: Konfiguriere Release-Please mit manifestbasiertem Ansatz
  ([`cfd6d4e`](https://github.com/JonesH/mcp-reflect/commit/cfd6d4ee0120ccdeca34c47c2443dddbc440dbee))

- **ci**: Korrigiere YAML-Einrückungsfehler im Release-Please workflow
  ([`cbbd2bc`](https://github.com/JonesH/mcp-reflect/commit/cbbd2bcfcdcae7a78c13326ab802b13fc2849c45))

- **ci**: Korrigiere YAML-Einrückungsfehler in PyPI-Release-Workflow
  ([`10310a2`](https://github.com/JonesH/mcp-reflect/commit/10310a2996175b4c1818a25d6783070daa7fd440))

- **ci**: Wechsle zu Token-basierter Authentifizierung für offizielles PyPI
  ([`8896421`](https://github.com/JonesH/mcp-reflect/commit/88964213b9563b339b0ffc74bc6faf1954079c5c))

- **dependencies**: Mache fastmcp zur optionalen Abhängigkeit für bessere Kompatibilität
  ([`9a5309e`](https://github.com/JonesH/mcp-reflect/commit/9a5309e49b160432be047d88058f7977206720f9))

### Build System

- Add Dockerfile and docker-compose.yml for containerized deployment
  ([`0b4049f`](https://github.com/JonesH/mcp-reflect/commit/0b4049f034149c752c8cf9f853b4f663e262e8cb))

### Chores

- Fix lint configuration in pyproject.toml
  ([`b68c781`](https://github.com/JonesH/mcp-reflect/commit/b68c781c81f58aeb17eb6d48d223d4d621bc57e1))

- Increase allowed line length from 88 to 120 in configuration files
  ([`26de420`](https://github.com/JonesH/mcp-reflect/commit/26de4204af2fffd1bcbcb0115c40aeb60646edcc))

- Remove CLI scripts from pyproject.toml and add Makefile for tasks
  ([`5d2b915`](https://github.com/JonesH/mcp-reflect/commit/5d2b9151a848bc609597c1d05baf73cde82ef11c))

- Remove line_length setting from isort configuration
  ([`a53ccdf`](https://github.com/JonesH/mcp-reflect/commit/a53ccdfc3d579618c30ec6e34fd0ab8e71079f3f))

- Remove MCP conformance workflow file
  ([`32e72bc`](https://github.com/JonesH/mcp-reflect/commit/32e72bc4ee10010e32d619f9c4f3a04cb1766c4d))

- Update dependencies and config for Python 3.13 compatibility
  ([`aa659e2`](https://github.com/JonesH/mcp-reflect/commit/aa659e2fc91c2dea094b614486e6432ceeaa3d3f))

- Update ruff configuration in pyproject.toml
  ([`c0523b2`](https://github.com/JonesH/mcp-reflect/commit/c0523b2b7d650aff219d9734db6dd18b4ba6c6be))

- Update ruff version and adjust formatting commands in Makefile
  ([`6d5b78c`](https://github.com/JonesH/mcp-reflect/commit/6d5b78ceac1a5def99bace9163d9aff0940d5f1f))

### Code Style

- Clean up formatting and update author info in pyproject.toml
  ([`8f98b2a`](https://github.com/JonesH/mcp-reflect/commit/8f98b2abaecd6fd9267a2e1ae732284e77d09ed1))

- Clean up imports, formatting, and docstrings; add poetry.lock; update .gitignore
  ([`d6fa508`](https://github.com/JonesH/mcp-reflect/commit/d6fa5084d93934293a6d19a1284e33858a21a2cc))

- Format set_focus_dimensions method for better readability
  ([`5c55dc4`](https://github.com/JonesH/mcp-reflect/commit/5c55dc412d0aa485c88c3321bba764db9c092f10))

### Continuous Integration

- Add GitHub workflow for TestPyPI auto deploy and update docs and dependencies
  ([`c3711cc`](https://github.com/JonesH/mcp-reflect/commit/c3711ccc34ad247baff4c1fb717a54dc91f3072a))

- Add GitHub workflows for manual and automated PyPI publishing
  ([`8fe26c1`](https://github.com/JonesH/mcp-reflect/commit/8fe26c1ed4b7c4987fe31d91c35282436ec53158))

- Add permissions for PyPI trusted publishing in workflows
  ([`bfeb56e`](https://github.com/JonesH/mcp-reflect/commit/bfeb56e457069011243485eadcf0787af9e5fdef))

- Refactor GitHub workflows for automated semantic-release and cleanup version-bump.yml
  ([`af1eb77`](https://github.com/JonesH/mcp-reflect/commit/af1eb779f594ee8316ce06b70a434324dd7a20ad))

- Replace old PyPI publish workflow with new validated release workflow
  ([`d7fa82d`](https://github.com/JonesH/mcp-reflect/commit/d7fa82db1b47b528b021c0ba585d70f9d8a21f94))

### Documentation

- **install**: Aktualisiere Installationsanweisungen für optionale Abhängigkeiten
  ([`94df26a`](https://github.com/JonesH/mcp-reflect/commit/94df26aed96522e6db0c288af49afdd380c1c357))

- **release**: Füge Dokumentation zum Release-Prozess hinzu
  ([`a281b3b`](https://github.com/JonesH/mcp-reflect/commit/a281b3b44f3ecd2c3b872e3d0eee6d4ad20e491b))

### Features

- Add 'all' target to Makefile for running tasks in order
  ([`8d17afa`](https://github.com/JonesH/mcp-reflect/commit/8d17afa124279f03a1536093ff610ed305f7fc6e))

- Add field validator to set focus_dimensions to None if empty
  ([`5cd8e66`](https://github.com/JonesH/mcp-reflect/commit/5cd8e66c0b474b51799ed80739bacd626daaca9f))

- Add fix target to automatically resolve lint issues with ruff
  ([`9030d3f`](https://github.com/JonesH/mcp-reflect/commit/9030d3fc681c18c8af35039d0904d0ac6b6c4f6d))

- Add poetry commands for linting, formatting, and type checking
  ([`31dd868`](https://github.com/JonesH/mcp-reflect/commit/31dd868df45f660944b1dd3882874a74ea2699cc))

- Add return type annotation and docstring to set_focus_dimensions method
  ([`7c879c6`](https://github.com/JonesH/mcp-reflect/commit/7c879c64ad2dbf00c87d4a0d4d9004a98b3c6deb))

- Add structured meta-reflection tools with storage, summary, and reset functionality
  ([`5fee061`](https://github.com/JonesH/mcp-reflect/commit/5fee061233d1c93b885363e7d9b51d26f6b86ee4))

- Add UVX HTTP server support, update publish workflow, and enhance README with UV usage
  instructions
  ([`5ebb0ab`](https://github.com/JonesH/mcp-reflect/commit/5ebb0abf328d803be8a26759bca651cb5f5f0d31))

- Enforce non-empty response and change focus_dimensions default to None
  ([`e2885f6`](https://github.com/JonesH/mcp-reflect/commit/e2885f632eeff694ade829b5c1be920d474b58ab))

- **ci**: Implementiere Trusted Publishing für TestPyPI-Workflow
  ([`83c3e60`](https://github.com/JonesH/mcp-reflect/commit/83c3e60b8ff7af18b55431744895bcd27582616f))

- **ci**: Migriere PyPI-Release-Workflow zu Trusted Publishing
  ([`d66e068`](https://github.com/JonesH/mcp-reflect/commit/d66e06823cebddc11d737f089368dc816a4d431b))

### Refactoring

- **ci**: Entferne redundanten manual-publish workflow
  ([`dcd8c66`](https://github.com/JonesH/mcp-reflect/commit/dcd8c66efcd6c751c9adf772a7d07a0d1912034b))

- **ci**: Optimiere Release-Please workflow mit besserer Struktur und Konfiguration
  ([`1ad2f85`](https://github.com/JonesH/mcp-reflect/commit/1ad2f856798f7fb4d58de2804b86d73af3b26df3))

### Testing

- Fix parsing errors and improve evaluation response handling
  ([`5831ec9`](https://github.com/JonesH/mcp-reflect/commit/5831ec93c88a3aefafdddb4f845a46a12e95ac30))


## v0.0.0 (2025-05-11)

### Features

- Implementiere MCP-Reflect Tool mit FastMCP
  ([`5996187`](https://github.com/JonesH/mcp-reflect/commit/599618719f85e088cae6c2a8a383b3e0f8ff0953))
