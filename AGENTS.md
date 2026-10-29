# Native development

Run the prepared interpreter with `python scripts/setup_worktree.py` before
development. It checks Python 3.10+, Torch and NumPy without installing packages,
loading models or contacting ComfyUI. Use `python tests/run_tests.py` for isolated
CPU/static checks. See [README](README.md#development) for scope and limitations.

Operating guidance for native H3 composition is maintained in the shared
`comfyui` skill; use the shared-agent-skills owner for discovery and maintenance.
