# -*- coding: utf-8 -*-
"""Gera og.png (1200x630) — banner de preview do link (navy + dourado)."""
import numpy as np
from pathlib import Path
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

OUT=Path(r"G:\Drives compartilhados\Gestao_AI\carteira_etf_site")
GOLD="#C2A14D"; GOLDL="#D9BE7A"; WHITE="#F5F3EE"; MUTED="#AEB9C4"

fig=plt.figure(figsize=(12,6.30),dpi=100)
ax=fig.add_axes([0,0,1,1]); ax.axis("off"); ax.set_xlim(0,1); ax.set_ylim(0,1)

# fundo navy com gradiente diagonal sutil
c0=np.array([13,30,52])/255; c1=np.array([26,59,92])/255
gx=np.linspace(0,1,300); gy=np.linspace(0,1,300)
X,Y=np.meshgrid(gx,gy); t=(X*0.6+Y*0.4)
img=(c0.reshape(1,1,3)*(1-t)[...,None]+c1.reshape(1,1,3)*t[...,None])
ax.imshow(img,extent=[0,1,0,1],aspect="auto",origin="lower",zorder=0)

# moldura dourada fina
ax.add_patch(Rectangle((0.035,0.07),0.93,0.86,fill=False,ec=GOLD,lw=1.5,alpha=0.65,zorder=2))

# kicker
ax.text(0.5,0.80,"G E S T Ã O   C E R T I F I C A D A   A N B I M A",
        ha="center",va="center",color=GOLD,fontsize=14,family="sans-serif",weight="bold",zorder=3)
# wordmark
ax.text(0.5,0.60,"ROMULO CORCINO",ha="center",va="center",color=WHITE,
        fontsize=60,family="serif",weight="bold",zorder=3)
# linha dourada
ax.plot([0.36,0.64],[0.475,0.475],color=GOLD,lw=2.2,zorder=3)
# subtítulo
ax.text(0.5,0.385,"Carteira de ETFs para Pessoa Física",ha="center",va="center",
        color=GOLDL,fontsize=25,family="serif",style="italic",zorder=3)
# descritor
ax.text(0.5,0.20,"4 perfis   ·   retorno líquido de IR   ·   backtest contra o CDI",
        ha="center",va="center",color=MUTED,fontsize=15.5,family="sans-serif",zorder=3)

fig.savefig(OUT/"og.png"); plt.close(fig)
print("og.png gerado (1200x630)")
