**Sprint 3 – Prototipagem Funcional e Integração**
Protótipo de precificação dinâmica para eletropostos, feito com um ESP32 em MicroPython e simulado no Wokwi.

A documentação completa, com o esquema de integração, a justificativa técnica, os resultados, as instruções de funcionamento e a conexão com a disciplina, está no PDF:

[**`docs/Documentacao\_Sprint3.pdf`**](docs/Documentacao_Sprint3.pdf)

**Simulação online:** https://wokwi.com/projects/475598428946468865

Estrutura do repositório
.
├──README.md
├── src/
│   ├── main.py            # lógica de leitura, cálculo do preço e controle das saídas
│   └── lcd\\\_i2c.py         # controle do display LCD por I2C
├── circuito/
│   ├── circuito\\\_wokwi.png # circuito montado no Wokwi
│   └── wokwi-project.txt  # link do projeto no Wokwi
└── docs/
    ├── Documentacao\\\_Sprint3.pdf   # documentação completa da Sprint 3
    ├── diagramas/
    │   ├── diagrama\\\_blocos.jpg    # entradas, ESP32 e saídas
    │   └── fluxograma.jpg         # fluxo do programa
    └── prints/                    # prints da simulação em cada cenário


