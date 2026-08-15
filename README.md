# AMCB Studio Public

Hospedagem pública das páginas de suporte, privacidade e termos dos aplicativos da AMCB Studio.

Este repositório não contém código-fonte dos aplicativos. Cada produto mantém seu próprio repositório; aqui ficam apenas documentos que precisam de URLs públicas estáveis para distribuição nas lojas.

## Estrutura

- `docs/apps/uploadfit/`: suporte, privacidade e termos do UploadFit;
- `docs/apps/pdf-target/`: suporte e privacidade do PDF Target.

O GitHub Pages deve ser configurado para publicar a pasta `docs` da branch `main`.

Valide documentos e links locais antes de publicar:

```sh
python3 scripts/validate_site.py
```

