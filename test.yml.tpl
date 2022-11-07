hello:
  world: {{ hostname }}
  test: {{ load_balancer_hostname }}
  yaml_snippiet:
    {{ yaml_block | indent(4) }}
