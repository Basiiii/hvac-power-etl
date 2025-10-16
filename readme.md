# TP01 – Integração e Análise de Dados HVAC

**Autor:** Enrique George Rodrigues  
**Número de Aluno:** 28602  

---

## Estrutura do Repositório

O projeto segue a seguinte organização de pastas:

```
tp01-28602/
├── README.md
├── doc/
│   └── 28602_doc.pdf                       # Relatório final do TP01
├── dataint/                                # Transformações e jobs Pentaho (Kettle)
│   ├── jobs/
│   │   └── etl_hvac_power.kjb              # Job principal
│   ├── transformations/
│   │   └── etl_climate_analysis.ktr        # Transformação de ETL
│   └── node-red-flow.json                  # Ficheiro Node-RED
├── data/
│   ├── input/                              # Ficheiros de dados de entrada
│   │   ├── outdoor_data.json
│   │   └── sensor_data.csv
│   └── output/                             # Ficheiros de saída gerados pelo ETL e Python
│       ├── hvac_data.db
│       ├── power_efficiency.csv
│       └── power_efficiency.xml
└── src/                                    # Código Python utilizado para análise e visualização
    └── analyze_power_temp.py
```

---

## Descrição do Projeto

O projeto consiste na construção de um pipeline completo de ETL e análise de dados de sistemas HVAC, incluindo:

1. **Aquisição e Simulação de Dados**  
   - Node-RED gera dados simulados de temperatura interior e consumo de energia do HVAC.  
   - Dados meteorológicos históricos exteriores são obtidos via API Open-Meteo.

2. **Transformação e Enriquecimento (Pentaho / Kettle)**  
   - Limpeza, validação e normalização de timestamps.  
   - Filtragem de dados por tipo de sensor.  
   - Agrupamentos por sala e timestamp, com cálculo de métricas derivadas (`avg_power`, `temp_diff`, `efficiency`).  
   - Exportação para CSV, XML e SQLite.

3. **Análise e Visualização (Python)**  
   - Produção de gráficos para explorar padrões de consumo energético e comportamento térmico.  
   - Gráficos incluídos:
     - Power vs Outdoor Temperature
     - Power vs Temperature Difference
     - 3D Scatter: Power vs Temp Factors
     - Histogram of Efficiency
     - Boxplot of Avg Power per Room

---

## Como Executar

### Pré-requisitos

- **Node-RED** (para simulação de dados)
- **Pentaho Data Integration (Kettle)** versão 10.2 ou superior
- **Python 3.10+** com pacotes:
  - pandas ≥ 2.0
  - matplotlib ≥ 3.7
  - seaborn ≥ 0.13
  - qrcode

### Passos de Execução

1. **Gerar dados simulados com Node-RED**
   - Executar o fluxo Node-RED `hvac_simulation.json` para gerar CSV de entrada.

2. **Executar Transformação/Job no Pentaho**
   - Abrir `dataint/etl_hvac_power.kjb` no Kettle.  
   - Executar o job, que chamará a transformação `etl_climate_analysis.ktr`.  
   - Os ficheiros de saída serão gerados na pasta `data/output/`.

3. **Executar Análise Python**
   - Navegar para a pasta `src/`.  
   - Executar:
     ```bash
     python analyze_power_temp.py
     ```
   - Todos os gráficos e o QR Code serão gerados.

4. **Ver Relatório**
   - Relatório final: `doc/28602_doc.pdf`.
