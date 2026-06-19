# Carteira de ETFs · TAG Investimentos

Página única (HTML estático) com:
- **Quiz de perfil** do investidor (6 perguntas → RF / Conservador / Moderado / Agressivo)
- **Carteiras** por perfil (ETFs + fundos listados isentos), com alocação por classe
- **Backtest** contra o CDI (bruto e líquido de IR), Ulcer Index e mapa risco-retorno
- **Racional** da construção

Acesso: **https://romulocorcinotag.github.io/carteira-etf/**

## Stack
- HTML/CSS puro + [Chart.js](https://www.chartjs.org/) (CDN). Sem build.
- `data.js` — séries semanais e métricas geradas a partir do backtest (fonte: Comdinheiro, 03/05/2021–18/06/2026).

## Aviso
Material informativo/educacional. Não é oferta nem recomendação. Rentabilidade passada não garante futura. Backtest usa proxies de índices/ETFs e premissas de IR simplificadas.
