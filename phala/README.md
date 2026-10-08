# Phala production packaging

This public fork owns Phala's vLLM Router packaging. The router implementation remains the official unmodified `vllm-router` 0.1.15 wheel from upstream tag `v0.1.15`, commit `1fbcde7443d75b36befb61bc081f64c2a1f13a4b`. The fork's current upstream main may be newer; it is not the source version selected by this recipe.

Build with `docker build -f phala/Dockerfile phala`. The [Dockerfile](Dockerfile) pins `vllm/vllm-openai:v0.31.0@sha256:c1c9f6fd5c109ba7f0546a59f5b2f15fb87f64c77782e90a27b648b42a8e67c3` and the upstream wheel SHA256 `2f268b001a546d7921c2e87b510869134a212f0ab2faf138b78eb554c93a2241`. [router_with_env.py](router_with_env.py) is the only Phala runtime customization: it passes the existing environment TOKEN into RouterArgs.api_key without putting it in process arguments or logs. No Rust router or vLLM engine patch is applied.

These two files were migrated byte-for-byte from `Phala-Network/phala-models-compose` commit `b4a1a8286698f7bd8690e9408398c4c554af417d`. That historical commit produced the accepted image `ghcr.io/phala-network/vllm-router:0.1.15-phala1@sha256:2b76af60c1e9af5497ead57c2de0e2cf061e497e85692adaa0add2ed0941b103`. This source migration does not rebuild the image, alter its provenance or restart a deployment. Future packaging changes belong here and require a new immutable source tag/Release and qualified image digest; production Compose only references the published component.

The vLLM inference engine is a separate component: its public upstream fork is [Phala-Network/vllm](https://github.com/Phala-Network/vllm), and the current deployment uses the official unmodified v0.31.0 image. Do not place engine patches or deployment Compose files in this router packaging directory.
