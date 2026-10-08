# Separate router image layer; do not rebuild/restart accepted engines to add routing.
ARG ROUTER_BASE_IMAGE=vllm/vllm-openai:v0.31.0@sha256:c1c9f6fd5c109ba7f0546a59f5b2f15fb87f64c77782e90a27b648b42a8e67c3
FROM ${ROUTER_BASE_IMAGE}
RUN uv pip freeze --system > /tmp/router-constraints.txt \
    && uv pip install --system --only-binary=:all: -c /tmp/router-constraints.txt \
      'https://files.pythonhosted.org/packages/fe/8f/ea7aced147c8c2e50271550765470bdb5d5342b4422fe1114aa76aa65584/vllm_router-0.1.15-cp38-abi3-manylinux_2_28_x86_64.whl#sha256=2f268b001a546d7921c2e87b510869134a212f0ab2faf138b78eb554c93a2241' \
    && python3 -c 'from vllm_router.router import Router; import importlib.metadata as m; assert m.version("vllm-router") == "0.1.15"' \
    && vllm-router --help >/dev/null \
    && rm /tmp/router-constraints.txt
COPY router_with_env.py /usr/local/bin/router_with_env.py
ENTRYPOINT ["python3", "/usr/local/bin/router_with_env.py"]
