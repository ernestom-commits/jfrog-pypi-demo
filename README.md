# JFrog PyPI Demo — Catalog API

A minimal Python Flask service used to demonstrate JFrog Platform capabilities for the Python/PyPI ecosystem.

## What this demonstrates

| JFrog Capability | How |
|-----------------|-----|
| PyPI via Artifactory | `pip install` routes through `demo-pypi` virtual — Curation evaluated at download |
| Xray CVE scan | `Pillow==9.0.0` (CVE-2022-22817), `PyYAML==5.4.1` (CVE-2020-14343) detected |
| Build info | `jf pip install` publishes full dependency graph to Artifactory |
| FrogBot | PR scan comments with CVE findings + fix versions |

## CVEs in this demo

Packages are pinned below CVSS 8.0 so Curation allows download; Xray still flags them.

| Package | Version | CVE | CVSS | Finding |
|---------|---------|-----|------|---------|
| Werkzeug | 2.2.2 | CVE-2023-25577 | 7.5 High | Multipart form-data parser DoS via large boundaries |
| requests | 2.27.1 | CVE-2023-32681 | 6.1 Medium | Proxy-Authorization header leak on redirect |
| urllib3 | 1.26.6 | CVE-2023-43804 | 5.9 Medium | Cookie header leaked on cross-host redirect |

## Quick start (local)

```bash
# Configure pip to use Artifactory
jf pip-config --repo-resolve demo-pypi

# Install (all downloads tracked, Curation evaluated)
jf pip install -r requirements.txt

# Start
python src/app.py
curl http://localhost:5000/health
```

## Demo script

See `03-runbooks/runbook-02-security-xray.md` for the Xray demo using this app.
