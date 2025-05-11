# Release-Prozess für MCP-Reflect

Diese Dokumentation beschreibt den Prozess zur Veröffentlichung von MCP-Reflect auf PyPI.

## Voraussetzungen

1. **PyPI-Konto** - Für offizielle Releases
2. **TestPyPI-Konto** - Für Testveröffentlichungen
3. **GitHub-Repository-Zugriff** - Mit Schreibberechtigung

## TestPyPI-Veröffentlichungen (Entwicklungsversionen)

Entwicklungsversionen werden automatisch auf TestPyPI veröffentlicht, wenn:
- Änderungen an den Hauptquellcode-Dateien (`mcp_reflect/**`) oder `pyproject.toml` gepusht werden
- Der Workflow manuell über die GitHub-Oberfläche ausgelöst wird

### Manueller TestPyPI-Release

1. Navigiere zu GitHub Actions → "TestPyPI Auto Deploy"
2. Klicke auf "Run workflow"
3. (Optional) Gib ein benutzerdefiniertes Versionssuffix ein
4. Klicke auf "Run workflow"

### Installation einer TestPyPI-Version

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ mcp-reflect
```

## Offizielle PyPI-Veröffentlichungen

Für offizielle Releases gibt es zwei Methoden:

### Methode 1: GitHub Release

1. Navigiere zum Repository → "Releases" → "Create a new release"
2. Wähle das Tag (z.B. `v0.1.0`) und gib einen Titel ein
3. Klicke auf "Publish release"
4. Der PyPI-Release-Workflow wird automatisch ausgelöst

### Methode 2: Manueller Release

1. Navigiere zu GitHub Actions → "PyPI Official Release"
2. Klicke auf "Run workflow"
3. Gib die Version ein (z.B. `0.1.0`)
4. Schreibe "YES" zur Bestätigung
5. Klicke auf "Run workflow"

Diese Methode:
- Aktualisiert die Version in `pyproject.toml`
- Erstellt einen Git-Tag
- Veröffentlicht auf PyPI
- Erstellt einen GitHub Release

## PyPI Trusted Publishing Konfiguration

MCP-Reflect verwendet PyPI's Trusted Publishing für sichere Veröffentlichungen ohne API-Tokens:

1. Navigiere zu https://pypi.org → Account → Publishing
2. Klicke auf "Add new publisher"
3. Wähle "GitHub Actions"
4. Repository: `JonesH/mcp-reflect`
5. Workflow-Name: `pypi-release.yml`
6. Environment: Leer lassen oder "None" wählen

Die gleiche Konfiguration sollte auch für TestPyPI erfolgen.

## Versionierungsstrategie

MCP-Reflect folgt SemVer:

- **MAJOR** - Inkompatible API-Änderungen
- **MINOR** - Neue Funktionalität (rückwärtskompatibel)
- **PATCH** - Bugfixes und kleinere Änderungen

Entwicklungsversionen folgen dem Schema `X.Y.Z.devYYYYMMDDHHMMSS`.

## Checkliste für Releases

- [ ] Alle Tests bestehen
- [ ] Dokumentation aktualisiert
- [ ] CHANGELOG.md aktualisiert (falls vorhanden)
- [ ] Version in `pyproject.toml` überprüft
- [ ] FastMCP-Abhängigkeit geprüft
